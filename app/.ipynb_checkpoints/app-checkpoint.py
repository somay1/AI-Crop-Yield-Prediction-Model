from flask import Flask, render_template, request
import joblib
from preprocess import preprocess_input

app = Flask(__name__)

# Load the trained model
model = joblib.load("xgb_crop_yield_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect form data
        state = request.form['state']
        crop_year = request.form['crop_year']
        season = request.form['season']
        fertilizer = request.form['fertilizer']
        pesticide = request.form['pesticide']
        rainfall = request.form['rainfall']
        crop = request.form['crop']

        # Preprocess input
        input_df = preprocess_input(state, crop_year, season, fertilizer, pesticide, rainfall, crop)

        # Make prediction
        prediction = model.predict(input_df)[0]
        prediction = round(prediction, 2)

        return render_template('result.html', prediction_text=f"Predicted Crop Yield: {prediction} tons/hectare 🌾")

    except Exception as e:
        return render_template('result.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
