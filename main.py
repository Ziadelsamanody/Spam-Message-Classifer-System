import flask
from flask import  Flask,render_template, request
import numpy as np
import joblib


app = Flask(__name__)


# mail = input()
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("SPAM-EMAiLS_MODEL.pkl")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        message = request.form['message']

        # Transform the input text using the loaded vectorizer
        message_vec = vectorizer.transform([message])

        # Make prediction
        prediction = model.predict(message_vec)[0]

        # Get probability scores
        proba = model.predict_proba(message_vec)[0]
        confidence = proba[1] if prediction == 1 else proba[0]

        return render_template('result.html',
                               message=message,
                               prediction='SPAM' if prediction == 1 else 'NOT SPAM',
                               confidence=f"{confidence * 100:.2f}%")


if __name__ == '__main__':
    app.run()