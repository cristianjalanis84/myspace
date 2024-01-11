# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 14:51:31 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd
from difflib import SequenceMatcher
import time

def busqueda(fop_nom, Description_TM, name_TM,file_object):
    for nn in contenido :
        file_object.write(nn + '\n')
        if fop_nom != nn[:-4]:
            arch_fop_dest   = r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + nn
           
            my_arch_to_data_table = pd.read_excel(arch_fop_dest,sheet_name="Data Table",usecols=("C"))
            # my_arch_to_op_list_tm = pd.read_excel(arch_fop_dest,sheet_name="Operations List",usecols=("G"))
            # my_arch_to_op_list_desc_tm = pd.read_excel(arch_fop_dest,sheet_name="Operations List",usecols=("C"))
            my_arch_to_op_list= pd.read_excel(arch_fop_dest,sheet_name="Operations List")
            #my_arch_to_concheck = pd.read_excel(arch_fop_dest,sheet_name="ConCheck Def",usecols=("A"))
            file_object.write('*************Analizando Data Table***************' + '\n' )
            # for ii in range(9,len(my_arch_to_data_table)):
                
            #     # a = my_arch.loc[ii].to_string(index=False).replace(' ','').upper()
            a = Description_TM
            
            for jj in range(9,len(my_arch_to_data_table)):
                b = my_arch_to_data_table.loc[jj].to_string(index=False).replace(' ','').upper()
                if b != 'NAN':
                    r = SequenceMatcher(a=a,b=b).ratio()
                    if r >= 0.7 or b.find(a) > -1:
                        file_object.write('\n' + '....................................................' + Description_TM +'    '+ my_arch_to_data_table.loc[jj].to_string(index=False)+'\n')
            file_object.write('*************Analizando Operation List***************' + '\n' )
            for ii in range(1,len(my_arch_to_op_list)):
                
                a = Description_TM
                b = my_arch_to_op_list.iat[ii,2] # columna 2 es la de  descripcion de tm
                if type(b != str):
                    b = str(b)
                b = b.replace(' ','').upper()
                
                aux = my_arch_to_op_list.iat[ii,6] # la columna 6 es la del codigo de la tm
                if type(aux != str):
                    aux = str(aux)
                aux = aux.replace(' ','').upper()
                if b != 'NAN' :
                    if (SequenceMatcher(a=a,b=b).ratio() >= 0.7) or ( aux == name_TM) or b.find(a) > -1 :
                        
                        file_object.write( '\n' + '....................................................' +Description_TM + '    ' + name_TM + '    ' + aux +'     '+ b +'\n')


contenido = os.listdir(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')
# file_object = open(r'C:\Users\calanis\Desktop\info sat\scrips\demo21.txt', 'a')

# arch_fop_origen = r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + fop_nom
# my_arch = pd.read_excel(arch_fop_origen,sheet_name="Data Table",usecols=("C"))
fops_arch_nom = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="fops_analizados",usecols=("A"))
fops_arch_desc = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="fops_analizados",usecols=("B"))
fops_arch_tm = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="fops_analizados",usecols=("C"))
fops_arch_exp_val = pd.read_excel(r'C:\Users\calanis\Desktop\info sat\scrips\fops_ar1.xlsx',sheet_name="fops_analizados",usecols=("D"))

ii= 2
fin = False
cont_nn = 0

#for ii in range(27,max(len(fops_arch_nom),len(fops_arch_desc))):
for ii in range(0,4):
    if fops_arch_nom.loc[ii].to_string(index=False) != 'NaN':
        fop_nom = fops_arch_nom.loc[ii].to_string(index=False)
        file_object = open(r'C:\Users\calanis\Desktop\info sat\scrips\\' + fop_nom, 'a')
        print('Analizando TMs de ' + fop_nom + '\n')
        file_object.write('++++++++++++++++++++++++++++++++++++++' + fop_nom + '+++++++++++++++++++++++++++++++++++++++++' +  '\n')
        nn= ii
        Description_TM = fops_arch_desc.loc[nn].to_string(index=False)
        if Description_TM != 'NaN':
            print('Analizando  ' + Description_TM + '\n')
            name_TM = fops_arch_tm.loc[nn].to_string(index=False)
            t = time.process_time()
            busqueda(fop_nom,Description_TM,name_TM,file_object)
            t = time.process_time()
            while fops_arch_nom.loc[nn+1].to_string(index=False) == 'NaN':
                Description_TM = fops_arch_desc.loc[nn+1].to_string(index=False)
                print('Analizando  ' + Description_TM + '\n')
                name_TM = fops_arch_tm.loc[nn+1].to_string(index=False)
                t = time.process_time()
                busqueda(fop_nom,Description_TM,name_TM,file_object)
                elapsed_time = time.process_time() - t
                print('tiempo entre analisis ' + str(elapsed_time) + '\n')
                
                nn += 1
        file_object.close()
            
  
        
        




                
                
            
            
            
# b = a.replace(' ','')



file_object.close()