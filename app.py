import streamlit as st
import numpy as np
import joblib

# Load model & scaler
model = joblib.load("catboost_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Prediksi Kekuatan Tekan Beton (Concrete Compressive Strength)")

st.write("Masukkan nilai fitur:")

# Input fitur
cement = st.number_input("Cement", min_value=0.0)
blast_furnace_slag = st.number_input("Blast Furnace Slag", min_value=0.0)
fly_ash = st.number_input("Fly Ash", min_value=0.0)
water = st.number_input("Water", min_value=0.0)
superplasticizer = st.number_input("Superplasticizer", min_value=0.0)
coarse_aggregate = st.number_input("Coarse Aggregate", min_value=0.0)
fine_aggregate = st.number_input("Fine Aggregate", min_value=0.0)
age = st.number_input("Age", min_value=1)

if st.button("Prediksi"):
    input_data = np.array([[
        cement, blast_furnace_slag, fly_ash, water,
        superplasticizer, coarse_aggregate, fine_aggregate, age
    ]])
    
    # Scaling
    input_scaled = scaler.transform(input_data)
    
    # Prediksi
    prediction = model.predict(input_scaled)
    
    st.success(f"Prediksi Kekuatan Tekan Beton: {prediction[0]:.2f} MPa")
