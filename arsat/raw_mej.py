# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 19:45:50 2022

@author: calanis
"""

import os
import sys

print(os.path.dirname(sys.executable)+'\Scripts\\')
file_object = open(r'C:\Users\crist\Desktop\satelite\scrips\fo334.txt', 'r')
dest_object = open(r'C:\Users\crist\Desktop\satelite\scrips\filedest.txt', 'a')
a = file_object.readlines()

mfpos0 = (101 - 3*2 - 2 - 1)# nro de caracteres de la fila 4 - 3 bytes de 2 caracteres - 2 "\r" - 1 "\n"
mfpos1 = (101 - 3*2 - 2 + 1)
frame = hex(21)
position = 94
size_dato=1
c = "\r"
k = "".join(a)

jj = 0
kk = 0


while jj < len(a):
    b = a [jj][0:15]
    if b == "Packet len: 336":               #verifico que sea un minor frame (identificado con el tamanio 336)
        mf = a[jj+4][mfpos0:mfpos1]
        if mf == frame[2:4]:                 # de frame saco los caracteres "0x" para realizar la comparacion
            kk = jj
            for kk in range (kk , kk + 12) : #obtengo las 12 lineas del minor frame
                dest_object.write( a[kk] )
            dest_object.write( "\n" )
    jj = jj + 1
dest_object.close() 
dest_object = open(r'C:\Users\crist\Desktop\satelite\scrips\filedest.txt', 'r')
jj = 0
temp_filedest = dest_object.readlines()
size_enc = len("Packet len: 336 (0x150) Packet Epoch:")

for ii in range(len(temp_filedest)):
    
    if temp_filedest[ii][:size_enc]=="Packet len: 336 (0x150) Packet Epoch:":
        
        while size_dato:
            if position <= 2:
            
            elif position >=3 and position <= 34 :
            
            elif position >=35 and position <= 66 :
                
            elif position >=67 and position <= 98 :
                
            elif position >=99 and position <= 130 :
                
            elif position >=131 and position <= 162 :
                
            elif position >=163 and position <= 194 :
                
            elif position >=195 and position <= 210 :
    
    




final_object = open(r'C:\Users\crist\Desktop\satelite\scrips\fileok.txt', 'a')
for jj in range(len(temp_filedest)):
    final_object.write( temp_filedest[jj])
         

final_object.close()
       
file_object.close() 
dest_object.close() 
 
        
