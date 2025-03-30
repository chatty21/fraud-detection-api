# 🛡️ Fraud Detection API

An AI-powered Flask API that predicts whether a financial transaction is **fraudulent** based on transaction metadata. Built using a trained machine learning model with a beautiful interactive frontend.

---

## 🚀 Features

- Predicts fraud from transaction metadata (location, merchant, amount, etc.)
- Flask API with `/predict` route
- Integrated Swagger UI for testing (`/apidocs`)
- Beautiful HTML frontend (`index.html`)
- Uses a trained `RandomForestClassifier`

---

## 🧠 Tech Stack

- Python + Flask
- Scikit-learn + joblib
- HTML + CSS (Frontend)
- Flasgger (Swagger API Docs)

---

## 📂 Project Structure

```
bank-fraud/
├── app.py                      # Flask backend API
├── fraud_detection_model.pkl   # Trained ML model
├── ordinal_encoder.pkl         # Preprocessing encoder
├── templates/
│   └── index.html              # Frontend UI
├── requirements.txt
└── README.md
```

---

## 📦 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/fraud-detection-api.git
cd fraud-detection-api
```

### 2. Create Virtual Environment (Optional but recommended)
```bash
python -m venv fraud_env
source fraud_env/bin/activate  # On Windows: fraud_env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

Visit your browser:
```
http://127.0.0.1:5050
```

Swagger Docs:
```
http://127.0.0.1:5050/apidocs
```

---

## 📮 Example Request (POST `/predict`)

```json
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
```

---

## 🧠 Model Info
- Model: `RandomForestClassifier`
- Trained on a ~1M row dataset
- Balanced with `class_weight='balanced'`

---

## 🌐 Deployment (Optional)
You can deploy the app using:
- [Render](https://render.com/)
- [Google Cloud Run](https://cloud.google.com/run)
- [Replit](https://replit.com/)

---

## 📄 License
MIT License. Free to use and modify.