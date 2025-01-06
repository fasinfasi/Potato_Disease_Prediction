# 🥔Potato Plant Disease Detection 🩺

#### This repository contains the source code and documentation for a web-based application that helps farmers detect potato plant diseases by analyzing leaf images. Users can either upload a photo from their gallery or capture one using their device's camera. The project integrates machine learning for accurate disease prediction and is deployed using modern frameworks and tools.

## Purpose💡
Agriculture faces significant challenges from plant diseases, which can lead to reduced yields and economic loss. By providing an easy-to-use tool for farmers, this project aims to:

- Quickly identify potato plant diseases.
- Reduce dependence on manual diagnosis.
- Provide insights for timely treatment and disease prevention.

## Features✨
- Image Upload and Capture: Upload images from the gallery or capture directly via the camera.
- Machine Learning Model: Built using TensorFlow and Keras with 93.88% accuracy.
- Visualization: Data insights visualized using matplotlib and seaborn.
- API Integration: Backend powered by FastAPI with TensorFlow Serve.
- Cloud Deployment: TensorFlow Lite model deployed on Google Cloud Platform (GCP).
- API Testing: Endpoints tested using Postman.

## Tech Stack
#### Frontend
- Framework: React.js
- Key Features: Responsive design, user-friendly interface for both desktop and mobile devices.
#### Backend
- Framework: FastAPI
- Model Serving: TensorFlow Serve for real-time predictions.
- Hosting: Deployed on a local server or cloud environments.
#### Machine Learning
- Libraries: TensorFlow, Keras, seaborn, matplotlib
- Development Platform: Google Colab for efficient training and experimentation.
- Dataset: Sourced from Kaggle, specifically curated for potato plant diseases.
##### Techniques Used:
- Data Augmentation: To enhance dataset diversity and improve model robustness.
- Transfer Learning: Leveraging pre-trained models for faster and more accurate training.

## Deployment
- Cloud Service: Google Cloud Platform (GCP)
- API Testing: Postman for ensuring reliable and secure API endpoints.

## Dataset and Model
- Source: Kaggle https://www.kaggle.com/datasets/arjuntejaswi/plant-village 
  where I only took potato plant leaves datasets omit other leaves datasets
- Images: Labeled images of potato leaves, categorized by disease types like 'Potato Early blight', 'Potato Late blight' and 'healthy leaves'.
#### Model Training
- Architecture: CNN (Convolutional Neural Network) based on TensorFlow and Keras.
- Performance: Achieved 93.88% accuracy on the validation dataset.
- Visualization: Model accuracy and loss graphs plotted using matplotlib.

## Installation and Setup
### Prerequisites
- Python 3.9+
- Node.js and npm
- Google Cloud Platform (GCP) account
- Postman for API testing

### Clone the Repository
```
git clone https://github.com/fasinfasi/Potato_Disease_Prediction.git
cd potato-disease-detection  
```

#### 1. Frontend Setup
Navigate to the frontend directory:
```
cd frontend
```
Install dependencies:
```
npm install
```
Run the React development server:
```
npm start
```
#### 2. Backend Setup
Navigate to the backend directory:
```
cd api
```
Start the FastAPI server:
```
uvicorn main:app --reload
```

## Usage
#### 1. Access the Web App
Open the frontend in your browser by navigating to http://localhost:3000 (default React port).
#### 2. Upload or Capture Image
Select or capture an image of a potato leaf.
Submit the image for disease detection.
#### 3. View Results
The model predicts the type of disease or confirms a healthy leaf.
Results are displayed on the screen.

##### Feel free to use and adapt this README! Let me know if you'd like further refinements🤗.
