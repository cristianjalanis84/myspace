# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 12:44:17 2021

@author: crist
"""


# import pandas as pd

# dato = pd.read_excel(r'C:\Users\crist\Desktop\cja\prueba.xlsx')

# print(dato)

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd
from datetime import datetime
TM = "PGH0089"


contenido = os.listdir(r'C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\LEOP\\')
fecha = datetime.now()
fecha_frt = fecha.strftime("%c")



# df_tlm = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) #
# df_desc = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

# df_tlm = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) 
# df_desc = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

file_object = open(r'C:\Users\crist\Desktop\satelite\scrips\fops_ar1.txt', 'a')
title_1 ="********************************************************************"
title_2 ="*  " + fecha_frt
title_3 ="*  Busqueda de la TM " + TM 
title_4 ="********************************************************************"
file_object.write(title_1 + '\n' + title_2 + '\n' + title_3 + '\n' + title_4 + '\n')
for nn in contenido:
    arch_fop =r"C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\LEOP\\" + nn
    
    print(arch_fop)
    file_object.write( nn + '\n')
    df_tlm = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("G"))
    
    df_desc = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("C"))
    df_step = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("A"))
    for ii in range(0,len(df_tlm)):
        var_tlm = df_tlm.loc[ii].to_string(index=False)
        #var2_tlm = var_tlm[14:]
        if var_tlm == TM :
            var_desc = df_desc.loc[ii].to_string(index=False)
            # var2_desc = var_desc[23:]
            print(ii)
            print(var_tlm)
            print(var_desc)
            jj = ii
            step = df_step.loc[jj].to_string(index=False)
            while step == "NaN"  :
                jj -= 1
                step = df_step.loc[jj].to_string(index=False)
            file_object.write(str(ii+2) + "  " + var_tlm + "  " + var_desc + "  In Step : " + step +'\n')
            
file_object.close()
# df = pd.read_excel(r"C:\Users\crist\Downloads\readfile.xlsx")
# print(df)