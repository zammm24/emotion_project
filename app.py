import streamlit as st
from model import predict_emotion

st.set_page_config(page_title="Emotion Detector", page_icon="🧠")

st.title("🧠 Emotion Detection from Text")
st.write("Enter a sentence and detect emotion")

user_input = st.text_input("Type something:")

if st.button("Detect Emotion"):
    if user_input:
        result = predict_emotion(user_input)
        st.success(f"Detected Emotion: {result}")
    else:
        st.warning("Please enter text")