import streamlit as st
import pandas as pd

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.write("Column 1")
    text_input_1 = st.text_input("Enter text for column 1")

with col2:
    st.write("Column 2")
    text_input_2 = st.text_input("Enter text for column 2")

with col3:
    st.write("Column 3")
    text_input_3 = st.text_input("Enter text for column 3")
