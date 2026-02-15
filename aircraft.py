import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("aircraft1.pkl")

st.set_page_config(page_title="Engine Failure Predictor", layout="centered")

st.title("AIRCRAFT Engine Failure Prediction System")
st.markdown("Enter engine parameters below to predict failure type.")

st.divider()

st.header("Engine Parameters")

# Since Type is already numeric (0,1,2) in dataset
machine_type = st.selectbox("Machine Type", [0, 1, 2])

air_temp = st.number_input("Air Temperature (K)", 250.0, 350.0)
process_temp = st.number_input("Process Temperature (K)", 250.0, 350.0)
rotational_speed = st.number_input("Rotational Speed (rpm)", 0, 50000)
torque = st.number_input("Torque (Nm)", 0.0, 100.0)
vibration = st.number_input("Vibration Levels", 0.0, 100.0)
operational_hours = st.number_input("Operational Hours", 0.0, 1000.0)

st.divider()

if st.button("Predict Failure Type"):

    input_data = np.array([[
        machine_type,
        air_temp,
        process_temp,
        rotational_speed,
        torque,
        vibration,
        operational_hours
    ]])

    prediction = model.predict(input_data)

    st.success(f"Prediction Result: {prediction[0]}")
