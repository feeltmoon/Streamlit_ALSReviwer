import pandas as pd
import openpyxl
import streamlit as st
import io
import base64

# Create the main function to run the app

st.title("XLSX File Uploader and Filter")

#Uploader
uploaded_file = st.file_uploader("Choose your file", accept_multiple_files=False, type=['xlsx'])

#sidebar
#option_list = ['Default']
#selected_option = st.sidebar.selectbox("Filter by", option_list)



if uploaded_file is not None:
    bytes_data = uploaded_file.read()

    try: 
        df = pd.read_excel(io.BytesIO(bytes_data), sheet_name='Fields', engine='openpyxl')
        #return df
        #if df is not None:
            #st.dataframe(df)
        if df is not None:
            # Header:
            st.sidebar.title("Field Search")
            df = df[df['DraftFieldActive'] == True]
            option_list = ['FieldOID', 'FormOID', 'VariableOID', 'DataDictionaryName', 'PreText']
            selected_option = st.sidebar.selectbox("Fields Search", option_list)
            user_input = st.sidebar.text_input("Please enter a field key word")

            if selected_option is not None and user_input != '':
                filtered_df = df[df[selected_option].str.contains(user_input, case=False, na=False)]
                filtered_df = pd.DataFrame(filtered_df,columns=["FormOID", "PreText", "FieldOID", "VariableOID", "DataFormat","DataDictionaryName", "IsLog", "IsVisible"])
                st.markdown(''':blue[Fields] :balloon:''')
                st.dataframe(filtered_df)
                st.markdown("""---""")
    except pd.errors.SheetNameError:
        st.write("Worksheet named 'Fields' not found")
