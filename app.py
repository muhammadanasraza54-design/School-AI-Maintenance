import streamlit as st
import google.generativeai as genai
from PIL import Image

# Setup Gemini AI
# Yahan apni API Key dalein
genai.configure(api_key="AAPKI_API_KEY_YAHAN_LIKHEIN")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🏗️ School Maintenance Real-AI Analyzer")

uploaded_files = st.file_uploader("Photos upload karein", type=["jpg", "png"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        img = Image.open(file)
        st.image(img, width=300)
        
        with st.spinner("Gemini AI is analyzing this image..."):
            # AI ko instruction dena (Prompting)
            prompt = "Is school ki building ki photo ko analyze karein aur batayen ke kya koi toot-phoot (damage), cracks, ya paint ki zaroorat hai? Roman Urdu mein short report dein."
            
            response = model.generate_content([prompt, img])
            
            st.subheader("AI Report:")
            st.write(response.text)
            st.write("---")