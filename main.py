import pandas as pd
import openpyxl
import streamlit as st
import io
import base64

# Create the main function to run the app

st.title("XLSX File Uploader and Filter")

#Uploader
uploaded_file = st.file_uploader("Choose your file", accept_multiple_files=False, type=['xlsx'])

if uploaded_file is not None:
    bytes_data = uploaded_file.read()
    df = pd.read_excel(io.BytesIO(bytes_data), sheet_name='Fields', engine='openpyxl')
    #return df
    #if df is not None:
        #st.dataframe(df)

#sidebar
if df is not None:
    options = df.columns.tolist()
    selected_option = st.sidebar.selectbox("Filter by", options)
else:
    selected_option = st.sidebar.selectbox("Filter by", "Default")

st.sidebar.title("Text Input")
user_input = st.sidebar.text_input("Enter text")

if selected_option != 'Default' and user_input is not None:
    filtered_df = df[df[selected_option] == user_input]
    filtered_df = pd.DataFrame(filtered_df,columns=["FormOID", "PreText", "VariableOID", "DataFormat","IsLog","IsVisible"])
    st.dataframe(filtered_df)


st.markdown("""---""")
