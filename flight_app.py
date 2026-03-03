import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("flight_model.pkl")

st.title("✈️ Flight Price Prediction App")

st.sidebar.header("Enter Flight Details")

airline = st.sidebar.selectbox("Airline", [
    "SpiceJet", "AirAsia", "Vistara", "GO_FIRST",
    "Indigo", "Air India"
])

source_city = st.sidebar.selectbox("Source City", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata",
    "Hyderabad", "Chennai"
])

destination_city = st.sidebar.selectbox("Destination City", [
    "Delhi", "Mumbai", "Bangalore", "Kolkata",
    "Hyderabad", "Chennai"
])

departure_time = st.sidebar.selectbox("Departure Time", [
    "Early_Morning", "Morning", "Afternoon",
    "Evening", "Night", "Late_Night"
])

arrival_time = st.sidebar.selectbox("Arrival Time", [
    "Early_Morning", "Morning", "Afternoon",
    "Evening", "Night", "Late_Night"
])

travel_class = st.sidebar.selectbox("Class", [
    "Economy", "Business"
])

stops = st.sidebar.selectbox("Stops", [0, 1, 2])

duration = st.sidebar.number_input("Duration (in hours)", min_value=0.5, max_value=20.0)

days_left = st.sidebar.slider("Days Left for Departure", 1, 50)

if st.sidebar.button("Predict Price"):

    input_data = pd.DataFrame([[
        airline,
        source_city,
        departure_time,
        stops,
        arrival_time,
        destination_city,
        travel_class,
        duration,
        days_left
    ]], columns=[
        "airline",
        "source_city",
        "departure_time",
        "stops",
        "arrival_time",
        "destination_city",
        "class",
        "duration",
        "days_left"
    ])

    prediction = model.predict(input_data)[0]

    st.success(f"💰 Estimated Flight Price: ₹{prediction:,.0f}")
