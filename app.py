import streamlit as st
import google.generativeai as genai
from PIL import Image

# App ka Title
st.set_page_config(page_title="Raju AI Scanner")
st.title("🍎 Raju's AI Calorie Scanner")

# Side menu mein API Key daalne ke liye
st.sidebar.header("Settings")
api_key = st.sidebar.text_input("Enter Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    
    # Camera input mobile ke liye
    img_file = st.camera_input("Take a photo of your food")

    if img_file:
        img = Image.open(img_file)
        st.image(img, caption='Scanning your meal...', use_container_width=True)
        
        # AI Model ko instruction dena
        model = genai.GenerativeModel('gemini-1.5-flash')
        with st.spinner('Analyzing...'):
            response = model.generate_content(["Identify this food and give total calories, protein, carbs, and fats in a simple list.", img])
            st.subheader("Nutrition Info:")
            st.write(response.text)
else:
    st.info("👈 Side menu mein apni Gemini API Key daalein (Jo humne Google AI Studio se li thi).")
