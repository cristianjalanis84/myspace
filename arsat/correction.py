# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:59:08 2023

@author: calanis
"""



#file_object = open(r'C:\Users\calanis\Desktop\SCC_V4795_full\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_APP_TEMP.DRW', 'rw')#TVAC\
file_object = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TVAC_SATELLITE_APP_TEMP_prueba.DRW', 'r')    
file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TVAC_SATELLITE_APP_TEMP.txt', 'r')
file_object_modif = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TVAC_SATELLITE_APP_TEMP_prueba_write.DRW', 'a')
ncodetm = 12
ndescmimic = 70
ndescdb = 45
ncodesoh = 12
ndescsoh = 45 


s=file_salida.readlines()
mimic_mod = file_object.readlines()

file_object.close()



for ii in range(0,len(s)):
    if s[ii][12] == '*':
        correct_value = s[ii][ncodetm + ndescmimic : ncodetm + ndescmimic + ndescdb]
        incorrect_value_aux =s[ii][ncodetm + 1 : ncodetm + ndescmimic]
        incorrect_value = incorrect_value_aux[:incorrect_value_aux.find('*')]
        for jj in range (0,len(mimic_mod)):
            if mimic_mod[jj].find(incorrect_value) > -1 :
                aux = mimic_mod[jj][:mimic_mod[jj].find(incorrect_value)] + correct_value + '"' + '\n'
                mimic_mod[jj] = aux
            

for ii in range (0 , len(mimic_mod)):
    file_object_modif.write(mimic_mod[ii])
file_salida.close()
file_object_modif.close()