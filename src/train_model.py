import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


def train_model():

    print("Training ML model...")

    df = pd.read_csv("./data/processed/listings_cleaned.csv")

    features = ["accommodates", "bedrooms", "beds", "bathrooms", "number_of_reviews", "availability_365"]
    target = "price_clean"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, "./models/random_forest_model.pkl")

    print("Model trained and saved successfully!")