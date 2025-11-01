import pandas as pd
import numpy as np
import joblib

# Load saved encoders
state_encoder = joblib.load("state_encoder.pkl")
season_encoder = joblib.load("season_encoder.pkl")
crop_encoder = joblib.load("crop_encoder.pkl")

def preprocess_input(state, crop_year, season, fertilizer, pesticide, rainfall, crop):
    try:
        state_encoded = state_encoder.transform([state])[0]
    except ValueError:
        state_encoded = -1  # unseen value

    try:
        season_encoded = season_encoder.transform([season])[0]
    except ValueError:
        season_encoded = -1

    try:
        crop_encoded = crop_encoder.transform([crop])[0]
    except ValueError:
        crop_encoded = -1

    # Create dataframe for prediction
    df = pd.DataFrame({
        "State": [state_encoded],
        "Crop_Year": [int(crop_year)],
        "Season": [season_encoded],
        "Fertilizer": [float(fertilizer)],
        "Pesticide": [float(pesticide)],
        "Annual_Rainfall": [float(rainfall)],
        "Crop_x": [crop_encoded]
    })

    return df
