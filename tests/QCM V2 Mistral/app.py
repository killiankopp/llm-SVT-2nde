import PyPDF2
from transformers import pipeline
import streamlit as st


def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in range(len(reader.pages)):
        text += reader.pages[page].extract_text()
    return text

def generate_quiz(text):
    model_name = "fbellame/mistral-pdf-to-quizz-7b"
    generator = pipeline("text-generation", model=model_name)

    # Example prompt for quiz generation
    prompt = f"Generate multiple-choice quiz questions from the following text: {text}"

    quiz = generator(prompt, max_length=200)
    return quiz[0]['generated_text']


st.title('PDF to Quiz Generator')

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    quiz = generate_quiz(text)
    st.write(quiz)