import streamlit as st
from exercises import exercises
from bug_whisperer import explain_bug
from hint_generator import generate_hint

st.set_page_config(page_title="AI Learning Tools", layout="wide")

st.title("AI Tools for Learning Python Programming")

tab1, tab2 = st.tabs(["Debug My Code", "Get Tiered Hints"])

# Bug Whisperer 
with tab1:
    st.header("AI Bug Whisperer")
    st.write("Paste your Python code. The AI will explain the error like a tutor.")

    code_input = st.text_area("Your Python code:", height=200)

    if st.button("Explain My Bug"):
        if code_input.strip() == "":
            st.warning("Please paste some code.")
        else:
            explanation = explain_bug(code_input)
            st.success("Explanation:")
            st.write(explanation)

# Hint Generator 
with tab2:
    st.header("💡 Tiered Hint Generator")
    st.write("Choose an exercise and select a hint level.")

    exercise_name = st.selectbox("Choose a Python exercise:", list(exercises.keys()))
    level = st.slider("Hint level (1 = nudge, 4 = full solution)", 1, 4)

    if st.button("Generate Hint"):
        hint = generate_hint(exercises[exercise_name], level)
        st.info(hint)
