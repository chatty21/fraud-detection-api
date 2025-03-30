from flask import Flask, request, jsonify
import pandas as pd
import joblib
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

# Load model and encoder
model = joblib.load("fraud_detection_model.pkl")
encoder = joblib.load("ordinal_encoder.pkl")

# Define expected columns and categorical columns
expected_cols = ['cc_num', 'merchant', 'category', 'amt', 'gender', 'city', 'state',
                 'zip', 'lat', 'long', 'city_pop', 'job', 'unix_time', 'merch_lat',
                 'merch_long', 'hour', 'day', 'weekday', 'month', 'age']
categorical_cols = ['merchant', 'category', 'gender', 'city', 'state', 'job']

@app.route('/')
def home():
    return "✅ Fraud Detection API with Swagger is live! Go to /apidocs to test it."

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict if a transaction is fraudulent.
    ---
    tags:
      - Fraud Detection
    parameters:
      - name: input
        in: body
        required: true
        schema:
          id: FraudInput
          type: object
          properties:
            cc_num:
              type: number
              example: 1234567890123456
            merchant:
              type: string
              example: "Fraud_Merchant"
            category:
              type: string
              example: "grocery_pos"
            amt:
              type: number
              example: 20.0
            gender:
              type: string
              example: "M"
            city:
              type: string
              example: "New York"
            state:
              type: string
              example: "NY"
            zip:
              type: integer
              example: 10001
            lat:
              type: number
              example: 40.71
            long:
              type: number
              example: -74.01
            city_pop:
              type: integer
              example: 8000000
            job:
              type: string
              example: "Engineer"
            unix_time:
              type: integer
              example: 1325376000
            merch_lat:
              type: number
              example: 40.73
            merch_long:
              type: number
              example: -73.99
            hour:
              type: integer
              example: 14
            day:
              type: integer
              example: 12
            weekday:
              type: integer
              example: 2
            month:
              type: integer
              example: 1
            age:
              type: integer
              example: 30
    responses:
      200:
        description: Fraud prediction result
        schema:
          type: object
          properties:
            prediction:
              type: integer
              example: 0
    """
    try:
        input_data = request.get_json()
        df = pd.DataFrame([input_data])
        df = df[expected_cols]

        # Encode categorical columns
        df[categorical_cols] = encoder.transform(df[categorical_cols])

        prediction = model.predict(df)[0]
        return jsonify({"prediction": int(prediction)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)