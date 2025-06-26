import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(
    page_title="Jay | ML Portfolio", 
    page_icon="🧠", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for animations and styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Inject custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(to bottom right, #111827, #1F2937);
        color: #F3F4F6;
    }
    
    h1, h2, h3 {
        background: linear-gradient(to right, #60A5FA, #8B5CF6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .project-card {
        background: rgba(31, 41, 55, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .project-card:hover {
        border-color: #60A5FA;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    }
    
    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.5rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
    }
    
    .coming-soon {
        background-color: rgba(251, 191, 36, 0.2);
        color: #FBBF24;
    }
    
    .live {
        background-color: rgba(52, 211, 153, 0.2);
        color: #34D399;
    }
    
    .divider {
        height: 1px;
        background: linear-gradient(to right, transparent, #4B5563, transparent);
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div style="text-align: center; padding: 5rem 0 3rem;">
    <h1 style="font-size: 3.5rem; margin-bottom: 1rem;">Jay's Machine Learning Portfolio</h1>
    <p style="font-size: 1.25rem; color: #9CA3AF; max-width: 700px; margin: 0 auto;">
        Innovative solutions powered by cutting-edge AI and data science
    </p>
</div>
""", unsafe_allow_html=True)

# ---- PROJECTS ----
st.markdown("""
<div class="divider"></div>
<h2 style="font-size: 2rem; margin-bottom: 2rem;">🚀 Featured Projects</h2>
""", unsafe_allow_html=True)

# Project card function with new styling
def project_card(title, desc, status="Coming Soon 🚧", link=None):
    status_class = "coming-soon" if "Coming" in status else "live"
    
    card = f"""
    <div class="project-card">
        <h3>{title}</h3>
        <p style="color: #D1D5DB; margin: 0.75rem 0 1.25rem;">{desc}</p>
        <div style="display: flex; justify-content: space-between; align-items: center;">
            <span class="status-badge {status_class}">{status}</span>
            {f'<a href="{link}" target="_blank" style="color: #60A5FA; text-decoration: none; font-weight: 500;">👉 Try it here</a>' if link else ''}
        </div>
    </div>
    """
    st.markdown(card, unsafe_allow_html=True)

# Projects in columns
col1, col2 = st.columns(2)

with col1:
    project_card(
        "🔌 EV Load Forecasting",
        "Predict future electric vehicle charging demand using ARIMA, XGBoost, and Transformers. Includes time series preprocessing and evaluation.",
    )

    project_card(
        "🧠 Image Classifier",
        "CNN-based classifier that detects objects in noisy environments with GradCAM visualizations.",
    )

with col2:
    project_card(
        "💰 Bitcoin Price Predictor",
        "Fetches real-time BTC data using API, predicts next-day price using time series models.",
    )

    project_card(
        "📊 Interactive Portfolio",
        "This website! Built using Streamlit with custom animations and styling.",
        status="✅ Live",
        link="https://your-portfolio.streamlit.app"
    )

# ---- FOOTER ----
st.markdown("""
<div class="divider"></div>
<div style="text-align: center; padding: 2rem 0; color: #9CA3AF;">
    <p>📫 Contact: <a href="mailto:your.email@example.com" style="color: #60A5FA; text-decoration: none;">your.email@example.com</a> | 
    <a href="https://github.com/yourusername" target="_blank" style="color: #60A5FA; text-decoration: none;">GitHub</a> | 
    <a href="https://linkedin.com/in/yourprofile" target="_blank" style="color: #60A5FA; text-decoration: none;">LinkedIn</a></p>
    <p>© 2023 Jay's ML Portfolio. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)