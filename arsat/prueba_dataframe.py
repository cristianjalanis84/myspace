# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 14:04:08 2022

@author: crist
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd


df_tlm = pd.read_excel(r'C:\Users\crist\Desktop\satelite\scrips\ar1\0841-3900-6PCOP-055-I  PCU Switch Over.xlsx',sheet_name="Operations List",usecols=("G"))
# df_tlm2 = pd.read_excel(r'C:\Users\crist\Desktop\satelite\scrips\ar1\0841-3900-6PCOP-055-I  PCU Switch Over.xlsx',sheet_name="Operations List",usecols=("A"))
# df_tlm3 = pd.read_excel(r'C:\Users\crist\Desktop\satelite\scrips\ar1\0841-3900-6PCOP-055-I  PCU Switch Over.xlsx',sheet_name="Operations List",usecols=("B"))
# df_tlm4 = pd.read_excel(r'C:\Users\crist\Desktop\satelite\scrips\ar1\0841-3900-6PCOP-055-I  PCU Switch Over.xlsx',sheet_name="Operations List",usecols=("C"))
# df_tlm5 = pd.read_excel(r'C:\Users\crist\Desktop\satelite\scrips\ar1\0841-3900-6PCOP-055-I  PCU Switch Over.xlsx',sheet_name="Operations List",usecols=("D"))

contenido = os.listdir(r'C:\Users\crist\Desktop\satelite\scrips\Nueva carpeta\\')