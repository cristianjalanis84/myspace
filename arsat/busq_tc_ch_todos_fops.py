# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:50:55 2022

@author: crist
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd
from datetime import datetime
TM = "PGH0089"


contenido = os.listdir(r'C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')
fecha = datetime.now()
fecha_frt = fecha.strftime("%c")



# df_tlm = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) #
# df_desc = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

# df_tlm = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) 
# df_desc = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

file_object = open(r'C:\Users\crist\Desktop\satelite\scrips\fops_SSGM.txt', 'a')
# file_object_list = open(r'C:\Users\crist\Desktop\satelite\scrips\fops_ar1_dump.txt', 'r')
title_1 ="********************************************************************"
title_2 ="*  " + fecha_frt
title_3 ="*  Busqueda del tc set channels " 
title_4 ="********************************************************************"
file_object.write(title_1 + '\n' + title_2 + '\n' + title_3 + '\n' + title_4 + '\n')
# list_of_fops=file_object_list.readlines()

    
for nn in contenido:
    
    arch_fop =r"C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\" + nn
    
    print(arch_fop)
    file_object.write( nn + '\n')
    df_step = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("A"))
    df_tlm = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("C"))#descripcion de la tm
    
    df_desc = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("D"))#comando
    df_arg = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("E"))#argumentos
    # writer=pd.ExcelWriter(r"C:\Users\crist\Desktop\df_prueba_1.xlsx", engine="openpyxl", mode="a")
    indice=0
    for ii in range(0,len(df_tlm)):
        var_tlm = df_tlm.loc[ii].to_string(index=False)
        #writer=pd.ExcelWriter(r"C:\Users\crist\Desktop\df_prueba_1.xlsx", engine="openpyxl", mode="a")
        #var2_tlm = var_tlm[14:]
        if var_tlm.find("SSGM WRITE VAR FDIR") > -1:
            var_desc = df_tlm.loc[ii].to_string(index=False)
            var_desc_tc = df_desc.loc[ii].to_string(index=False)
            var_desc_tc_arg1= df_arg.loc[ii].to_string(index=False)
            var_desc_tc_arg2= df_arg.loc[ii+1].to_string(index=False)
            # var2_desc = var_desc[23:]
            # print(ii)
            # print(var_tlm)
            # print(var_desc)
            jj = ii
            step = df_step.loc[jj].to_string(index=False)
            while step == "NaN"  :
                jj -= 1
                step = df_step.loc[jj].to_string(index=False)
            file_object.write( var_desc + "  " + var_desc_tc +  "  " + var_desc_tc_arg1 + "  " + var_desc_tc_arg2 +"  In Step : " + step +'\n')
            # df1= pd.DataFrame([var_desc + "  " + var_desc_tc +  "  " + var_desc_tc_arg1 + "  " + var_desc_tc_arg2 +"  In Step : " + step])
            # with pd.ExcelWriter(r"C:\Users\crist\Desktop\df_prueba_2.xlsx", engine="openpyxl", mode="a") as writer:
            #     df1.to_excel(writer, sheet_name=nn, startrow=indice, startcol=0,index='False',header='False',merge_cells=('False'))
            indice+=1
            
file_object.close()
# file_object_list.close()
# df = pd.read_excel(r"C:\Users\crist\Downloads\readfile.xlsx")
# print(df)