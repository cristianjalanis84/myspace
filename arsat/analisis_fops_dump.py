# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 13:40:44 2022

@author: crist
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook


#contenido = os.listdir(r'C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')
contenido = os.listdir(r'C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures\fops\\')#ar2
fecha = datetime.now()
fecha_frt = fecha.strftime("%c")



# df_tlm = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) #
# df_desc = pd.read_excel(r"C:\Users\crist\Downloads\0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

# df_tlm = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("G")) 
# df_desc = pd.read_excel("0841-3900-6PCOP-036-H SADM Anomaly.xlsx",sheet_name="Operations List",usecols=("C"))

file_object =           open(r'C:\Users\crist\Desktop\satelite\scrips\fops_ar2_DUMP_ANALISIS_SIN_FORMULA.txt', 'a')
file_object_tc_config = open(r'C:\Users\crist\Desktop\satelite\scrips\TC_DUMP_AR2.txt', 'r')
file_object_list =      open(r'C:\Users\crist\Desktop\satelite\scrips\fops_ar2_dump.txt', 'r')
title_1 ="********************************************************************"
title_2 ="*  " + fecha_frt
title_3 ="*  Busqueda del tc set channels " 
title_4 ="********************************************************************"
file_object.write(title_1 + '\n' + title_2 + '\n' + title_3 + '\n' + title_4 + '\n')
list_of_fops=file_object_list.readlines()
tc_dump_config = file_object_tc_config.readlines()

def buscar_tc_dump(s,tc_dump):
    encontrado=0
    for ii in tc_dump:
        var=ii[ii.find('D'):]
        var=var[:var.find(' ')]
        if var == s :
            encontrado=1
            break
            
    return encontrado
    
    
    
    
for mm in list_of_fops:
    
    for nn in contenido:
        if mm[:-1]== nn:
            #arch_fop =r"C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\" + nn
            arch_fop =r"C:\Users\crist\Desktop\satelite\scrips\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures\fops\\" + nn  #ar2
            print(arch_fop)
            file_object.write( nn + '\n')
            df_step = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("A"))
            df_tlm = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("C"))#descripcion del tc
            
            df_desc = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("D"))#comando
            df_arg = pd.read_excel(arch_fop,sheet_name="Operations List",usecols=("E"))#argumentos
            
            # wb = load_workbook(filename = arch_fop)
            # sheet_names = wb.get_sheet_names()
            # indice_op_list=0
            # for ii in range (len(sheet_names)):
            #     var = sheet_names[ii]
            #     if var=='Operations List' :
            #         indice_op_list=ii
            # name = sheet_names[indice_op_list] #operation list
            # sheet_ranges = wb[name]
            # df_formula = pd.DataFrame(sheet_ranges.values)
            
            for ii in range(0,len(df_tlm)):
                var_desc = df_desc.loc[ii].to_string(index=False)
                #var2_tlm = var_tlm[14:]
                if var_desc.find("DSE0000")>-1 or var_desc.find("DSE0001")>-1:
                    var_desc = df_desc.loc[ii].to_string(index=False)
                    var_desc_tc = df_tlm.loc[ii].to_string(index=False)
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
                    file_object.write(var_desc_tc + "  " + var_desc +  "  " + var_desc_tc_arg1 + "  " + var_desc_tc_arg2 +"  In Step : " + step +'\n')
                elif var_desc.find("DSF0100")>-1:
                    var_desc = df_desc.loc[ii].to_string(index=False)
                    var_desc_tc = df_tlm.loc[ii].to_string(index=False)
                    # var_desc_tc_arg1= df_arg.loc[ii].to_string(index=False)
                    # var_desc_tc_arg2= df_arg.loc[ii+1].to_string(index=False)
                    # var2_desc = var_desc[23:]
                    # print(ii)
                    # print(var_tlm)
                    # print(var_desc)
                    jj = ii
                    step = df_step.loc[jj].to_string(index=False)
                    while step == "NaN"  :
                        jj -= 1
                        step = df_step.loc[jj].to_string(index=False)
                    file_object.write( var_desc_tc + "  " + var_desc +  "  " + "  In Step : " + step +'\n')
                elif var_desc.find("DSF0001")>-1 or var_desc.find("DSF0002")>-1 :
                    var_desc = df_desc.loc[ii].to_string(index=False)
                    var_desc_tc = df_tlm.loc[ii].to_string(index=False)
                    # var_desc_tc_arg1= df_arg.loc[ii].to_string(index=False)
                    # var_desc_tc_arg2= df_arg.loc[ii+1].to_string(index=False)
                    # var2_desc = var_desc[23:]
                    # print(ii)
                    # print(var_tlm)
                    # print(var_desc)
                    jj = ii
                    step = df_step.loc[jj].to_string(index=False)
                    while step == "NaN"  :
                        jj -= 1
                        step = df_step.loc[jj].to_string(index=False)
                    file_object.write( var_desc_tc + "  " + var_desc +  "  " + "  In Step : " + step +'\n')
                elif  var_desc != 'NaN' :
                    if buscar_tc_dump(var_desc.strip(),tc_dump_config):
                        var_desc = df_desc.loc[ii].to_string(index=False)
                        var_desc_tc = df_tlm.loc[ii].to_string(index=False)
                        var_desc_tc_arg1= df_arg.loc[ii].to_string(index=False)
                        var_desc_tc_arg2= df_arg.loc[ii+1].to_string(index=False)
                        # tc_form=df_formula[3][ii+1] # ubicacion del tc CON FORMULA
                        # arg1_form=df_formula[4][ii+1] # ubicacion del arg 1 CON FORMULA
                        # arg2_form=df_formula[4][ii+2] # ubicacion del tc CON FORMULA
                        
                        # var2_desc = var_desc[23:]
                        # print(ii)
                        # print(var_tlm)
                        # print(var_desc)
                        jj = ii
                        step = df_step.loc[jj].to_string(index=False)
                        while step == "NaN"  :
                             jj -= 1
                             step = df_step.loc[jj].to_string(index=False)
                        #file_object.write(str(ii) +"   "+var_desc_tc + "  " + var_desc +  "  "  + var_desc_tc_arg1 + "  " + var_desc_tc_arg2 +"  formula del tc = "+ str(tc_form) + "  formula del word count = "+ str(arg1_form) + "  formula del offset = " + str(arg2_form) + "  In Step : " + step +'\n')
                        file_object.write(str(ii) +"   "+var_desc_tc + "  " + var_desc +  "  "  + var_desc_tc_arg1 + "  " + var_desc_tc_arg2  + "  In Step : " + step +'\n')

file_object.close()
file_object_list.close()
file_object_tc_config.close()
# df = pd.read_excel(r"C:\Users\crist\Downloads\readfile.xlsx")
# print(df)