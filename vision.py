# Streamlit Image content generation using gemini pro model

from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import pathlib
import textwrap
import google.generativeai as genai
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
    text = text.replace('•', '  *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# model_path = "gs://gemini

def get_gemini_response(question):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

st.set_page_config(
    page_title="Gemini LLM Application",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.title("Gemini LLM Application")
with st.expander("About"):
    st.write(
        "This app uses the Gemini Pro model to generate image content based on the input text."
    )
    # image_placeholder = st.empty()
    # image_placeholder.image(
    #     "https://storage.googleapis.com/gemini-assets/images/gemini-logo.png",
    #     use_column_width=True,
    # )

input = st.text_input("Input: ", key="input")
submit = st.button("Generate Image")