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

        if selected_option is not None and user_input is not None:
            filtered_df = df[df[selected_option].str.contains(user_input, case=False)]
            filtered_df = pd.DataFrame(filtered_df,columns=["FormOID", "PreText", "VariableOID", "DataFormat","IsLog","IsVisible"])
            st.dataframe(filtered_df, width=800)

    # Form Search:
    df_frm = pd.read_excel(io.BytesIO(bytes_data), sheet_name='Forms', engine='openpyxl')
    if df_frm is not None:
        # Header:
        st.sidebar.title("Form Search")
        df_frm = df_frm[df_frm['DraftFormActive'] == True]
        option_list_frm = ['OID', 'DraftFormName', 'LogDirection', 'IsSignatureRequired']
        selected_option_frm = st.sidebar.selectbox("Form Search", option_list_frm)
        user_input_frm = st.sidebar.text_input("Please enter a form key word")

        if selected_option_frm is not None and user_input_frm is not None:
            filtered_df_frm = df_frm[df_frm[selected_option_frm].str.contains(user_input_frm, case=False)]
            filtered_df_frm = pd.DataFrame(filtered_df_frm,columns=["OID", "DraftFormName", "IsSignatureRequired", "LogDirection"])
            st.dataframe(filtered_df, width=800)

st.markdown("""---""")
