import requests
import streamlit as st
import base64

# Define API details
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def get_img_as_base64(file):
    with open(file,"rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()
img = get_img_as_base64("bg.jpg")

page_bg_img = f"""

<style>
[data-testid="stAppViewContainer"] > .main {{
background-image :url("data:image/png;base64,{img}");
background-size : cover;
}}
[data-testid="stHeader"]{{
background:rgba(0,0,0,0);
}}
</style>

"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Function to query the API with the image
def query(image_bytes):
    response = requests.post(API_URL, headers=headers, data=image_bytes)
    return response.json()

# Streamlit UI
st.title("Image Captioning")
inside = st.file_uploader('Upload your image: ', type='jpg')

if inside is not None:
    if st.button('Generate'):
    # Convert the uploaded file to bytes and send it to the API
       file_bytes = inside.read()
       output = query(file_bytes)
    
    # Display the output caption
       st.write( output[0].get("generated_text", "No caption generated"))
