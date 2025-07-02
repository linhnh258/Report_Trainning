import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

import joblib
import os

def train_and_save_model():
    # Path to save model 
    model_dir = os.path.join(os.path.dirname(__file__), "trained_models")
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "random_forest_iris.joblib")

    # Load dataset
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target)
    X.columns = [col.replace(' (cm)', '').replace(' ', '_') for col in X.columns]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy on test data: {accuracy}")

    # Save model 
    joblib.dump(model, model_path)
    print(f"Model saved at: {model_path}")

    # Save class name for future work 
    class_names_path = os.path.join(model_dir, "class_names.joblib")
    joblib.dump(list(iris.target_names), class_names_path)
    print(f"Name of class saved at: {class_names_path}")

if __name__ == "__main__":
    train_and_save_model()

