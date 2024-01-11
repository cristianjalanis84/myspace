# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:18:59 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd

contenido = os.listdir(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')


file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\obcs_conf_ar1_sseq.txt', 'a')
#fops_arch_nom = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="fops_analizados",usecols=("A"))

# s=[]

# s = [fops_arch_nom.loc[ii].to_string(index=False) for ii in range(len(fops_arch_nom)) if fops_arch_nom.loc[ii].to_string(index=False) != 'NaN']

ss = {}
#
    # fops_desc = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="Operations List",usecols=("C"))
    # fops_tm= pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="Operations List",usecols=("G"))
ss_desc = {ii[:-4]:[] for ii in contenido }
ss_tm = ss_desc.copy()



for ii in contenido:
    ff_desc = fops_desc = pd.read_excel(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + ii ,sheet_name="Operations List",usecols=("C"))
    ff_tm = pd.read_excel(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + ii,sheet_name="Operations List",usecols=("G"))
    ss_desc[ii[:-4]] = [ff_desc.loc[jj].to_string(index=False) for jj in range(len(ff_desc)) ]#if ff_desc.loc[jj].to_string(index=False) != 'NaN']
    ss_tm[ii[:-4]] = [ff_tm.loc[jj].to_string(index=False) for jj in range(len(ff_tm)) ]#if ff_tm.loc[jj].to_string(index=False) != 'NaN']
    



ff_tm = pd.read_excel(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\0841-3900-6PCOP-100-K OBCS Configuration.XLSX'  ,sheet_name="TM_TC Tables",usecols=("E"))
ff_tm_desc = pd.read_excel(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\0841-3900-6PCOP-100-K OBCS Configuration.XLSX'  ,sheet_name="TM_TC Tables",usecols=("F"))



    
#ss="{:<12}".format("TM mimic") +"{:70}".format("Descripcion de la mimic")   
    
for ii in range(35,130,2):
   
    tm = ff_tm.loc[ii].to_string(index=False)
    tm_desc = ff_tm_desc.loc[ii].to_string(index=False)
    print(tm)
    print(tm_desc)
    fftm = False
    for jj in ss_tm :
        
        for kk in range(len(ss_tm[jj])):
            
            if ss_tm[jj][kk].find(tm) > -1 or ss_desc[jj][kk].upper().find(tm) > -1 or ss_tm[jj][kk] == tm:
                if fftm == False :
                    file_salida.write('Analizando ' + jj + '\n' )
                    fftm = True
                sss= "{:<12}".format(ss_tm[jj][kk]) +"{:50}".format(ss_desc[jj][kk]) +  '\n'
                file_salida.write(sss)
        fftm = False
                
                
file_salida.close()