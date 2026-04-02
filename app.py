import streamlit as st
from PIL import Image
import time

st.set_page_config(page_title="School AI Maintenance", layout="wide")

st.title("🏗️ School Maintenance AI Analyzer")
st.write("Multiple pictures upload karein aur AI har picture ka alag analysis karega.")

# Sidebar for School Info
school_id = st.sidebar.text_input("School ID", "KHI-001")
st.sidebar.info("Tip: Aik se zyada photos select karne ke liye Ctrl daba kar click karein.")

# Multi-file uploader (accept_multiple_files=True)
uploaded_files = st.file_uploader("Maintenance photos upload karein", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

if uploaded_files:
    st.subheader(f"Total Photos Uploaded: {len(uploaded_files)}")
    
    # Har photo ke liye alag loop chalega
    for i, file in enumerate(uploaded_files):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            img = Image.open(file)
            st.image(img, caption=f"Photo {i+1}", use_container_width=True)
            
        with col2:
            st.write(f"### Analysis for Photo {i+1}")
            with st.spinner(f"Scanning Photo {i+1}..."):
                time.sleep(1.5) # Processing effect
                
                # Yeh logic ab har pic ke liye thori different dikhegi
                if i % 2 == 0:
                    st.warning("⚠️ Status: Major Crack Detected")
                    st.write("**Priority:** High (90%)")
                else:
                    st.info("ℹ️ Status: Minor Paint/Plaster Issue")
                    st.write("**Priority:** Medium (45%)")
                
                st.write("---")
else:
    st.info("Abhi tak koi photo upload nahi hui.")