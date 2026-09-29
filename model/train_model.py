import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "messages.csv"
MODEL_FILE = BASE_DIR / "model" / "scam_model.pkl"

df = pd.read_csv(DATA_FILE)
required = {"text", "label"}
if not required.issubset(df.columns):
    raise ValueError("Dataset must contain 'text' and 'label' columns.")

X = df["text"].astype(str)
y = df["label"].astype(str)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english")),
    ("classifier", LogisticRegression(max_iter=1000))
])

model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Model Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

joblib.dump(model, MODEL_FILE)
print(f"\nModel saved to: {MODEL_FILE}")
