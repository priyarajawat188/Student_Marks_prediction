
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_marks_model (1).pkl")

# App title
st.title("Student Marks Prediction")
st.write("Welcome to my Machine Learning Project")
st.header("Predict Your Marks")

# Study Hours input
st.subheader("Study Hours")

study_hours_slider = st.slider(
    "Select study hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0,
    step=0.5,
    key="study_slider"
)

study_hours = st.number_input(
    "Or enter study hours",
    min_value=0.0,
    max_value=24.0,
    value=study_hours_slider,
    step=0.5,
    key="study_input"
)

# Attendance input
st.subheader("Attendance (%)")

attendance_slider = st.slider(
    "Select attendance",
    min_value=0.0,
    max_value=100.0,
    value=90.0,
    step=1.0,
    key="attendance_slider"
)

attendance = st.number_input(
    "Or enter attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=attendance_slider,
    step=1.0,
    key="attendance_input"
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
