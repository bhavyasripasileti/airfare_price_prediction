# ✈️ AI Flight Fare Estimator

An interactive Machine Learning web application that predicts flight ticket prices based on user inputs such as airline, route, date, class, and number of stops.

Built using **Python, Scikit-Learn, and Streamlit**, this project demonstrates an end-to-end ML workflow from model training to deployment.

---

## 🚀 Live Features

- 📅 Journey date selection (auto days-left calculation)
- 🕒 Departure time selection (mapped to time categories)
- 🛫 Airline selection
- 📍 Source & Destination selection
- 💺 Travel class selection
- 🧳 Stops selection
- 💰 Real-time price prediction
- ⏱ Estimated flight duration display
- 🎯 Fare classification (Budget / Standard / Expensive)
- 📈 Booking recommendation logic

---

## 🧠 Machine Learning Details

- **Dataset:** Clean Flight Price Dataset (300K+ records)
- **Model Used:** Random Forest Regressor
- **Pipeline:**  
  - OneHotEncoding for categorical features  
  - Numerical feature passthrough  
  - Scikit-learn Pipeline integration  
- **Model Performance:**  
  - R² Score ≈ **0.97**

---

## 🏗 Project Architecture

```
airfare_price_prediction/
│
├── flight_app.py          # Streamlit web app
├── flight_model.pkl       # Trained ML model
├── train_model.py         # Model training script
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚙️ How It Works

1. User selects flight details.
2. System calculates:
   - Days left until departure
   - Time category (Morning/Afternoon/Evening/Night)
   - Estimated duration
3. Model predicts ticket price.
4. App displays:
   - Estimated price
   - Duration
   - Fare category
   - Booking recommendation

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib

---

## ▶️ Run Locally

1. Clone the repository:

```bash
git clone https://github.com/your-username/airfare_price_prediction.git
cd airfare_price_prediction
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
streamlit run flight_app.py
```

---

## 🌐 Deployment

This project is deployed using **Streamlit Cloud** for live web access.

---

## 🎯 Key Highlights

- End-to-end ML pipeline implementation
- Production-style model saving & loading
- Clean interactive UI
- Real-time predictions
- Business logic integration
- Git version control workflow

---

## 📌 Future Improvements

- 📈 Price trend visualization
- 🏆 Multi-airline comparison
- 📊 Feature importance visualization
- 🎨 Enhanced UI styling
- 🔍 Model explainability (SHAP)

---

## 👩‍💻 Author

Bhavya Sri Pasileti  
B.Tech | Data Science & AI Enthusiast  
Passionate about building intelligent ML systems and deploying real-world applications.

---

⭐ If you like this project, feel free to star the repository!
