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

**EfficientNet** achieved the best overall performance.



## 🖥️ Application Interface

### Main Screens

1. Home Page
   ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/home.jpg?raw=true)
   
 
3. Login Page
      ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/Connexion.jpg?raw=true)
 
5. Registration Page
    ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/Page%20d%E2%80%99inscription.jpg?raw=true)
 
7. Prediction Page
   ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/Page%20de%20pr%C3%A9diction.jpg?raw=true)
  
9. Result Page
    ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/R%C3%A9sultat%20de%20Pr%C3%A9diction.jpg?raw=true)

11. Diagnostic Report Page
     ![image alt](https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN/blob/main/Rapport%20d%C3%A9taill%C3%A9%20du%20diagnostic.png?raw=true)
 














## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/hajarbaider/D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN.git
cd D-tection-de-la-pneumonie-l-aide-de-mod-les-CNN
```

### 2.Download Large Files (Model)

This project uses Git LFS for large files (the .h5 model):
```bash
git lfs install
git lfs pull
```
Run the Application
```bash
python app.py
```
