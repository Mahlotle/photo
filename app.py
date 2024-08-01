import streamlit as st
from PIL import Image
import google.generativeai as genai

# Directly set the Google API key
GOOGLE_API_KEY = "AIzaSyDHVrqrYy_zCgqH_ksuFLqLD3CHfMk9MKc"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to load OpenAI model and get responses
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, image])
    return response.text

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")

# Text input field for user prompt
input_text = st.text_input("Input Prompt: ", key="input")

# File uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Display the uploaded image
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)
else:
    image = None

# Submit button to trigger the response
submit = st.button("Tell me about the image")

# Handle the submit button click
if submit:
    if input_text or image:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please provide input text or upload an image.")
