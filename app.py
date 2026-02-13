import streamlit as st
import pickle
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie

# ------------------------------------------------------------------------------------------------
# 1. SETUP & CONFIGURATION
# ------------------------------------------------------------------------------------------------
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")

# Lottie Animation Load karne ka function
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# CSS for "Sexy" Look (Gradient Background & Hover Effects)
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: white;
    }
    
    /* Input Fields Styling */
    .stSelectbox, .stNumberInput {
        background-color: transparent;
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(45deg, #ff00cc, #333399);
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
        width: 100%;
        font-weight: bold;
    }
    
    /* Button Hover Effect */
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #333399, #ff00cc);
        box-shadow: 0 0 15px #ff00cc;
    }
    
    /* Headings */
    h1, h2, h3 {
        color: #00d2ff;
        font-family: 'Helvetica', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------------------
# 2. LOAD DATA
# ------------------------------------------------------------------------------------------------
try:
    pipe = pickle.load(open('model.pkl', 'rb'))
    df = pickle.load(open('df.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: model.pkl ya df.pkl nahi mili! Pehle model train karo.")
    st.stop()

# ------------------------------------------------------------------------------------------------
# 3. UI LAYOUT
# ------------------------------------------------------------------------------------------------

# Header Section with Animation
col1, col2 = st.columns([2, 1])

with col1:
    st.title("💻 Laptop Price Predictor")
    st.markdown("### Find the *perfect price* for your dream machine using **Machine Learning**.")
    st.markdown("---")

with col2:
    # Ye URL se animation load hoga (Coding boy animation)
    lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
    st_lottie(lottie_coding, height=200, key="coding")

# Input Section (Card Style)
st.subheader("⚙️ Configuration")

# Column Layout for Inputs (2 columns dikhenge)
c1, c2 = st.columns(2)

with c1:
    company = st.selectbox('Brand', df['brand'].unique())
    ram = st.selectbox('RAM (GB)', [2, 4, 8, 12, 16, 24, 32, 64])
    hdd = st.selectbox('Storage (GB)', [128, 256, 512, 1000, 2000])

with c2:
    screen_size = st.number_input('Screen Size (Inches)', 10.0, 30.0, 15.6)
    # OS ke naam clean dikhane ke liye thoda safai
    os = st.selectbox('Operating System', df['OS'].unique())

st.markdown("<br>", unsafe_allow_html=True) # Thoda space

# ------------------------------------------------------------------------------------------------
# 4. PREDICTION LOGIC
# ------------------------------------------------------------------------------------------------
if st.button('🚀 Predict Price'):
    # Progress Bar (Thoda drama add karne ke liye)
    import time
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
        
    # Query creation
    query = pd.DataFrame([[company, ram, hdd, screen_size, os]], 
                        columns=['brand', 'Ram', 'ROM', 'display_size', 'OS'])
    
    # Prediction
    prediction = pipe.predict(query)
    price = int(np.exp(prediction[0])) if prediction[0] < 15 else int(prediction[0]) 
    # Note: Agar training me np.log use kiya tha to np.exp lagana, nahi to simple rakho
    # Main assume kar raha hu simple Linear Regression hai
    
    st.balloons() # Confetti udayega! 🎉
    
    # Result ko bade font me dikhana
    st.markdown(f"""
    <div style="background-color: #0f2027; padding: 20px; border-radius: 10px; border: 2px solid #00d2ff; text-align: center;">
        <h2 style="color: white; margin:0;">Estimated Price:</h2>
        <h1 style="color: #00d2ff; font-size: 50px; margin:0;">₹ {price:,}</h1>
        <p style="color: gray;">*Based on current market trends</p>
    </div>
    """, unsafe_allow_html=True)
