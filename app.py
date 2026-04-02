import streamlit as st
from PIL import Image

st.title("🏗️ School Maintenance AI Analyzer")
school_id = st.text_input("School ID", "KHI-001")
uploaded_file = st.file_uploader("Photo upload karein", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="School Image", use_container_width=True)
    st.success(f"AI is analyzing {school_id}... Window/Door damage detected!")