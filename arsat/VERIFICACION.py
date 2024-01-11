# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 10:10:12 2023

@author: calanis
"""
import pandas as pd
import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')


#df_tlm.loc[jj].to_string(index=False)
df_tlm = pd.read_excel(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\tm description comparison ar1 vs ar2_INVrevision.xlsx',usecols=("A"))
df_tlm_desc = pd.read_excel(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\tm description comparison ar1 vs ar2_INVrevision.xlsx',usecols=("H"))
contenido = os.listdir(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\')



def busq_erratas(df_tlm,df_tlm_desc,tm):
    desc = '__no_encontrado___'
    for ii in range(0,int(len(df_tlm))):
        if df_tlm.loc[ii].to_string(index=False) == tm :
            desc = df_tlm_desc.loc[ii].to_string(index=False)
    return desc

#auxs= "{:<12}".format(s) + "{:70}".format(pepito)
for ii in contenido :
    file_origen = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\' + ii, 'r')
    file_destino = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\' + ii[:-4] + '_errata.txt','a')
    origen = file_origen.readlines()
    
    for jj in range(0,len(origen)):
        desc = ' '
        if origen[jj][:7] != 'TM mimi' and origen[jj][:7] != '       ':
            desc = busq_erratas(df_tlm, df_tlm_desc, origen[jj][:7])
        aux =  origen[jj] + "{:<50}".format(desc) + '\n'  
        file_destino.write(aux)
    file_origen.close()
    file_destino.close()