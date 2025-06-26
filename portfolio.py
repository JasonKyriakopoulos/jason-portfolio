import streamlit as st

st.set_page_config(page_title="Jay's Data Science Portfolio", layout="wide")

st.title("Welcome to Jay's Portfolio 👋")
st.write("""
This is where I show off my data science projects.  
(More projects coming soon, stay tuned!)
""")

st.subheader("🚀 Projects")

st.markdown("### 🔌 EV Forecasting App (Coming Soon)")
st.markdown("Time-series forecasting for electric vehicle charging stations. Built with XGBoost, LSTM, and Transformers.")

st.markdown("### 💰 Bitcoin Price Predictor (Coming Soon)")
st.markdown("Pulls real-time Bitcoin data and predicts future prices with machine learning.")

st.markdown("### 🧠 Background-Foreground Classifier")
st.markdown("An image classification model that detects foreground objects. Built with Keras and CNNs.")
