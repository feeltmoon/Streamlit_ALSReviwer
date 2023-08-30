import streamlit as st
import pandas as pd

def to_empty():
    chkacn_var.delete(0,tk.END)
    chkacn_formOID.delete(0,tk.END)
    chkacn_folderOID.delete(0,tk.END)
    chkacn_recPos.delete(0,tk.END)
    chkacn_frmRpt.delete(0,tk.END)
    chkacn_fldRpt.delete(0,tk.END)

def to_empty_qua():
    qua_var.delete(0,tk.END)
    qua_formOID.delete(0,tk.END)
    qua_folderOID.delete(0,tk.END)
    qua_recPos.delete(0,tk.END)
    qua_frmRpt.delete(0,tk.END)
    qua_fldRpt.delete(0,tk.END)

def copy_data():
    if b.get() == True:
        to_empty()
        #print("b true")
        
        chkacn_var.insert(0, var.get())
        chkacn_formOID.insert(0,formOID.get())
        chkacn_folderOID.insert(0,folderOID.get())
        chkacn_recPos.insert(0,recPos.get())
        chkacn_frmRpt.insert(0,frmRpt.get())
        chkacn_fldRpt.insert(0,fldRpt.get())
    else:
        to_empty()
        
    if b1.get() == True:
        to_empty()
        #print("b1 true")
        
        chkacn_var.insert(0, var1.get())
        chkacn_formOID.insert(0,formOID1.get())
        chkacn_folderOID.insert(0,folderOID1.get())
        chkacn_recPos.insert(0,recPos1.get())
        chkacn_frmRpt.insert(0,frmRpt1.get())
        chkacn_fldRpt.insert(0,fldRpt1.get())
        
    if b2.get() == True:
        to_empty()
        #print("b2 true")
        
        chkacn_var.insert(0, var2.get())
        chkacn_formOID.insert(0,formOID2.get())
    
# Initialize Streamlit app
st.set_page_config(page_title="My Streamlit App")

# Define widgets
var = st.text_input("Variable", value="")
formOID = st.text_input("formOID", value="")
folderOID = st.text_input("folderOID", value="")
recPos = st.text_input("recPos", value="")
frmRpt = st.text_input("frmRpt", value="")
fldRpt = st.text_input("fldRpt", value="")

var1 = st.text_input("Variable 1", value="")
formOID1 = st.text_input("formOID 1", value="")
folderOID1 = st.text_input("folderOID 1", value="")
recPos1 = st.text_input("recPos 1", value="")
frmRpt1 = st.text_input("frmRpt 1", value="")
fldRpt1 = st.text_input("fldRpt 1", value="")

var2 = st.text_input("Variable 2", value="")
formOID2 = st.text_input("formOID 2", value="")
folderOID2 = st.text_input("folderOID 2", value="")
recPos2 = st.text_input("recPos 2", value="")
frmRpt2 = st.text_input("frmRpt 2", value="")
fldRpt2 = st.text_input("fldRpt 2", value="")

b = st.checkbox('Checkbox 1')
b1 = st.checkbox('Checkbox 2')
b2 = st.checkbox('Checkbox 3')

# Define actions
if st.button('Copy data'):
    copy_data()
