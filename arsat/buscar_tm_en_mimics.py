# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 13:05:50 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')

contenido = os.listdir(r'C:\Users\calanis\Desktop\SCC_V5060_full\mimics.ar1\\')

f=open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\resul_busq_mimics_L1T0021.txt ', 'a')

identTmCode = "   5 0 1"
tm='L1T0021'

def obtenerCodTm (s):
    aux = s[s.find("_")+1:]
    aux = aux[:aux.find("_")]
    return aux



for ii in contenido:
    print('procesando ' + ii + '\n')
    if ii[-4:] == '.DRW' :
        fd=open(r'C:\Users\calanis\Desktop\SCC_V5060_full\mimics.ar1\\' + ii , 'r')
        S = fd.readlines()
        for jj in range(len(S)):
            if S[jj][:8] == identTmCode:
                ss=obtenerCodTm(S[jj])
                if ss == tm :
                    f.write(tm + ' encontrada en ' + ii + '\n' )
                    
                
        
        fd.close()
        
f.close()