# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 13:13:44 2022

@author: crist
"""

import pandas as pd

# a="Holiss"
# b="chau"
# c="fjcsvn"
# d="qqqw"


file_object = open(r'C:\Users\crist\Desktop\satelite\scrips\fops_ar1_channels_1_1_todos_1.txt', 'r')
list_fops_ch=file_object.readlines()

ii=0
index=0
while ii <len(list_fops_ch):
    s=list_fops_ch[ii]
    
    if s[:4]=="0841":
        df1 = pd.DataFrame([s[:s.find('.')]])
        s=s[s.find('_'):]
        name=s[:s.find('.')]
        
        with pd.ExcelWriter(r"C:\Users\crist\Desktop\df_prueba_4.xlsx", engine="openpyxl", mode="a") as writer:
            df1.to_excel(writer, sheet_name=name, startrow=index, startcol=0,index='False',header='False',merge_cells=('False'))
        aux=list_fops_ch[ii]
        jj=ii
        index+=1
        s=list_fops_ch[jj+1]
        while s[:4] != "0841":
            jj+=1
            s=list_fops_ch[jj]
            df1 = pd.DataFrame([s[:-1]])
            #with pd.ExcelWriter(r"C:\Users\crist\Desktop\df_prueba_3.xlsx", engine="openpyxl", mode="a") as writer:
            df1.to_excel(r"C:\Users\crist\Desktop\df_prueba_4.xlsx", sheet_name=name, startrow=index, startcol=0,index='False',header='False',merge_cells=('False'))
            
            index+=1
        ii+=jj-ii 
    ii+=1
        
# df1.to_excel(r"C:\Users\crist\Desktop\df_prueba_1.xlsx",sheet_name='Hoja1',index='False') 