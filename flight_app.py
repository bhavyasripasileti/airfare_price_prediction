import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load model
model = joblib.load("flight_model.pkl")

st.set_page_config(page_title="Flight Price Prediction", layout="wide")

st.title("✈️ Flight Price Prediction")

st.sidebar.header("Search Flights")

airline = st.sidebar.selectbox("Airline", [
    "SpiceJet", "AirAsia", "Vistara", "GO_FIRST",
    "Indigo", "Air India"
])

source_city = st.sidebar.selectbox("From", [
    "Delhi", "Mumbai", "Bangalore",
    "Kolkata", "Hyderabad", "Chennai"
])

destination_city = st.sidebar.selectbox("To", [
    "Delhi", "Mumbai", "Bangalore",
    "Kolkata", "Hyderabad", "Chennai"
])

travel_class = st.sidebar.selectbox("Class", ["Economy", "Business"])

stops = st.sidebar.selectbox("Stops", [0, 1, 2])

journey_date = st.sidebar.date_input("Journey Date")

# Calculate days_left automatically
today = datetime.today().date()
days_left = (journey_date - today).days

if days_left <= 0:
    st.error("Please select a future date.")
else:

    if st.sidebar.button("Search Flights"):

        # Hidden internal values (model requirement)
        departure_time = "Morning"
        arrival_time = "Evening"

        # Estimate duration automatically based on route
        estimated_duration = 2.5 if source_city != destination_city else 1.0

        input_data = pd.DataFrame([[
            airline,
            source_city,
            departure_time,
            stops,
            arrival_time,
            destination_city,
            travel_class,
            estimated_duration,
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

        st.success(f"💰 Estimated Ticket Price: ₹{prediction:,.0f}")

        st.info(f"⏱ Estimated Flight Duration: {estimated_duration} hours")
