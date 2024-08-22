import requests
import streamlit as st
from PIL import Image

# Define the API URL and headers
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}

# Function to query the API with the uploaded image
def query(image):
    img_bytes = image.read()
    response = requests.post(API_URL, headers=headers, data=img_bytes)
    return response.json()

# Streamlit app
st.title("Image Captioning App")

# Image uploader widget
image = st.file_uploader("UPLOAD YOUR IMAGE HERE...", type=["png", "jpg", "jpeg"])

# Button to generate output
if st.button("Generate"):
    if image is not None:
        result = query(image)
        caption = result[0]['generated_text']  # Assuming the API returns a list of captions
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Caption:", caption)
    else:
        st.error("Please upload an image before generating!")
