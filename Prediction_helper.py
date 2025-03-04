import pandas as pd
from joblib import load

model_cat = load("artifacts/Model_cat.joblib")
# cat_encoder = load("artifacts\cat_encoder.joblib")

def preprocess_input(features):
    expected_columns = [
        'age', 'sex', 'chest_pain_type', 'country', 'resting_blood_pressure',
        'cholesterol', 'fasting_blood_sugar', 'Restecg', 'max_heart_rate_achieved',
        'exercise_induced_angina', 'st_depression', 'st_slope_type',
        'num_major_vessels', 'thalassemia_type'
    ]

    df = pd.DataFrame([features], columns=expected_columns)
    # df = pd.DataFrame(0, columns=expected_columns, index=[0])
    df = encode_label(df)
    return df

def encode_label(df):
    for col in ['sex', 'chest_pain_type', 'country', 'Restecg',
                 'st_slope_type', 'thalassemia_type']:
        encoder = load(f'artifacts/{col}_label_encoder.joblib')  # Load the encoder
        df[col] = encoder.transform(df[col])
    return df
def predict(features):
    input_df = preprocess_input(features)
    prediction = model_cat.predict(input_df)
    return int(prediction)