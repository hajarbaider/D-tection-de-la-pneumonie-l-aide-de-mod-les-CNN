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
User → Web Interface → Flask Server → CNN Model → Prediction → Result






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
