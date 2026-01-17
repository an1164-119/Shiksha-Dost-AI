import streamlit as st
from coach import get_advice

st.set_page_config(page_title="Shiksha-Dost Assistant")
st.title("Teacher Support Portal")
st.write("Enter your classroom challenge to get a quick coaching strategy.")

grade = st.selectbox("Grade Level", ["Primary", "Middle", "Secondary"])
problem = st.text_area("What is happening in your classroom?")

if st.button("Get Coaching Tip"):
    if problem:
        with st.spinner("Thinking..."):
            advice = get_advice(problem, grade)
            st.subheader("Your Action Plan")
            st.info(advice)