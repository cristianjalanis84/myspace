# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 12:16:02 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')


contenido = os.listdir(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\')


fd = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\\' + 'lista_mimics_alizadas.txt', 'a')

for ii in contenido:
    fd.write(ii[:-4] + '\n')

fd.close()