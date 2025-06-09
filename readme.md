# 🛡️ Fraud Detection API

An AI-powered Flask API that predicts whether a financial transaction is fraudulent based on transaction metadata. Built using a trained machine learning model with a beautiful interactive frontend.

[![Render Status](https://img.shields.io/badge/render-live-success?style=flat-square&logo=render)](https://fraud-detection-api-19p9.onrender.com)

---

## 🚀 Features

- 🔍 Predicts fraud from transaction metadata (merchant, amount, location, etc.)
- 🧩 Flask API with `/predict` route
- 🧪 Swagger UI for API testing → [View Docs](https://fraud-detection-api-19p9.onrender.com/apidocs)
- 🌐 Beautiful HTML form → [Launch Form](https://fraud-detection-api-19p9.onrender.com/form)
- 🧠 Uses a trained `RandomForestClassifier`

---

## 🧠 Tech Stack

- Python, Flask
- Scikit-learn, Joblib
- HTML + CSS (custom frontend)
- Flasgger (Swagger API Docs)

---

## 📂 Project Structure

fraud-detection-api/
├── app.py # Flask backend API
├── fraud_detection_model.pkl # Trained ML model
├── ordinal_encoder.pkl # Preprocessing encoder
├── templates/
│ └── index.html # Frontend form UI
├── requirements.txt
├── Procfile
└── README.md


---

## ⚙️ Local Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/chatty21/fraud-detection-api.git
cd fraud-detection-api

(Optional) Create a Virtual Environment

python -m venv fraud_env
source fraud_env/bin/activate  # Windows: fraud_env\Scripts\activate

### Install Dependencies
```bash
pip install -r requirements.txt
---

### Run the App
```bash
python app.py
---

App runs at: http://127.0.0.1:5050

Swagger UI: http://127.0.0.1:5050/apidocs

📮 Example Request (POST /predict)
json
Copy
Edit
{
  "cc_num": 1234567890123456,
  "merchant": "SuperMart",
  "category": "grocery_pos",
  "amt": 120.50,
  "gender": "F",
  "city": "San Francisco",
  "state": "CA",
  "zip": 94107,
  "lat": 37.77,
  "long": -122.42,
  "city_pop": 870000,
  "job": "Data Scientist",
  "unix_time": 1325376000,
  "merch_lat": 37.78,
  "merch_long": -122.43,
  "hour": 15,
  "day": 18,
  "weekday": 3,
  "month": 5,
  "age": 32
}
🧠 Model Info
Classifier: RandomForestClassifier

Dataset: 1M+ real-like financial transactions

Balanced using class_weight='balanced'

🌐 Live Demo
🔗 Main API: fraud-detection-api-19p9.onrender.com

🧪 Swagger UI

🌐 Frontend Form

🚀 Deployment Options
This app can be deployed on:

Render

Google Cloud Run

Replit

Vercel (with ASGI wrapper)

📄 License
MIT License – feel free to use, modify, and share.






