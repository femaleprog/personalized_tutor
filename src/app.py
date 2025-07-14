import streamlit as st

st.title("Your personalized tutor")

st.header("Welcome to your Learning Assistant")
st.write("Ask me anything related to your course materials, and I'll explain concepts and quiz you!")

user_input = st.text_input("Ask me any question about your course :)")

if user_input:

    st.write("Retrieving relevant information and explanation...")

    reponse = ""

    st.subheader("Quiz time !")

    