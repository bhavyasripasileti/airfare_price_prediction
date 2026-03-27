# ✈️ AI Flight Fare Estimator
### Predict flight ticket prices with machine learning — instantly.
---
> An end-to-end Machine Learning web application that predicts flight ticket prices based on airline, route, travel class, stops, and journey date — powered by a Random Forest model trained on 300K+ records.

---

## 🌐 Live App

> 🔗 **[Click here to try the app live »](https://airfarepriceprediction-dyer4xmpnetfacacncmzkm.streamlit.app)**

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Machine Learning Details](#-machine-learning-details)
- [Project Architecture](#️-project-architecture)
- [How It Works](#️-how-it-works)
- [Tech Stack](#️-tech-stack)
- [Getting Started](#-getting-started)
- [Deployment](#-deployment)
- [Roadmap](#-roadmap)
- [Author](#-author)

---

## 🔍 Overview

The **AI Flight Fare Estimator** is a full-stack machine learning application that enables users to predict flight ticket prices in real time. Simply enter your flight preferences — and the app instantly returns an estimated fare, duration, fare category, and smart booking recommendation.

This project demonstrates a **complete ML workflow**: data preprocessing → model training → pipeline construction → serialization → web deployment.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📅 **Date-Aware Prediction** | Auto-calculates days left until departure |
| 🕒 **Time-of-Day Mapping** | Maps departure times to Morning / Afternoon / Evening / Night |
| 🛫 **Airline Selection** | Supports multiple airline options |
| 📍 **Route Selection** | Source & destination city picker |
| 💺 **Class & Stops** | Economy / Business + number of stops |
| 💰 **Real-Time Pricing** | Instant fare prediction on user inputs |
| ⏱ **Duration Estimate** | Estimated flight duration display |
| 🎯 **Fare Classification** | Labels fares as Budget / Standard / Expensive |
| 📈 **Booking Recommendation** | Smart logic to advise the best time to book |

---

## 🧠 Machine Learning Details

```
Dataset      →  Clean Flight Price Dataset  (300,000+ records)
Algorithm    →  Random Forest Regressor
R² Score     →  ≈ 0.97  (97% variance explained)
```

### Pipeline Architecture

```
Raw Input Features
        │
        ▼
┌───────────────────────────┐
│   Scikit-learn Pipeline   │
│  ┌─────────────────────┐  │
│  │ OneHotEncoder        │  │  ← Categorical: Airline, Source, Destination, Class
│  ├─────────────────────┤  │
│  │ Passthrough          │  │  ← Numerical: Days Left, Stops, Duration
│  └─────────────────────┘  │
└───────────┬───────────────┘
            │
            ▼
   Random Forest Regressor
            │
            ▼
     Predicted Fare (₹)
```

### Model Performance

| Metric | Value |
|---|---|
| R² Score | **0.97** |
| Training Records | **300,000+** |
| Encoding | OneHotEncoding |
| Serialization | Joblib (`.pkl`) |

---

## 🏗️ Project Architecture

```
airfare_price_prediction/
│
├── flight_app.py          # 🖥  Streamlit web application (UI + prediction logic)
├── flight_model.pkl       # 🤖  Serialized trained ML pipeline
├── train_model.py         # 🏋  Model training & evaluation script
├── requirements.txt       # 📦  Project dependencies
└── README.md              # 📄  Project documentation
```

---

## ⚙️ How It Works

```
Step 1 — User Input
  └─ Selects airline, source, destination, class, stops, and journey date

Step 2 — Feature Engineering
  ├─ Calculates days left until departure
  ├─ Maps departure time → time category (Morning / Afternoon / Evening / Night)
  └─ Estimates flight duration based on route

Step 3 — Model Inference
  └─ Pre-trained Random Forest pipeline generates fare prediction

Step 4 — Results Display
  ├─ 💰 Estimated ticket price
  ├─ ⏱  Estimated flight duration
  ├─ 🎯 Fare category (Budget / Standard / Expensive)
  └─ 📈 Booking recommendation
```

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Language | Python 3.9+ |
| ML Framework | Scikit-learn |
| Data Processing | Pandas, NumPy |
| Web Framework | Streamlit |
| Model Serialization | Joblib |
| Deployment | Streamlit Cloud |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/airfare_price_prediction.git
cd airfare_price_prediction
```

**2. (Optional) Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the application**
```bash
streamlit run flight_app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 🌍 Deployment

This project is deployed on **Streamlit Cloud** for live public access.

To deploy your own instance:

1. Push the repository to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to `flight_app.py`
5. Click **Deploy**

> ⚡ No server management required — Streamlit Cloud handles everything.

---

## 🗺 Roadmap

- [ ] 📈 Price trend visualization over time
- [ ] 🏆 Multi-airline side-by-side comparison
- [ ] 📊 Feature importance visualization (SHAP values)
- [ ] 🎨 Enhanced UI with custom theming
- [ ] 🔍 Model explainability dashboard

---

## 👩‍💻 Author

**Bhavya Sri Pasileti**

> B.Tech | Data Science & AI Enthusiast
> Passionate about building intelligent ML systems and deploying real-world applications.

[LinkedIn](https://www.linkedin.com/in/bhavya-sri-pasileti-16565a2a1)

---

**If this project helped you or you found it interesting, please consider giving it a ⭐ — it means a lot!**
