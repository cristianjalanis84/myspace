# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 08:56:07 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')


contenido = os.listdir(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\')
file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\RESUMEN DE DISCREPANCIAS.txt', 'a')

ncodetm = 12
ndescmimic = 70
ndescdb = 45
ncodesoh = 12
ndescsoh = 45 

for ii in contenido:
    file_salida.write('--------------------' + ii[:-4] + '----------------------' + '\n')
    ss="{:<12}".format("TM mimic") +"{:70}".format("Descripcion de la mimic") + "{:45}".format("Descripcion de la base de datos")  +"{:12}".format("TM cod SOH")  +"{:45}".format("Descripcion de la tm en el SOH") + "{:50}".format("Descripcion del sensor en el SOH") + '\n'
    file_salida.write(ss)
    file_aux = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\mimic analizadas\\' + ii)
    lista_aux = file_aux.readlines()
    for jj in range(0,len(lista_aux)):
        if lista_aux[jj][12] == '*':
            file_salida.write(lista_aux[jj])
    file_aux.close()
    
file_salida.close()


    