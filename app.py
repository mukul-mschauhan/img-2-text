from PIL import Image
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import textwrap
import google.generativeai as genai

# Setup the API
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

def get_response(input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input!="":
        response = model.generate_content([input, image])
        return(response.text)
    else:
        response = model.generate_content(image)
    return(response.text)

# Create the Streamlit Page
st.header("🖼️Image to :blue[Text] ✅▶️✨🎯")
input  = st.text_input("Input Prompt: ✍🏻")
uploaded_file = st.file_uploader("Upload an Image", 
                                 type = ["jpg", "jpeg", "png"])
# Display the Image
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image",
             use_container_width=True)

submit = st.button("Do the Magic🚀")

if submit:
    response = get_response(input, image)
    st.subheader("The Response is: ")
    st.write(response)