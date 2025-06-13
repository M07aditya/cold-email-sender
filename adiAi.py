# app.py
import streamlit as st
from gemini_helper import my_google_llm

st.set_page_config(page_title="Ask Gemini", page_icon="🤖")

st.title("🤖 Ask Gemini - AI Question Answering")
st.markdown("Type your question below and Gemini will answer it!")

# Text input
question = st.text_input("Your Question:", "")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Gemini is thinking..."):
            answer = my_google_llm(question)
        st.success("Answer:")
        st.write(answer)
