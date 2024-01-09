## Invoice Extractor ##

from dotenv import load_dotenv

load_dotenv() ## load all the environment variables from .env

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

## configuring api key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


## function to loaad Gemini pro vision model and get response

def get_gemini_response(input,image,prompt):
    #loading the gemini model
    model=genai.GenerativeModel('gemini-pro-vision')
    response =model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    # check if a file has been uploaded
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

# initialize our streamlit app
    
st.set_page_config(page_title="Invoice Extractor")

st.header("Gemini Application")
input = st.text_input('Input Prompt: ', key='input')
uploaded_file = st.file_uploader('Choose an image...', type=['jpg','png','jpeg','pdf'])
image=''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)


submit=st.button("Tell Me About The Invoice")

input_prompt ="""
You are an expert in understanding invoices. 
You will receive input images as invoices and you will have to
answer questions based on the input image.
"""

# if submit button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt,image_data,input)

    st.subheader("The Response is")
    st.write(response)
