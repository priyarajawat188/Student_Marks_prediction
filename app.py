import streamlit as st
import pandas as pd
import joblib

    # Load the trained model
model = joblib.load("student_marks_model (1).pkl")

# App title
st.title("Student Marks Prediction")
st.write("Welcome to my Machine Learning Project")
st.header("Predict Your Marks")

# User inputs
study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=90.0
)

# Prediction
if st.button("Predict Marks"):
    input_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance]
    })

    predicted_marks = model.predict(input_data)

    st.success(f"Predicted Marks: {predicted_marks[0]:.2f}")
