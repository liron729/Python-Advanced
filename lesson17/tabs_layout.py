import streamlit as st

tab1, tab2, tab3 = st.tabs(["tab 1", "tab 2", "tab 3"])

with tab1:
    st.header("content for tab 1")
    st.write("hello")

with tab2:
    st.header("content for tab 2")
    st.write("hello")

with tab3:
    st.header("content for tab 3")
    st.write("hello")