

import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("student_marks_model (1).pkl")

# App title
st.title("Student Marks Prediction")
st.write("Welcome to my Machine Learning Project")
st.header("Predict Your Marks")

# Study Hours dropdown
st.subheader("Study Hours")

study_hours = st.selectbox(
    "Select your study hours",
    options=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
             11, 12, 13, 14, 15, 16, 17, 18, 
             19, 20, 21, 22, 23, 24],
    index=5
)

# Attendance dropdown
st.subheader("Attendance (%)")

attendance = st.selectbox(
    "Select your attendance percentage",
    options=list(range(0, 101, 5)),
    index=18
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
