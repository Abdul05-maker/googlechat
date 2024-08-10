import streamlit as st
import google.generativeai as genai
from PyPDF2 import PdfReader
import io

# Configure Google Generative AI API
GOOGLE_API_KEY = "AIzaSyCWNDbhBTB6p6WxD1Bqvvz93Dxj8EoVJj8"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def getResponseFromModel(user_input, pdf_text):
    # Combine user input with extracted PDF text for more context
    combined_input = f"Based on the PDF content:\n{pdf_text}\n\nQuestion: {user_input}"
    response = model.generate_content(combined_input)
    return response.text

# Streamlit UI
st.title("Simple Chatbot")
st.write("This chatbot uses the Gemini API key from Google Generative AI.")

# PDF Upload
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

pdf_text = ""
if uploaded_file is not None:
    pdf_reader = PdfReader(io.BytesIO(uploaded_file.read()))
    pdf_text = ""
    for page in pdf_reader.pages:
        pdf_text += page.extract_text() or ""  # Handle case where extract_text() might return None
    st.write("PDF content extracted. You can now ask questions based on this content.")

# Get user input
user_input = st.text_input("Enter Your Prompt:")

# Generate and display output when the user provides input
if user_input:
    if pdf_text:
        output = getResponseFromModel(user_input, pdf_text)
        st.write("Response:")
        st.write(output)
    else:
        st.write("Please upload a PDF first.")











    