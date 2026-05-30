import os
import pickle
from pathlib import Path
from typing import Dict, Any
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import pandas as pd

MODEL_DIR = Path(__file__).resolve().parent / "../models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)


def load_intent_model():
    model_path = MODEL_DIR / "intent_clf.pkl"
    if model_path.exists():
        with open(model_path, "rb") as f:
            return pickle.load(f)
    return _create_default_model()


def _create_default_model():
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(max_features=2000)),
        ("clf", LogisticRegression(max_iter=1000)),
    ])
    return pipeline


def train_models(dataset_path: str) -> Dict[str, Any]:
    df = pd.read_csv(dataset_path)
    X = df.text.values
    y = df.intent.values
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Naive Bayes": MultinomialNB(),
        "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
    }
    vectorizer = TfidfVectorizer(max_features=3000)
    X_train = vectorizer.fit_transform(X)

    results = {}
    for name, model in models.items():
        model.fit(X_train, y)
        y_pred = model.predict(X_train)
        results[name] = {
            "accuracy": accuracy_score(y, y_pred),
            "precision": precision_score(y, y_pred, average="weighted", zero_division=0),
            "recall": recall_score(y, y_pred, average="weighted", zero_division=0),
            "f1_score": f1_score(y, y_pred, average="weighted", zero_division=0),
            "confusion_matrix": confusion_matrix(y, y_pred).tolist(),
        }
    default_pipeline = Pipeline([("tfidf", vectorizer), ("clf", LogisticRegression(max_iter=1000))])
    default_pipeline.fit(X, y)
    with open(MODEL_DIR / "intent_clf.pkl", "wb") as f:
        pickle.dump(default_pipeline, f)
    return results
