import streamlit as st

if st.button("click me"):
    st.write("button clicked")

if st.checkbox("check me to show some text"):
    st.write("Youre seeing this cuz u checked checkbox")

user_input = st.text_input("enter text", "sample text")
st.write("u entered:", user_input)

age = st.number_input("enter ur age kid 18+ only", min_value=0, max_value=100)
st.write(f"ur age is: {age}" )

message = st.text_area("Enter a message")
st.write(f"your message: {message}")

choice = st.radio("Pick one", ["choice 1", "choice 2", "choice 3"])
st.write(f"you chose: {choice}")

if st.button("Success"):
    st.success("operation was successful")

try:
    1/0
except Exception as e:
    st.exception(e)