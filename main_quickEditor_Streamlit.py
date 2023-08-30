import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter import ttk
import pandas as pd
import openpyxl


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
        chkacn_folderOID.insert(0,folderOID2.get())
        chkacn_recPos.insert(0,recPos2.get())
        chkacn_frmRpt.insert(0,frmRpt2.get())
        chkacn_fldRpt.insert(0,fldRpt2.get())
    
    if b3.get() == True:
        to_empty()
        #print("b3 true")
        
        chkacn_var.insert(0, var3.get())
        chkacn_formOID.insert(0,formOID3.get())
        chkacn_folderOID.insert(0,folderOID3.get())
        chkacn_recPos.insert(0,recPos3.get())
        chkacn_frmRpt.insert(0,frmRpt3.get())
        chkacn_fldRpt.insert(0,fldRpt3.get())
        
    if b4.get() == True:
        to_empty()
        
        #print("b4 true")
        
        chkacn_var.insert(0, var4.get())
        chkacn_formOID.insert(0,formOID4.get())
        chkacn_folderOID.insert(0,folderOID4.get())
        chkacn_recPos.insert(0,recPos4.get())
        chkacn_frmRpt.insert(0,frmRpt4.get())
        chkacn_fldRpt.insert(0,fldRpt4.get())
        
    if b5.get() == True:
        to_empty()
        #print("b5 true")
        
        chkacn_var.insert(0, var5.get())
        chkacn_formOID.insert(0,formOID5.get())
        chkacn_folderOID.insert(0,folderOID5.get())
        chkacn_recPos.insert(0,recPos5.get())
        chkacn_frmRpt.insert(0,frmRpt5.get())
        chkacn_fldRpt.insert(0,fldRpt5.get())
        
def copy_data_qua():
    if qua.get() == True:
        to_empty_qua()
        #print("b true")
        
        qua_var.insert(0, var.get())
        qua_formOID.insert(0,formOID.get())
        qua_folderOID.insert(0,folderOID.get())
        qua_recPos.insert(0,recPos.get())
        qua_frmRpt.insert(0,frmRpt.get())
        qua_fldRpt.insert(0,fldRpt.get())
    else:
        to_empty_qua()
        
    if qua1.get() == True:
        to_empty_qua()
        #print("b1 true")
        
        qua_var.insert(0, var1.get())
        qua_formOID.insert(0,formOID1.get())
        qua_folderOID.insert(0,folderOID1.get())
        qua_recPos.insert(0,recPos1.get())
        qua_frmRpt.insert(0,frmRpt1.get())
        qua_fldRpt.insert(0,fldRpt1.get())
        
    if qua2.get() == True:
        to_empty_qua()
        #print("b2 true")
        
        qua_var.insert(0, var2.get())
        qua_formOID.insert(0,formOID2.get())
        qua_folderOID.insert(0,folderOID2.get())
        qua_recPos.insert(0,recPos2.get())
        qua_frmRpt.insert(0,frmRpt2.get())
        qua_fldRpt.insert(0,fldRpt2.get())
    
    if qua3.get() == True:
        to_empty_qua()
        #print("b3 true")
        
        qua_var.insert(0, var3.get())
        qua_formOID.insert(0,formOID3.get())
        qua_folderOID.insert(0,folderOID3.get())
        qua_recPos.insert(0,recPos3.get())
        qua_frmRpt.insert(0,frmRpt3.get())
        qua_fldRpt.insert(0,fldRpt3.get())
        
    if qua4.get() == True:
        to_empty_qua()
        
        #print("b4 true")
        
        qua_var.insert(0, var4.get())
        qua_formOID.insert(0,formOID4.get())
        qua_folderOID.insert(0,folderOID4.get())
        qua_recPos.insert(0,recPos4.get())
        qua_frmRpt.insert(0,frmRpt4.get())
        qua_fldRpt.insert(0,fldRpt4.get())
        
    if qua5.get() == True:
        to_empty_qua()
        #print("b5 true")
        
        qua_var.insert(0, var5.get())
        qua_formOID.insert(0,formOID5.get())
        qua_folderOID.insert(0,folderOID5.get())
        qua_recPos.insert(0,recPos5.get())
        qua_frmRpt.insert(0,frmRpt5.get())
        qua_fldRpt.insert(0,fldRpt5.get())

def generate_code():
    #structure method:
    def const_header():
        if chkID_entry.get() != "" and CF_entry.get() != "":
            #const: =CONCATENATE("|",K3,"|","True","|","True")
            return "|" + chkID_entry.get() + "|" + "True" + "|" + "True"
    def const_body():
    
        varOIDs = [var,var1,var2,var3,var4,var5]
        folderOIDs = [folderOID,folderOID1,folderOID2,folderOID3,folderOID4,folderOID5]
        formOIDs = [formOID,formOID1,formOID2,formOID3,formOID3,formOID4,formOID5]
        recPoss = [recPos,recPos1,recPos2,recPos3,recPos4,recPos5]
        frmRpts = [frmRpt,frmRpt1,frmRpt2,frmRpt3,frmRpt4,frmRpt5]
        fldRpts = [fldRpt,fldRpt1,fldRpt2,fldRpt3,fldRpt4,fldRpt5]                
             
        var_cnt = 0
        for item in varOIDs:
            if item.get() != "":
                var_cnt = var_cnt + 1
        
        print(var_cnt)
        
        body_concat = ""
        if var_cnt == 1:
            for i,item in enumerate(varOIDs):
                if item.get() != "":
                    #const: =("||",IF(A3="CheckBox","StandardValue",A3),"|",B3,"|",C3,"|",D3,"|",B3,"|",E3,"||||",IF(F3 <> "","|0","|"),IF(G3 <> "","|0","|"),CHAR(10),$L$3,CHAR(10))
                    body_concat = "||" + "DataPoint" + "|" + varOIDs[i].get() + "|" + folderOIDs[i].get() + "|" + formOIDs[i].get() + "|" + varOIDs[i].get() + "|" + recPoss[i].get() + "|||||" + frmRpts[i].get() + "|" + fldRpts[i].get() + "\n" + "IsPresent|||||||||||||"
            return body_concat
        elif var_cnt > 1:
            for i,item in enumerate(varOIDs):
                if item.get() != "":
                    #const: =("||",IF(A3="CheckBox","StandardValue",A3),"|",B3,"|",C3,"|",D3,"|",B3,"|",E3,"||||",IF(F3 <> "","|0","|"),IF(G3 <> "","|0","|"),CHAR(10),$L$3,CHAR(10))
                    body_concat = body_concat + "||" + "DataPoint" + "|" + varOIDs[i].get() + "|" + folderOIDs[i].get() + "|" + formOIDs[i].get() + "|" + varOIDs[i].get() + "|" + recPoss[i].get() + "|||||" + frmRpts[i].get() + "|" + fldRpts[i].get() + "\n" + "IsPresent|||||||||||||" + "\n"
            
            sents = body_concat.rsplit('\n', 1)
            body_concat = '\n'.join(sents[:-1]) + sents[-1]          
            return body_concat
    
    def const_or():
        
        varOIDs = [var,var1,var2,var3,var4,var5]
        var_cnt = 0
        for item in varOIDs:
            if item.get() != "":
                var_cnt = var_cnt + 1
                
        or_concat = ""
        if var_cnt == 1:
            or_concat = "Or|||||||||||||"
        elif var_cnt > 1:
            for i in range(var_cnt-1):
                or_concat = or_concat + "Or|||||||||||||" + "\n"
        return or_concat
    
    def const_qua():
        qua_concat = ""
        if check_qua != "":
            #CONCATENATE(C9,"|",D9,"|",B9,"|",B9,"|",E9,"|",F9,"|",G9,"||||","IsPresent","||",0,"|",CHAR(10))
            qua_concat = qua_folderOID.get() + "|" + qua_formOID.get() + "|" + qua_var.get() + "|" + qua_recPos.get() + "|" + qua_frmRpt.get() + "|" + qua_fldRpt.get() + "||||" + "IsPresent" + "||" + "0" + "|"
        else:
            qua_concat = ""
        return qua_concat
    
    def const_acn():
        acn_concat = ""
        if qua_var != "":
            #CONCATENATE(C3,"|",D3,"|",B3,"|",B3,"|",E3,"|",F3,"|",G3,"||||","CustomFunction","||",J3,"|")
            acn_concat = chkacn_folderOID.get() + "|" + chkacn_formOID.get() + "|" + chkacn_var.get() + "|" + chkacn_var.get() + "|" + chkacn_recPos.get() + "|" + chkacn_frmRpt.get() + "|" + chkacn_fldRpt.get() + "||||" + "CustomFunction" + "||" + CF_entry.get() + "|"
        else:
            acn_concat = ""
        return acn_concat
    
    def copy_code():
        # get text from scrollText widget
        text = text_box.get("1.0", "end-1c")
        # copy text to clipboard
        root.clipboard_clear()
        root.clipboard_append(text)
    
    
    header = const_header()
    body = const_body()
    or_con = const_or()
    qua = const_qua()
    acn = const_acn()
    
    print(str(qua))
    
    combine = header + "\n" + "\n" + body + "\n" + or_con + "\n" + qua + "\n" + acn
    
    new_window = tk.Toplevel(root)
    new_window.title(str(chkID_entry.get()))

    #frame_new = ttk.Frame(root)
    #frame_new.pack()
    
    #sample text for label text box storing paragraph
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ac mi vel felis bibendum ullamcorper. Nam euismod elit ut nulla bibendum, vel aliquet orci bibendum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed vel risus vel velit bibendum hendrerit. Nulla facilisi. Etiam ut nibh non libero facilisis rhoncus non vitae arcu."
    
    widgets_frame_new = ttk.LabelFrame(new_window, text="Quick Editor")
    widgets_frame_new.grid(row=0, column=0, padx=20, pady=10,sticky="w")
    # text box    
    text_box = scrolledtext.ScrolledText(widgets_frame_new, wrap=tk.WORD, width=75, height=25, font=("Arial", 10),state="normal")
    text_box.bind("<Key>", lambda e: "break")
    text_box.bind("<Button-1>", lambda e: "break")      
    text_box.grid(row=0, column=0, padx=5, pady=5,  sticky="ew")
    text_box.insert(tk.END, combine)
    # copy button
    copy_button = ttk.Button(widgets_frame_new, text="Copy", command=copy_code)
    copy_button.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")


def close_all_windows():
    for widget in root.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()    


root = tk.Tk()

style = ttk.Style(root)
root.tk.call("source", "forest-light.tcl")
root.tk.call("source", "forest-dark.tcl")
style.theme_use("forest-dark")

frame = ttk.Frame(root)
frame.pack()

#=======================================FRAME AREA 1: HEADER=======================================
widgets_frame = ttk.LabelFrame(frame, text="Header: Check ID/CF")
widgets_frame.grid(row=0, column=0, padx=20, pady=10,sticky="w")
# entry box
chkID_entry = ttk.Entry(widgets_frame,width=25)
chkID_entry.grid(row=0, column=0, padx=5, pady=5,  sticky="ew")
chkID_entry.insert(0, "Check ID")
# entry box
CF_entry = ttk.Entry(widgets_frame,width=25)
CF_entry.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")
CF_entry.insert(0, "CF")
#=======================================FRAME AREA 1: HEADER=======================================

#======================================FRAME AREA 2: CHECKSTEP=====================================
#Line#1
widgets_frame1 = ttk.LabelFrame(frame, text="Check steps")
widgets_frame1.grid(row=1, column=0, padx=20, pady=10)
# entry box
var = ttk.Entry(widgets_frame1,width=20)
var.grid(row=0, column=0, padx=5, pady=5,  sticky="ew")
var.insert(0, "varOID")
# entry box
formOID = ttk.Entry(widgets_frame1,width=10)
formOID.grid(row=0, column=1, padx=5, pady=5,  sticky="ew")
formOID.insert(0, "formOID")
# entry box
folderOID = ttk.Entry(widgets_frame1,width=10)
folderOID.grid(row=0, column=2, padx=5, pady=5,  sticky="ew")
folderOID.insert(0, "folderOID")
# entry box
recPos = ttk.Entry(widgets_frame1,width=6)
recPos.grid(row=0, column=3, padx=5, pady=5,  sticky="ew")
recPos.insert(0, "recPos")
# entry box
frmRpt = ttk.Entry(widgets_frame1,width=6)
frmRpt.grid(row=0, column=4, padx=5, pady=5,  sticky="ew")
frmRpt.insert(0, "frmRpt")
# entry box
fldRpt = ttk.Entry(widgets_frame1,width=6)
fldRpt.grid(row=0, column=5, padx=5, pady=5,  sticky="ew")
fldRpt.insert(0, "fldRpt")
# check box
b = tk.BooleanVar()
check = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b, command=copy_data)
check.grid(row=0, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua = tk.BooleanVar()
check_qua = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua, command=copy_data_qua)
check_qua.grid(row=0, column=7, padx=5, pady=10, sticky="nsew")
 

#Line2
# entry box
var1 = ttk.Entry(widgets_frame1,width=20)
var1.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")
#var1.insert(0, "varOID")
# entry box
formOID1 = ttk.Entry(widgets_frame1,width=10)
formOID1.grid(row=1, column=1, padx=5, pady=5,  sticky="ew")
#formOID1.insert(0, "formOID")
# entry box
folderOID1 = ttk.Entry(widgets_frame1,width=10)
folderOID1.grid(row=1, column=2, padx=5, pady=5,  sticky="ew")
# entry box
recPos1 = ttk.Entry(widgets_frame1,width=6)
recPos1.grid(row=1, column=3, padx=5, pady=5,  sticky="ew")
#recPos1.insert(0, "recPos")
# entry box
frmRpt1 = ttk.Entry(widgets_frame1,width=6)
frmRpt1.grid(row=1, column=4, padx=5, pady=5,  sticky="ew")
#frmRpt1.insert(0, "frmRpt")
# entry box
fldRpt1 = ttk.Entry(widgets_frame1,width=6)
fldRpt1.grid(row=1, column=5, padx=5, pady=5,  sticky="ew")
#fldRpt1.insert(0, "fldRpt")
# check box
b1 = tk.BooleanVar()
check1 = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b1, command=copy_data)
check1.grid(row=1, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua1 = tk.BooleanVar()
check_qua1 = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua1, command=copy_data_qua)
check_qua1.grid(row=1, column=7, padx=5, pady=10, sticky="nsew")

#Line3
# entry box
var2 = ttk.Entry(widgets_frame1,width=20)
var2.grid(row=2, column=0, padx=5, pady=5,  sticky="ew")
#var2.insert(0, "varOID")
# entry box
formOID2 = ttk.Entry(widgets_frame1,width=10)
formOID2.grid(row=2, column=1, padx=5, pady=5,  sticky="ew")
# entry box
folderOID2 = ttk.Entry(widgets_frame1,width=10)
folderOID2.grid(row=2, column=2, padx=5, pady=5,  sticky="ew")
#formOID2.insert(0, "formOID")
# entry box
recPos2 = ttk.Entry(widgets_frame1,width=6)
recPos2.grid(row=2, column=3, padx=5, pady=5,  sticky="ew")
#recPos2.insert(0, "recPos")
# entry box
frmRpt2 = ttk.Entry(widgets_frame1,width=6)
frmRpt2.grid(row=2, column=4, padx=5, pady=5,  sticky="ew")
#frmRpt2.insert(0, "frmRpt")
# entry box
fldRpt2 = ttk.Entry(widgets_frame1,width=6)
fldRpt2.grid(row=2, column=5, padx=5, pady=5,  sticky="ew")
#fldRpt2.insert(0, "fldRpt")
# check box
b2 = tk.BooleanVar()
check2 = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b2, command=copy_data)
check2.grid(row=2, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua2 = tk.BooleanVar()
check_qua2 = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua2, command=copy_data_qua)
check_qua2.grid(row=2, column=7, padx=5, pady=10, sticky="nsew")


#Line4
# entry box
var3 = ttk.Entry(widgets_frame1,width=20)
var3.grid(row=3, column=0, padx=5, pady=5,  sticky="ew")
#var3.insert(0, "varOID")
# entry box
formOID3 = ttk.Entry(widgets_frame1,width=10)
formOID3.grid(row=3, column=1, padx=5, pady=5,  sticky="ew")
# entry box
folderOID3 = ttk.Entry(widgets_frame1,width=10)
folderOID3.grid(row=3, column=2, padx=5, pady=5,  sticky="ew")
#formOID3.insert(0, "formOID")
# entry box
recPos3 = ttk.Entry(widgets_frame1,width=6)
recPos3.grid(row=3, column=3, padx=5, pady=5,  sticky="ew")
#recPos3.insert(0, "recPos")
# entry box
frmRpt3 = ttk.Entry(widgets_frame1,width=6)
frmRpt3.grid(row=3, column=4, padx=5, pady=5,  sticky="ew")
#frmRpt3.insert(0, "frmRpt")
# entry box
fldRpt3 = ttk.Entry(widgets_frame1,width=6)
fldRpt3.grid(row=3, column=5, padx=5, pady=5,  sticky="ew")
#fldRpt3.insert(0, "fldRpt")
# check box
b3 = tk.BooleanVar()
check3 = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b3, command=copy_data)
check3.grid(row=3, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua3 = tk.BooleanVar()
check_qua3 = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua3, command=copy_data_qua)
check_qua3.grid(row=3, column=7, padx=5, pady=10, sticky="nsew")

#Line5
# entry box
var4 = ttk.Entry(widgets_frame1,width=20)
var4.grid(row=4, column=0, padx=5, pady=5,  sticky="ew")
#var4.insert(0, "varOID")
# entry box
formOID4 = ttk.Entry(widgets_frame1,width=10)
formOID4.grid(row=4, column=1, padx=5, pady=5,  sticky="ew")
# entry box
folderOID4 = ttk.Entry(widgets_frame1,width=10)
folderOID4.grid(row=4, column=2, padx=5, pady=5,  sticky="ew")
#formOID4.insert(0, "formOID")
# entry box
recPos4 = ttk.Entry(widgets_frame1,width=6)
recPos4.grid(row=4, column=3, padx=5, pady=5,  sticky="ew")
#recPos4.insert(0, "recPos")
# entry box
frmRpt4 = ttk.Entry(widgets_frame1,width=6)
frmRpt4.grid(row=4, column=4, padx=5, pady=5,  sticky="ew")
#frmRpt4.insert(0, "frmRpt")
# entry box
fldRpt4 = ttk.Entry(widgets_frame1,width=6)
fldRpt4.grid(row=4, column=5, padx=5, pady=5,  sticky="ew")
#fldRpt4.insert(0, "fldRpt")
# check box
b4 = tk.BooleanVar()
check4 = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b4, command=copy_data)
check4.grid(row=4, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua4 = tk.BooleanVar()
check_qua4 = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua4, command=copy_data_qua)
check_qua4.grid(row=4, column=7, padx=5, pady=10, sticky="nsew")

#Line6
# entry box
var5 = ttk.Entry(widgets_frame1,width=20)
var5.grid(row=5, column=0, padx=5, pady=5,  sticky="ew")
#var4.insert(0, "varOID")
# entry box
formOID5 = ttk.Entry(widgets_frame1,width=10)
formOID5.grid(row=5, column=1, padx=5, pady=5,  sticky="ew")
# entry box
folderOID5 = ttk.Entry(widgets_frame1,width=10)
folderOID5.grid(row=5, column=2, padx=5, pady=5,  sticky="ew")
#formOID4.insert(0, "formOID")
# entry box
recPos5 = ttk.Entry(widgets_frame1,width=6)
recPos5.grid(row=5, column=3, padx=5, pady=5,  sticky="ew")
#recPos4.insert(0, "recPos")
# entry box
frmRpt5 = ttk.Entry(widgets_frame1,width=6)
frmRpt5.grid(row=5, column=4, padx=5, pady=5,  sticky="ew")
#frmRpt4.insert(0, "frmRpt")
# entry box
fldRpt5 = ttk.Entry(widgets_frame1,width=6)
fldRpt5.grid(row=5, column=5, padx=5, pady=5,  sticky="ew")
#fldRpt4.insert(0, "fldRpt")
# check box
b5 = tk.BooleanVar()
check5 = ttk.Checkbutton(widgets_frame1, text="Checked", variable=b5, command=copy_data)
check5.grid(row=5, column=6, padx=5, pady=10, sticky="nsew")
# check box
qua5 = tk.BooleanVar()
check_qua5 = ttk.Checkbutton(widgets_frame1, text="qualifier", variable=qua5, command=copy_data_qua)
check_qua5.grid(row=5, column=7, padx=5, pady=10, sticky="nsew")


#======================================FRAME AREA 2: CHECKSTEP=====================================


#======================================FRAME AREA 3: CHECKACTION=====================================
#Line#1
widgets_frame2 = ttk.LabelFrame(frame, text="Check acn")
widgets_frame2.grid(row=2, column=0, padx=20, pady=10,sticky="w")
# entry box
chkacn_var = ttk.Entry(widgets_frame2,width=20)
chkacn_var.grid(row=0, column=0, padx=5, pady=5,  sticky="ew")
#chkacn_var.insert(0, "varOID")
# entry box
chkacn_formOID = ttk.Entry(widgets_frame2,width=10)
chkacn_formOID.grid(row=0, column=1, padx=5, pady=5,  sticky="ew")
#chkacn_formOID.insert(0, "formOID")
# entry box
chkacn_folderOID = ttk.Entry(widgets_frame2,width=10)
chkacn_folderOID.grid(row=0, column=2, padx=5, pady=5,  sticky="ew")
#chkacn_folderOID.insert(0, "folderOID")
# entry box
chkacn_recPos = ttk.Entry(widgets_frame2,width=6)
chkacn_recPos.grid(row=0, column=3, padx=5, pady=5,  sticky="ew")
#chkacn_recPos.insert(0, "recPos")
# entry box
chkacn_frmRpt = ttk.Entry(widgets_frame2,width=6)
chkacn_frmRpt.grid(row=0, column=4, padx=5, pady=5,  sticky="ew")
#chkacn_frmRpt.insert(0, "frmRpt")
# entry box
chkacn_fldRpt = ttk.Entry(widgets_frame2,width=6)
chkacn_fldRpt.grid(row=0, column=5, padx=5, pady=5,  sticky="ew")
#chkacn_fldRpt.insert(0, "fldRpt")
#======================================FRAME AREA 3: CHECKACTION=====================================

#======================================FRAME AREA 4: QUALIFIER=====================================
#Line#1
widgets_frame3 = ttk.LabelFrame(frame, text="qualifier")
widgets_frame3.grid(row=3, column=0, padx=20, pady=10,sticky="w")
# entry box
qua_var = ttk.Entry(widgets_frame3,width=20)
qua_var.grid(row=0, column=0, padx=5, pady=5,  sticky="ew")
#qua_var.insert(0, "varOID")
# entry box
qua_formOID = ttk.Entry(widgets_frame3,width=10)
qua_formOID.grid(row=0, column=1, padx=5, pady=5,  sticky="ew")
#qua_formOID.insert(0, "formOID")
# entry box
qua_folderOID = ttk.Entry(widgets_frame3,width=10)
qua_folderOID.grid(row=0, column=2, padx=5, pady=5,  sticky="ew")
#qua_folderOID.insert(0, "folderOID")
# entry box
qua_recPos = ttk.Entry(widgets_frame3,width=6)
qua_recPos.grid(row=0, column=3, padx=5, pady=5,  sticky="ew")
#qua_recPos.insert(0, "recPos")
# entry box
qua_frmRpt = ttk.Entry(widgets_frame3,width=6)
qua_frmRpt.grid(row=0, column=4, padx=5, pady=5,  sticky="ew")
#qua_frmRpt.insert(0, "frmRpt")
# entry box
qua_fldRpt = ttk.Entry(widgets_frame3,width=6)
qua_fldRpt.grid(row=0, column=5, padx=5, pady=5,  sticky="ew")
#qua_fldRpt.insert(0, "fldRpt")

submit_button = ttk.Button(widgets_frame3, text="Submit", command=generate_code)
submit_button.grid(row=1, column=0, padx=5, pady=5,  sticky="ew")

clear_button = ttk.Button(widgets_frame3, text="Close All Windows", command=close_all_windows)
clear_button.grid(row=1, column=1, padx=5, pady=5,  sticky="ew")
#======================================FRAME AREA 4: QUALIFIER=====================================

#Repeat short cut
def repeat_entry(event):
    global entry_boxes_formOID
    current_box = event.widget
    current_box_index = entry_boxes_formOID.index(current_box)
    current_box_value = current_box.get()
    if current_box_index > 0:
        prev_box = entry_boxes_formOID[current_box_index - 1]
        prev_box_value = prev_box.get()
        current_box.delete(0, tk.END)
        current_box.insert(0, prev_box_value)
        current_box.focus_set()

def repeat_entry_folderOID(event):
    global entry_boxes_folderOID
    current_box = event.widget
    current_box_index = entry_boxes_folderOID.index(current_box)
    current_box_value = current_box.get()
    if current_box_index > 0:
        prev_box = entry_boxes_folderOID[current_box_index - 1]
        prev_box_value = prev_box.get()
        current_box.delete(0, tk.END)
        current_box.insert(0, prev_box_value)
        current_box.focus_set()

def repeat_entry_recPos(event):
    global entry_boxes_recPos
    current_box = event.widget
    current_box_index = entry_boxes_recPos.index(current_box)
    current_box_value = current_box.get()
    if current_box_index > 0:
        prev_box = entry_boxes_recPos[current_box_index - 1]
        prev_box_value = prev_box.get()
        current_box.delete(0, tk.END)
        current_box.insert(0, prev_box_value)
        current_box.focus_set()
        
entry_boxes_formOID = [formOID,formOID1,formOID2,formOID3,formOID4,formOID5]
for entry_box in entry_boxes_formOID:
    entry_box.bind("<F3>", repeat_entry)

entry_boxes_folderOID = [folderOID,folderOID1,folderOID2,folderOID3,folderOID4,folderOID5]
for entry_box in entry_boxes_folderOID:
    entry_box.bind("<F3>", repeat_entry_folderOID)

entry_boxes_recPos = [recPos,recPos1,recPos2,recPos3,recPos4,recPos5]
for entry_box in entry_boxes_recPos:
    entry_box.bind("<F3>", repeat_entry_recPos)




root.mainloop()

It seems like you have shared a code snippet. How can I assist you with that?

can you please help convert this code to streamlit code

Certainly! Here's a possible Streamlit code based on the provided snippet:

python
Copy
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
        chkacn_folderOID.inser…[omitted]
        
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