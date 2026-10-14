import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_marks_model (1).pkl")

# App title
st.title("Student Marks Prediction")
st.write("Welcome to my Machine Learning Project")
st.header("Predict Your Marks")

# Study Hours slider
st.subheader("Study Hours")

study_hours = st.slider(
    "Select your study hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5
)

# Attendance slider
st.subheader("Attendance (%)")

attendance = st.slider(
    "Select your attendance percentage",
    min_value=0,
    max_value=100,
    value=90,
    step=1
)

# Prediction
if st.button("Predict Marks"):
    input_data = pd.DataFrame({
        "Study_Hours": [study_hours],
        "Attendance": [attendance]
    })

    predicted_marks = model.predict(input_data)

    st.success(
        f"Predicted Marks: {predicted_marks[0]:.2f}"
    )

