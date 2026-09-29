import re
import joblib
import streamlit as st
from pathlib import Path

from utils.text_analyzer import extract_urls, heuristic_warnings
from utils.url_analyzer import analyze_url

BASE_DIR = Path(__file__).resolve().parent
MODEL_FILE = BASE_DIR / "model" / "scam_model.pkl"

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="centered"
)

@st.cache_resource
def load_model():
    return joblib.load(MODEL_FILE)

st.title("🛡️ ScamShield AI")
st.write("AI-assisted screening of potentially suspicious messages and links.")

if not MODEL_FILE.exists():
    st.error("Model not found. Run: python model/train_model.py")
    st.stop()

model = load_model()

message = st.text_area(
    "Paste a message to analyze:",
    height=180,
    placeholder="Example: Your account will be blocked. Verify your KYC immediately..."
)

if st.button("🔍 Analyze Message", type="primary"):
    if not message.strip():
        st.warning("Please enter a message.")
        st.stop()

    prediction = model.predict([message])[0]
    probabilities = model.predict_proba([message])[0]
    confidence = max(probabilities) * 100

    urls = extract_urls(message)
    warnings = heuristic_warnings(message)

    st.subheader("Result")

    if prediction == "scam":
        st.error("🚨 POTENTIALLY SUSPICIOUS")
    else:
        st.success("✅ LIKELY LEGITIMATE")

    st.write(f"**Model confidence:** {confidence:.2f}%")
    st.caption("This is a model confidence score, not proof that a message is fraudulent.")

    if warnings:
        st.subheader("⚠️ Warning Indicators")
        for warning in warnings:
            st.write("• " + warning)

    if urls:
        st.subheader("🌐 URL Analysis")
        for url in urls:
            st.code(url)
            url_warnings = analyze_url(url)
            if url_warnings:
                for warning in url_warnings:
                    st.warning(warning)
            else:
                st.info("No basic URL-format warning detected. This does not prove the site is safe.")

    st.subheader("🛡️ Safety Guidance")
    st.write("""
    - Do not share OTPs, PINs, passwords, or banking credentials.
    - Do not send money because a message creates urgency or fear.
    - Verify unexpected requests using the organization's official app or website.
    - Do not assume that a model result is proof of fraud.
    """)

st.divider()
st.subheader("🇮🇳 Official Resources")
st.markdown("[Sanchar Saathi](https://sancharsaathi.gov.in/)")
st.markdown("[National Cyber Crime Reporting Portal](https://www.cybercrime.gov.in/)")
st.markdown("[CERT-In](https://www.cert-in.org.in/)")

st.caption(
    "ScamShield AI is an independent screening tool. It is not an official government fraud-detection service."
)
