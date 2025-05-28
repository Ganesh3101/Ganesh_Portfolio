import streamlit as st
import joblib
import numpy as np

model = joblib.load('static/model.joblib')

st.title("Heart Disease Prediction App ❤️")
st.markdown("Enter the patient details below:")

age = st.number_input("Age", 18, 100, 45)
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (trestbps)", 80, 200, 120)
chol = st.number_input("Serum Cholesterol in mg/dl (chol)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
restecg = st.selectbox("Resting ECG Results (restecg)", [0, 1, 2])
thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", 60, 250, 150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1])
oldpeak = st.number_input("ST Depression Induced by Exercise (oldpeak)", 0.0, 10.0, 1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment (slope)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (ca)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia (thal)", [0, 1, 2, 3])

# Prediction button
if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak, slope,
                            ca, thal]])

    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The patient is likely to have heart disease.")
    else:
        st.success("✅ The patient is unlikely to have heart disease.")