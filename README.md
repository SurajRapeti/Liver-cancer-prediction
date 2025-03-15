# Liver-cancer-prediction
Liver-cancer-prediction-using-machine-learning
Liver Cancer Prediction using Machine Learning
Overview
This project is a Flask-based web application that predicts liver disease using Machine Learning. It takes user input through a web interface and processes it using a trained ML model to classify whether a person is at risk for liver disease.

Features
✅ Web-based interface using Flask
✅ Machine learning model trained on liver disease dataset
✅ Accepts multiple user inputs for prediction
✅ Displays prediction results on a separate webpage

Tech Stack
Flask (Backend)
Pandas, NumPy (Data Processing)
Scikit-learn (Machine Learning)
HTML/CSS (Frontend)
Pickle (Model Serialization)
Dataset
The dataset used for training is stored in liver.csv, containing patient details such as age, gender, bilirubin levels, and protein counts.

Installation & Usage
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/liver-cancer-prediction.git
cd liver-cancer-prediction
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Run the Application
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000/ in your browser to access the web application.

Prediction Workflow
The user enters patient details in the web form.
The data is sent to the Flask backend for processing.
The trained model (stored as liver.pkl) predicts liver disease likelihood.
The result is displayed on the prediction page.

File Structure
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
├── README.md              # Project documentation  
Contributing
Feel free to contribute by improving the model, UI, or backend logic. Fork the repo and submit a pull request!
