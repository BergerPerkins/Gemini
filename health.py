import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image


load_dotenv() # loading all env variables
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input_prompt, image[0]])
    return response.text

def input_image_setup(uploaded_file):
    #check if file has been uploaded
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type":uploaded_file.type, # get the mime type of the uploaded file
                "data":bytes_data # get the bytes of the uploaded file
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")



#<<<<<<initialize the streamlit app Front end setup>>>>>>>>
st.set_page_config(page_title="Calories Adviser App", page_icon=":heart:", layout="wide")
st.header("Calories Adviser App")

#create a text input box
uploaded_file = st.file_uploader("Upload an image...", type=["png", "jpg", "jpeg"])
imaage=""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

submit = st.button("Tell Me About The Total Calories")


input_prompt ="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----

        Finally you can also mention weather the food is healthy or not and also
        mention the
        percentage split of the ratio of carbohydrates,fats,fibers,sugar and other important
        things required in our diet


"""

if submit:
    try:
        image_parts = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_parts)
        st.header("The response is ")
        st.write(response)
    except FileNotFoundError:
        st.write("Please upload an image")