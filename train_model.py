import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score

# Load dataset
df = pd.read_csv("clean_dataset.csv")
df = df.sample(50000, random_state=42)

# Drop unnecessary column
df = df.drop("flight", axis=1)

# Convert stops column
df["stops"] = df["stops"].replace({
    "zero": 0,
    "one": 1,
    "two_or_more": 2
})

# Features and target
X = df.drop("price", axis=1)
y = df["price"]

categorical_features = [
    "airline",
    "source_city",
    "destination_city",
    "departure_time",
    "arrival_time",
    "class"
]

numerical_features = [
    "stops",
    "duration",
    "days_left"
]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(
        n_estimators=20,
        max_depth=15,
        random_state=42,
    ))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print("R2 Score:", r2_score(y_test, y_pred))

# Save model
joblib.dump(model, "flight_model.pkl")
print("Model saved as flight_model.pkl")