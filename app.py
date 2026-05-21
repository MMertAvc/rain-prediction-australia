
import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")
encoders = joblib.load("label_encoders.pkl")

st.title("Will it Rain Tomorrow?")
st.markdown("Input today’s weather details to predict rainfall for tomorrow.")

# Inputs for user
location = st.selectbox("Location", list(encoders["Location"].classes_))
min_temp = st.number_input("Min Temperature (°C)")
max_temp = st.number_input("Max Temperature (°C)")
rainfall = st.number_input("Rainfall (mm)")
wind_gust_dir = st.selectbox("Wind Gust Direction", list(encoders["WindGustDir"].classes_))
wind_gust_speed = st.number_input("Wind Gust Speed")
wind_dir_9am = st.selectbox("Wind Dir 9am", list(encoders["WindDir9am"].classes_))
wind_dir_3pm = st.selectbox("Wind Dir 3pm", list(encoders["WindDir3pm"].classes_))
wind_speed_9am = st.number_input("Wind Speed 9am")
wind_speed_3pm = st.number_input("Wind Speed 3pm")
humidity_9am = st.number_input("Humidity 9am")
humidity_3pm = st.number_input("Humidity 3pm")
pressure_9am = st.number_input("Pressure 9am")
pressure_3pm = st.number_input("Pressure 3pm")
temp_9am = st.number_input("Temperature 9am")
temp_3pm = st.number_input("Temperature 3pm")
rain_today = st.selectbox("Did it Rain Today?", ["No", "Yes"])

# Encode inputs
inputs = [
    encoders["Location"].transform([location])[0],
    min_temp, max_temp, rainfall,
    encoders["WindGustDir"].transform([wind_gust_dir])[0],
    wind_gust_speed,
    encoders["WindDir9am"].transform([wind_dir_9am])[0],
    encoders["WindDir3pm"].transform([wind_dir_3pm])[0],
    wind_speed_9am, wind_speed_3pm,
    humidity_9am, humidity_3pm,
    pressure_9am, pressure_3pm,
    temp_9am, temp_3pm,
    encoders["RainToday"].transform([rain_today])[0]
]

# Predict
if st.button("Predict Rain Tomorrow"):
    result = model.predict([inputs])[0]
    st.success(f"Prediction: {'Yes' if result == 1 else 'No'}")
