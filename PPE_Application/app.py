import gradio as gr
from ultralytics import YOLO

model = YOLO("best.pt")

PPE_OPTIONS = ["Helmet", "Vest", "Gloves", "Boots"]

#function to detect PPE and check compliance
def detect_ppe(image, required_items):
    if image is None:
        return None, "Image not found. Please upload an image."

    if not required_items:
        return image, "No PPE requirement selected"

    results = model(image)
    detected = set() #set to store detected PPE items

    for r in results:
        for c in r.boxes.cls:
            detected.add(model.names[int(c)]) #add detected PPE item to the set
        annotated = r.plot()

    required = set(required_items)
    missing = required - detected

    if len(missing) == 0:
        status = "ACCEPTED - Required PPE detected"
    else:
        status = f"REJECTED - Missing: {', '.join(missing)}, please wear the required PPE."

    return annotated, status

#gradio interface for UI
demo = gr.Interface(
    fn=detect_ppe,
    inputs=[
        gr.Image(type="numpy", label="Input Image / Webcam"),
        gr.CheckboxGroup(
            choices=PPE_OPTIONS,
            value=PPE_OPTIONS,
            label="Select Required PPE"
        )
    ],
    outputs=[
        gr.Image(label="Detection Result"),
        gr.Textbox(label="PPE Compliance Status")
    ],
    title="PPE Compliance Detection System",
    description="Detect PPE using YOLOv8 and verify compliance based on selected requirements"
)

demo.launch() #launch the gradio app
