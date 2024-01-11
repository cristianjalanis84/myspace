# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:27:45 2023

@author: calanis
"""

import pandas as pd
import time


nn='0841-3900-6PCOP-055-I  PCU Switch Over.xlsx'
arch_fop_dest   = r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + nn
t = time.process_time()
my_arch_to_data_table = pd.read_excel(arch_fop_dest,sheet_name="Operations List")
elapsed_time = time.process_time() - t

t = time.process_time()
my_arch_to_data_table = pd.read_excel(arch_fop_dest,sheet_name="Operations List",usecols=("C"))
elapsed_time2 = time.process_time() - t

t = time.process_time()
my_arch_to_data_table = pd.read_excel(arch_fop_dest,sheet_name="Operations List",usecols=("G"))
elapsed_time3 = time.process_time() - t

t = time.process_time()
my_arch_to_data_table = pd.read_excel(arch_fop_dest,sheet_name="Operations List",usecols=("D"))
elapsed_time4 = time.process_time() - t


for ii in range(len(my_arch_to_data_table)):
    s = my_arch_to_data_table.iat[ii,2]
    if type(s) != str:
        s = str(s)
    if s == 'PCU Switch-over Page 1':
        print('nro de fila = ' + str(ii) + '\n')

#my_arch_to_data_table.loc[ii].to_string(index=False)