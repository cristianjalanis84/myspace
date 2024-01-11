# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:44:13 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd

contenido = os.listdir(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')


file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\switch_hpa_v3.txt', 'a')
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
    


aux = ['01A','01B','02A','02B','03A','03B','04A','04B','05A','05B','06A','06B','07A','07B','08A','08B','09A','09B','10A','10B','11A','11B','12A','12B','13A','13B','14A','14B','15A','15B','16A','16B']




    
#ss="{:<12}".format("TM mimic") +"{:70}".format("Descripcion de la mimic")   
    
for ii in aux:
   
    
    
    fftm = False
    for jj in ss_tm :
        
        for kk in range(len(ss_tm[jj])):
            
            if ss_desc[jj][kk].upper().find(ii) > -1:
                if fftm == False :
                    file_salida.write('Analizando ' + jj + '\n' )
                    fftm = True
                sss= "{:<12}".format(ss_tm[jj][kk]) +"{:50}".format(ss_desc[jj][kk]) +  '\n'
                file_salida.write(sss)
        fftm = False
                
                
file_salida.close()