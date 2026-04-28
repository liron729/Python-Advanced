import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("this is the sidebar")

st.sidebar.selectbox("choose an option", ["option 1", "option 2", "option 3"])

st.sidebar.radio("go to", ["home", "data", "settings"])

