# ScamShield AI

An AI-assisted scam-message screening project built with Python, TF-IDF,
Logistic Regression, and Streamlit.

## Project structure

ScamShieldAI/
- app.py
- requirements.txt
- README.md
- data/messages.csv
- model/train_model.py
- model/scam_model.pkl (created after training)
- utils/text_analyzer.py
- utils/url_analyzer.py
- utils/__init__.py

## Installation

```bash
pip install -r requirements.txt
```

## Train the model

From the ScamShieldAI folder:

```bash
python model/train_model.py
```

This creates:

```text
model/scam_model.pkl
```

## Run the application

```bash
streamlit run app.py
```

## Important

The included dataset is a small synthetic starter dataset for development.
It is not an official government dataset and should not be treated as
authoritative fraud intelligence.

For a production system, use a larger, properly licensed and validated
dataset and verified threat-intelligence sources.
