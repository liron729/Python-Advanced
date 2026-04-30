import pandas as pd
import streamlit as st

st.header("displaying dataframes")

data = pd.DataFrame({
    'Name': ['egzoni', 'melina', 'lironi', 'sara', 'anid', 'reina'],
    'age': [17,17,18,18,16,15],
    'city': ['Fushe Kosove', 'prishtine', 'presheve', 'obiliq', 'prishtine', 'prishtine']

})
st.dataframe(data)
