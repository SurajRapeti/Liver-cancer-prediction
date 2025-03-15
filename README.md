# Liver Cancer Prediction using Machine Learning  

## Overview  
This project is a **Flask-based web application** that predicts liver disease using **Machine Learning**. It takes user input through a web interface and processes it using a trained **ML model** to classify whether a person is at risk for liver disease.  

## Features  
✅ Web-based interface using **Flask**  
✅ Machine learning model trained on **liver disease dataset**  
✅ Displays prediction results on a separate webpage  

## Tech Stack  
- **Flask** (Backend)  
- **Pandas, NumPy** (Data Processing)  
- **Scikit-learn** (Machine Learning)  
- **HTML/CSS** (Frontend)  
- **Pickle** (Model Serialization)  

## Dataset  
The dataset used for training is stored in **liver.csv**, containing patient details such as **age, gender, bilirubin levels, and protein counts**.  

## Installation & Usage  

### 1. Clone the Repository  

    git clone https://github.com/SurajRapeti/liver-cancer-prediction.git

### 2. Install Dependencies

    pip install -r requirements.txt

### 3. Run the Application

     python app.py
  
### File Structure 
├── static/  
│   ├── 26758.jpg          # Image used in UI  
│  
├── templates/  
│   ├── liver.html         # Main input page  
│   ├── predict.html       # Output page  
│  
├── app.py                 # Flask application  
├── liver.pkl              # Trained machine learning model  
├── liver.csv              # Dataset used for training  
├── liver.ipynb            # Jupyter Notebook with ML model training  

### Prediction Workflow
- The user enters patient details in the web form.
- The data is sent to the Flask backend for processing.
- The trained model (stored as liver.pkl) predicts liver disease likelihood.
- The result is displayed on the prediction page.
