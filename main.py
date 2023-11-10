import pandas as pd
import streamlit as st

# Create a function to upload the xlsx file
def upload_file(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        df = pd.read_excel(io.BytesIO(bytes_data), sheet_name='Fields', engine='openpyxl')
        return df

# Create a function to display the table
def display_table(df):
    st.table(df)

# Create a function to filter the table based on user selection
def filter_table(df):
    options = df.columns.tolist()
    selected_option = st.sidebar.selectbox("Filter by", options)
    filtered_df = df[df[selected_option].notna()]
    return filtered_df

# Create the main function to run the app
def main():
    st.title("XLSX File Uploader and Filter")

    #Uploader
    uploaded_file = st.file_uploader("Choose your files", accept_multiple_files=True, type=['xlsx'])
    df = upload_file(uploaded_file)

    # Display the table if a file is uploaded
    if df is not None:
        display_table(df)

        # Filter the table based on user selection
        filtered_df = filter_table(df)
        display_table(filtered_df)

if __name__ == "__main__":
    main()
