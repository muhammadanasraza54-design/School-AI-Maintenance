import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="School AI Maintenance", layout="wide")

st.title("🏗️ School Maintenance AI Analyzer")
st.write("Engineers can upload site photos for automated damage detection.")

col1, col2 = st.columns(2)

with col1:
    school_id = st.text_input("School ID / Name", "KHI-001")
    uploaded_file = st.file_uploader("Maintenance photo upload karein", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption="Original Photo", use_container_width=True)
    
    with col2:
        st.subheader("AI Analysis Report")
        with st.spinner("AI Model scanning for damages..."):
            time.sleep(2) # Fake processing time
            
            # Yahan hum future mein real AI model lagayenge
            st.warning("⚠️ Damage Detected: Cracked Wall / Broken Window")
            st.write(f"**School ID:** {school_id}")
            st.write("**Maintenance Priority:** 85% (High)")
            st.progress(85)
            
            st.success("Recommendation: Requires immediate repair within 7 days.")