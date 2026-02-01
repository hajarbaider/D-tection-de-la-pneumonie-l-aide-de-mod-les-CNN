# 🫁 Pneumonia Detection using CNN

## 📌 Project Overview

This project focuses on the automatic detection of pneumonia from chest X-ray images using Deep Learning techniques, specifically Convolutional Neural Networks (CNN).

The objective is to assist medical professionals by providing a reliable and fast diagnostic support system.

This project compares multiple CNN architectures to identify the most efficient model for pneumonia classification.

## 🎯 Objectives

- Automate pneumonia detection from X-ray images
- Compare different CNN architectures
- Improve diagnostic accuracy
- Develop a user-friendly web interface
- Provide AI-assisted medical support


## 🧠 Technologies Used

| Category        | Technology |
|-----------------|------------|
| Programming     | Python     |
| Deep Learning   | TensorFlow / Keras |
| Machine Learning| Scikit-learn |
| Backend         | Flask      |
| Frontend        | HTML, CSS, Bootstrap |
| Visualization   | Matplotlib |
| Platform        | Google Colab |

## 📊 Dataset

This project uses the **Chest X-Ray Images (Pneumonia)** dataset available on Kaggle.

The dataset contains chest radiography images classified into three categories:

- Bacterial Pneumonia  
- Viral Pneumonia  
- Normal (Healthy)

All images are in PNG format and are organized into training, validation, and test sets.

The dataset includes thousands of labeled images, providing a strong foundation for training and evaluating deep learning models for pneumonia detection.


## ⚙️ Data Preprocessing

- Image resizing (224×224)
- Normalization
- Data augmentation:
  - Rotation
  - Zoom
  - Horizontal flip
  - Brightness adjustment

## 🏗️ System Architecture
**User** → **Web Interface** → **Flask Server** → **CNN Model** → **Prediction** → **Result**


### Workflow:

1. User uploads X-ray image
2. Image is preprocessed
3. CNN model analyzes image
4. Prediction is generated
5. Result is displayed

## 🧩 Models Implemented

| Model        | Description |
|--------------|-------------|
| VGG16        | Deep CNN with small filters |
| ResNet50     | Residual learning |
| DenseNet121  | Dense connectivity |
| EfficientNet | Optimized scaling |
| CoroNet      | COVID-based CNN |
| CovXNet      | Custom CNN |

## 🏆 Best Model Selection

After comparison, the best performing model was selected based on:

- Accuracy
- Recall
- F1-Score
- Confusion Matrix

EfficientNet achieved the best overall performance.



## 🖥️ Application Interface

### Main Screens

1. Home Page
   <img width="600" height="265" alt="image" src="https://github.com/user-attachments/assets/f3b94602-2f0a-44f2-8750-2660de6cc7fe" />
 
3. Login Page
   <img width="596" height="271" alt="image" src="https://github.com/user-attachments/assets/4234a7af-e292-453e-b21f-2f75ce5cc39a" />
 
5. Registration Page
   <img width="609" height="311" alt="image" src="https://github.com/user-attachments/assets/b0183b26-6953-48fb-939e-884b431c7dd0" />
 
7. Prediction Page
   <img width="600" height="272" alt="image" src="https://github.com/user-attachments/assets/5f43f762-4ba9-4685-8ef3-8e9c18712840" />
  
9. Result Page
    <img width="616" height="300" alt="image" src="https://github.com/user-attachments/assets/589d23f2-32ba-476d-88a5-b8427c54d9ef" />

11. Diagnostic Report Page
    <img width="600" height="216" alt="image" src="https://github.com/user-attachments/assets/8e57d0b5-cb6c-43a9-a0d5-29401456234a" />















Clone the Repository

To clone this repository, use:

git clone https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN.git
cd D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN

Download Large Files (Model)

This project uses Git LFS for large files (the .h5 model):

git lfs install
git lfs pull

Run the Application
python app.py
