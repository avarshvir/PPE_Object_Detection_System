# PPE Object Detection System
The PPE (Personal Protective Equipment) Object Detection System is a deep learning–based computer vision application designed to automatically detect whether workers are wearing required safety equipment such as **Helmet, Vest, Gloves, and Boots** in environments like construction sites and factories.

This system aims to improve workplace safety by automating PPE compliance monitoring using camera-based inspection instead of manual human observation.

---

## Problem Statement
Construction sites, factories, and other hazardous working environments require workers to wear proper safety equipment to minimize the risk of injury. Manual inspection of PPE compliance is time-consuming, costly, and prone to human error.

To address this problem, I developed an automated PPE detection system that uses deep learning and object detection to identify safety equipment worn by workers in real time using camera feeds. This system can be further integrated with embedded systems and access-control mechanisms (such as automatic doors or alarms) to enforce safety compliance.

---

## Detected PPE Classes
- Helmet  
- Vest  
- Gloves  
- Boots  

---

## Tech Stack
- **Programming Language**: Python
- **Libraries**: Ultralytics(for YOLO), Gradio(for UI), Open CV, PyTorch
- **Dataset**: Roboflow PPE Dataset -> [Link](https://universe.roboflow.com/randomlangyan/ppe-project-7brvs/dataset/3)
- **Tools**: VS code (Development), Google Colab(Training)
- **Deployment**: HuggingFace -> [Link](https)

---

## Model Training Approach

- Used a **pretrained YOLOv8 model** trained on the COCO dataset
- Applied **transfer learning** to fine-tune the model on a custom PPE dataset
- Training performed on Google Colab using a **Tesla T4 GPU**
- Model selection based on validation performance (`best.pt`)

---

## Model Evaluation Metrics

The trained model was evaluated using IoU-based object detection metrics on the validation dataset:
```
Precision: 0.8946163686006668
Recall: 0.8912529904398928
mAP@50: 0.911266088587406
mAP@50-95: 0.6869156525972596
```
These metrics indicate strong detection accuracy and reliable localization of PPE items.

---



## Getting Started
### Step 1: Clone Repository
```
- git clone https://github.com/avarshvir/PPE_Object_Detection_System.git
- cd PPE_Object_Detection_System
```
### Step 2: Model Training (Google Colab)
```
- Open Google Colab and change runtime to T4 GPU
- Upload PPE_Dataset.zip (make sure dataset in zip format)
- Run Actual_Code_To_Train_Model.ipynb to train the model
```
### Step 3: Application Setup
```
- Download the trained best.pt model from Colab (or use the provided model)
- Open the project in VS Code
```

### Step 4: Run the Application
```
- cd PPE_Application (make sure you are inside PPE_Object_Detection_System)
- python app.py
```

---
## Project Directory Structure
```
PPE_Object_Detection_System/
├── PPE_Application/
│   ├── app.py
│   └── best.pt
├── Actual_Code_To_Train_Model.ipynb
├── PPE_Dataset.zip
├── LICENSE
└── README.md
```

## About the Developer
- Name: Arshvir
- Stack Overflow: [arshvir](https://stackoverflow.com/users/17771039/arshvir)
- GitHub: [https://github.com/avarshvirr](https://github.com/avarshvir)
- Portfolio: [https://avarshvir.github.io/arshvir/](https://avarshvir.github.io/arshvir/)
---

## Contributing
Feel free to contribute to this repository by improving it performance and application ideas. 

## Star
Star or Love the repo if you like it :)
