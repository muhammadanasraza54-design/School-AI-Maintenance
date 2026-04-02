import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup Gemini AI
# Streamlit secrets se key uthane ka sahi tareeqa
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="School AI Maintenance", layout="wide")
st.title("🏗️ School Maintenance Real-AI Analyzer")

uploaded_files = st.file_uploader("School photos upload karein", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        img = Image.open(file)
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.image(img, caption="Uploaded Photo", use_container_width=True)
        
        with col2:
            with st.spinner("Gemini AI analysis kar raha hai..."):
                try:
                    # AI ko instruction
                    prompt = "Identify if there are any cracks, broken windows, water leakage, or paint issues in this school building photo. Provide a summary in Roman Urdu."
                    response = model.generate_content([prompt, img])
                    
                    st.subheader("AI Analysis Report:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Error: {e}")
        st.divider()
        
