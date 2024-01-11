# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 09:54:02 2023

@author: calanis
"""
import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')
import pandas as pd
from difflib import SequenceMatcher

contenido = os.listdir(r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\')
file_object = open(r'C:\Users\calanis\Desktop\info sat\scrips\demo11.txt', 'a')
fop_nom ='0841-3900-6PCOP-092-J ACE Switch over.xlsm'
arch_fop_origen = r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + fop_nom
my_arch = pd.read_excel(arch_fop_origen,sheet_name="Data Table",usecols=("C"))





for nn in contenido :
    file_object.write(nn + '\n')
    if fop_nom != nn:
        arch_fop_dest   = r'C:\Users\calanis\Desktop\Satellite Operations Handbook (SOH) - Part 2 - Flight Operational Procedures_ar1\fops\\' + nn
       
        my_arch_to = pd.read_excel(arch_fop_dest,sheet_name="Data Table",usecols=("C"))
        for ii in range(9,len(my_arch)):
            a = my_arch.loc[ii].to_string(index=False).replace(' ','').upper()
            if a != 'NAN':
                for jj in range(9,len(my_arch_to)):
                    b = my_arch_to.loc[jj].to_string(index=False).replace(' ','').upper()
                    if b != 'NAN':
                        r = SequenceMatcher(a=a,b=b).ratio()
                        if r >= 0.7 :
                            file_object.write( my_arch.loc[ii].to_string(index=False)+'    '+ my_arch_to.loc[jj].to_string(index=False)+'\n')
            
# b = a.replace(' ','')



file_object.close()
s1 = 'scagainstephola'
s2 = 'scastep'

result = SequenceMatcher(a=s1,b=s2).ratio()