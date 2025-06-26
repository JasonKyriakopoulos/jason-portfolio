import streamlit as st
from PIL import Image

st.set_page_config(page_title="Jay | Data Science Portfolio", layout="wide")

# ---- HEADER ----
st.markdown("<h1 style='text-align: center;'>👨‍💻 Jay | Data Science Projects</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Welcome to my portfolio. This is a growing collection of my best data science work. All projects are end-to-end, with real data and deployed apps.</p>", unsafe_allow_html=True)
st.markdown("---")

# ---- PROJECT CARDS ----
def project_card(title, desc, status="Coming Soon 🚧", link=None):
    st.markdown(f"### {title}")
    st.markdown(desc)
    if link:
        st.markdown(f"[👉 Try it here]({link})")
    else:
        st.markdown(f"*Status: {status}*")
    st.markdown("—" * 30)

# ---- PROJECTS ----
st.subheader("🚀 Featured Projects")

col1, col2 = st.columns(2)

with col1:
    project_card(
        "🔌 EV Load Forecasting App",
        "Predict future electric vehicle charging demand using ARIMA, XGBoost, and Transformers. Includes time series preprocessing, evaluation across stations, and UI for input.",
    )

    project_card(
        "🧠 Background-Foreground Image Classifier",
        "CNN-based classifier that detects objects in noisy environments. Image dataset cleaning + model training with Keras + GradCAM visualizations."
    )

with col2:
    project_card(
        "💰 Bitcoin Price Predictor",
        "Fetches real-time BTC data using API, then predicts next-day price using time series models.",
    )

    project_card(
        "📊 Interactive Resume + Projects Dashboard",
        "This website! Built using Streamlit and deployed on Streamlit Cloud. All code and projects are versioned using Git and GitHub.",
        status="✅ Live",
        link="https://YOUR-USERNAME-streamlit-app-name.streamlit.app"  # replace with real link
    )

# ---- FOOTER ----
st.markdown("---")
st.markdown("📫 Contact: your.email@example.com  |  [GitHub](https://github.com/YOUR_USERNAME)")
