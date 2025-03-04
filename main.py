import streamlit as st
import numpy as np
import pandas as pd

from Prediction_helper import predict

# Streamlit UI
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")
# st.title("💓 Heart Disease Prediction")
  # Streamlit interface
st.markdown("""
    <style>
    .header {
        color: #ffffff;
        background-color: #0073e6;
        padding: 15px;
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        border-radius: 10px;
    } 
 </style>
    """, unsafe_allow_html=True)
# Title of the app
st.markdown('<div class="header"> 💓 Heart Disease Prediction</div>', unsafe_allow_html=True)
import streamlit as st
import numpy as np
import pandas as pd

# Create the container for the form
with st.container():
    col1, col2, col3 = st.columns([1, 2, 1])

    # Column 1 - Patient Information
    with col1:
        st.write("### Patient Information")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        sex = st.selectbox("Sex", options=["Male", "Female"], key="sex", help="Select the gender of the patient")
        st.image("https://media.istockphoto.com/id/1165333893/vector/medical-document.jpg?s=612x612&w=0&k=20&c=EGfYzaUUvwH3vKgk6EUDN6AvFfSQRiHv7oVrlCxpE48=", use_container_width=True)

    # Column 2 - Health Data
    with col2:
        st.write("### Health Data")
        chest_pain_type = st.selectbox("Chest Pain Type", options=['typical_angina', 'asymptomatic', 'non-anginal', 'atypical_angina'], key="chest_pain_type")
        country = st.selectbox("Country", options=['Cleveland', 'Hungary', 'Switzerland', 'VA Long Beach'], key="country")
        resting_blood_pressure = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=300, step=1)
        cholesterol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, step=1)
        fasting_blood_sugar = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], key="fasting_blood_sugar")

    # Column 3 - Test Results
    with col3:
        st.write("### Test Results")
        Restecg = st.selectbox("Resting Electrocardiographic Results", options=['left_ventricular_hypertrophy', 'normal', 'stt abnormality'], key="Restecg")
        max_heart_rate_achieved = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, step=1)
        exercise_induced_angina = st.selectbox("Exercise Induced Angina", options=[0, 1], key="exercise_induced_angina")
        st_depression = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, step=0.1)
        st_slope_type = st.selectbox("ST Slope Type", options=['downsloping', 'flat', 'upsloping'], key="st_slope_type")
        num_major_vessels = st.number_input("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, step=1)
        thalassemia_type = st.selectbox("Thalassemia Type", options=['fixed_defect', 'reversable_defect', 'normal'], key="thalassemia_type")

# Organize features into a list or dictionary
features = {
    "age": age,
    "sex": sex,
    "chest_pain_type": chest_pain_type,
    "country": country,
    "resting_blood_pressure": resting_blood_pressure,
    "cholesterol": cholesterol,
    "fasting_blood_sugar": fasting_blood_sugar,
    "Restecg": Restecg,
    "max_heart_rate_achieved": max_heart_rate_achieved,
    "exercise_induced_angina": exercise_induced_angina,
    "st_depression": st_depression,
    "st_slope_type": st_slope_type,
    "num_major_vessels": num_major_vessels,
    "thalassemia_type": thalassemia_type
}

# Button to trigger prediction
st.markdown("<hr>", unsafe_allow_html=True)
if st.button("Predict"):
    prediction = predict(features)
    st.success(f"🫀 Predicted Heart Disease Type: {prediction}")
    # Show the result
    if prediction == 0:
        st.success("The patient has mild or no disease")
        st.balloons()
    else:
        st.success("The patient has significant coronary artery disease")
        st.snow()