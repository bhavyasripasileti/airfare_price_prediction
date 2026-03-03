import streamlit as st
import pandas as pd
import joblib
from datetime import datetime, time

# Load model
model = joblib.load("flight_model.pkl")

st.set_page_config(page_title="Flight Price Prediction", layout="wide")

st.title("✈️ AI Flight Fare Estimator")

st.sidebar.header("Search Flights")

# Inputs
airline = st.sidebar.selectbox("Airline", [
    "SpiceJet", "AirAsia", "Vistara",
    "GO_FIRST", "Indigo", "Air India"
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

departure_time_input = st.sidebar.time_input("Departure Time", value=time(9, 0))

# Convert real time into model category
hour = departure_time_input.hour

if 5 <= hour < 12:
    departure_time = "Morning"
elif 12 <= hour < 17:
    departure_time = "Afternoon"
elif 17 <= hour < 21:
    departure_time = "Evening"
else:
    departure_time = "Night"

arrival_time = "Evening"

# Calculate days_left
today = datetime.today().date()
days_left = (journey_date - today).days

if days_left <= 0:
    st.error("Please select a future date.")
else:

    if st.sidebar.button("Search Flights"):

        # Dynamic duration logic
        base_duration = 1.5 if source_city != destination_city else 1.0
        estimated_duration = base_duration + (stops * 0.8)

        # Prepare model input
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

        # Fare category logic
        if prediction < 4000:
            category = "🟢 Budget Deal"
        elif prediction < 8000:
            category = "🟡 Standard Fare"
        else:
            category = "🔴 Expensive Fare"

        # Layout
        col1, col2 = st.columns(2)

        with col1:
            st.success(f"💰 Estimated Ticket Price: ₹{prediction:,.0f}")
            st.markdown(f"### {category}")

        with col2:
            st.info(f"⏱ Estimated Flight Duration: {estimated_duration:.1f} hours")
            st.write(f"📅 Days Left: {days_left}")

        # Booking suggestion
        if days_left <= 5:
            st.warning("⚠️ Prices may increase soon. Consider booking now!")
        elif days_left <= 15:
            st.info("📈 Fares are moderately priced. Monitor for deals.")
        else:
            st.success("🎯 Good time to monitor fares.")
