# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:44:33 2022

@author: crist
"""

import os
import sys

print(os.path.dirname(sys.executable)+'\Scripts\\')
file_object = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\XeNFZ.TXT', 'r')
dest_object = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\filedest_OIT0111.txt', 'a')
a = file_object.readlines()

mfpos0 = (101 - 3*2 - 2 - 1)#92 nro de caracteres de la fila 4 - 3 bytes de 2 caracteres - 2 "\r" - 1 "\n"
mfpos1 = (101 - 3*2 - 2 + 1)#96
frame = '05'   #en hexadecimal, se omite el 0x
c = "\r"
k = "".join(a)

jj = 0
kk = 0
position = 82

while jj < len(a):
    b = a [jj][0:15]
    if b == "Packet len: 336":               #verifico que sea un minor frame (identificado con el tamanio 336)Packet len: 336 
        mf = a[jj+4][mfpos0:mfpos1]
        if  mf.find(frame) > -1 :                 # de frame saco los caracteres "0x" para realizar la comparacion
            kk = jj
            for kk in range (kk , kk + 12) : #obtengo las 12 lineas del minor frame
                dest_object.write( a[kk] )
            dest_object.write( "\n" )
    jj = jj + 1
dest_object.close() 
dest_object = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\filedest_OIT0111.txt', 'r')
jj = 0
temp_filedest = dest_object.readlines()
size_enc = len("Packet len: 336 (0x150) Packet Epoch:")
temp_tm = []
dates_tm = []
tamanio = 4 #Bytes

# while jj < len(temp_filedest):
#     b = temp_filedest [jj][0:15]
#     if b == "Packet len: 336":
#         nn = jj
#         temp_tm.append(temp_filedest[jj][size_enc:size_enc + 20]) #obtengo el tiempo del frame
        
#         dates_tm.append(temp_filedest[jj + 4][mfpos1:])           #añado desde tm de pos 1 hasta el final de la linea
#         for mm in range(5,11):
#             dates_tm.append(temp_filedest[jj + mm][4:])           #añado toda la linea menos los primeros 4 caracteres
#         dates_tm.append(temp_filedest[jj + 11][4:])
#         dates_tm.append("###########")    
#     jj = jj + 1

ll=0
findelinea = False
jj =0
while jj < len(temp_filedest):
    b = temp_filedest [jj][0:15]
    primspos = 1
   
    nn=0
    if b == "Packet len: 336":
        kk = 1
        while kk < 210 :
            findelinea = False
            
            if primspos :
                var_temp=temp_filedest[jj + 4][mfpos1+(kk-1)*4-1:mfpos1+(kk-1)*4+4]
                linea =list(temp_filedest[jj+4])
                
                if kk == position:
                    #var_temp[0]="#"
                    #print(kk)
                    for gg in range (0,4):
                        if linea[mfpos1+(kk-1)*4-1 +gg]==" ":
                            linea[mfpos1+(kk-1)*4-1 +gg]="#"
                    #var_temp.replace("\r","#")
                    #temp_filedest[jj + 4][mfpos1+(kk-1)*3:mfpos1+(kk-1)*4+4].replace("\r","#")
                    linea="".join(linea)
                    temp_filedest[jj+4]=linea
                               #salimos de la busqueda de la tm
                if var_temp[3]=="\n":
                    primspos = 0
                    nn+=1
                kk+=1
               
            else :
                ff=1
                ll=0
                while findelinea==False:
                    datovalido=True
                    if ff < 3:
                        var_temp=temp_filedest[jj+nn+4][ll:ll+4]
                        ff+=1
                        if ff==2:
                            ll+=4
                    else:
                        ll+=3
                        var_temp=temp_filedest[jj+nn+4][ll:ll+4]
                        
                    linea2 = list(temp_filedest[jj+nn+4])
                    if var_temp[0] == " ":
                        if kk==position:
                            #var_temp[0]="#"
                            #print("Encontre la posicion")
                            #print(kk)
                            for gg in range (0,4):
                                if linea2[ll +gg]==" ":
                                    print("encontre un espacio vacio")
                                    linea2[ll +gg]="#"
                            linea2="".join(linea2)
                            #print(linea2)
                            temp_filedest[jj+4+nn]=linea2
                            # var_temp.replace("\r","#")
                            # temp_filedest[jj+nn+4][ll:ll+4].replace("\r","#")
                        if var_temp[3]=="\n":
                            nn+=1
                            findelinea=True
                            #print(findelinea)
                    else:
                        datovalido =False#dato invalido (son los primeros caracteres de la linea)
                        #print("dato valido")
                        #print(datovalido)
                    
                    
                    
                    if datovalido :
                        kk +=1
                        
    jj+=1


final_object = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\FILEOK.txt', 'a')
for jj in range(len(temp_filedest)):
    final_object.write( temp_filedest[jj])
         
# while jj < len(a):
#     b = a [jj][0:15]
#     if b == "Packet len: 336":
#         mf = a[jj+4][mfpos0:mfpos1]
       
#         if mf == frame[2:4]:
#             print(mf)
         
#     jj = jj + 1
final_object.close()
       
file_object.close() 
dest_object.close() 
 
        
