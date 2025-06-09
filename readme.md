# 🛡️ Fraud Detection API

An AI-powered Flask API that predicts whether a financial transaction is fraudulent based on transaction metadata. Built using a trained machine learning model with a beautiful interactive frontend.

[![Render Status](https://img.shields.io/badge/render-live-success?style=flat-square&logo=render)](https://fraud-detection-api-19p9.onrender.com)

---

## 🚀 Features

- 🔍 Predicts fraud from transaction metadata (location, merchant, amount, etc.)
- 🧩 Flask API with `/predict` route
- 🧪 Integrated Swagger UI for live testing → [`/apidocs`](https://fraud-detection-api-19p9.onrender.com/apidocs)
- 🌐 Beautiful HTML frontend → [`/form`](https://fraud-detection-api-19p9.onrender.com/form)
- 🧠 Uses a trained `RandomForestClassifier`

---

## 🧠 Tech Stack

- Python + Flask
- Scikit-learn + Joblib
- HTML + CSS (Frontend)
- Flasgger (Swagger API Docs)

---

## 📂 Project Structure

bank-fraud/
├── app.py # Flask backend API
├── fraud_detection_model.pkl # Trained ML model
├── ordinal_encoder.pkl # Preprocessing encoder
├── templates/
│ └── index.html # Frontend UI
├── requirements.txt
└── README.md

yaml
Copy
Edit

---

## ⚙️ Setup Instructions (Local Dev)

### 1. Clone the Repo
```bash
git clone https://github.com/chatty21/fraud-detection-api.git
cd fraud-detection-api
2. (Optional) Create Virtual Environment
bash
Copy
Edit
python -m venv fraud_env
source fraud_env/bin/activate  # On Windows: fraud_env\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run the App Locally
bash
Copy
Edit
python app.py
🌍 Visit: http://127.0.0.1:5050

🔬 Swagger Docs: http://127.0.0.1:5050/apidocs

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
Model: RandomForestClassifier

Trained on a 1M+ row anonymized dataset

Balanced class distribution using class_weight='balanced'

🌐 Live Demo
🔗 Main API: fraud-detection-api-19p9.onrender.com

🧪 Swagger UI (/apidocs)

🌐 Frontend UI (/form)

🚀 Optional Deployment Options
You can easily deploy this app to:

Render (this repo is Render-ready)

Google Cloud Run

Replit

Vercel (via Flask + ASGI with Uvicorn)

📄 License
MIT License – free to use, modify, and share.

yaml
Copy
Edit

---

Would you like me to:
- Save this as `README.md` and push it to your repo?
- Add a screenshot of your Swagger or form in the README?
- Help you write a LinkedIn post to share this project?

Let me know!
