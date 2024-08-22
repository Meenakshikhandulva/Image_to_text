import streamlit as st
import base64
import requests

def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your background image using a raw string
img = get_img_as_base64(r"C:\Users\malat\OneDrive\Desktop\MEENA\guvi\bgim.jpg")

# Set the background image using CSS
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
}}
[data-testid="stHeader"] {{
    background: rgba(0, 0, 0, 0);
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

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