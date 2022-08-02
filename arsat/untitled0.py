# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:37:02 2022

@author: crist
"""

# var = ["Holiss","Como andas","bye"]
# print(var)
# ss=list(var[1][0:5])
# print(ss)
# print(ss[0])
# print(ss[1])
# print(ss[2])
# print(ss[3])
# print(ss[4])
# print(ss[1:4])
# ss="".join(ss)
# print(ss)
# var[0]="que pasa?"
# print(var)
inicioTc = "&def_cmd_list {\n"
finTc ="//EndSection Commands List Definition\n"
file_object = open(r'C:\Users\crist\Desktop\satelite\scrips\AR1_TC.db', 'r')
file_objectSal = open(r'C:\Users\crist\Desktop\satelite\scrips\AR1_TC_SAL.db', 'a')
file_objectTcDelete= open(r'C:\Users\crist\Desktop\satelite\scrips\TC_delete.txt', 'r')
a = file_object.readlines()
b = file_objectTcDelete.readlines()
c =[]
ii=0
while ii<len(a):
    s=a[ii]
    if s== inicioTc:
        inicioTcIndex = ii
    if s == finTc:
        print("estoy en la condicion de finTC")
        finTcIndex=ii
    ii+=1


for jj in b:
    ii = inicioTcIndex
    while ii < finTcIndex + 1 :
        if a[ii][4:11] == jj[0:7]:
            print("encontre una coincidencia")
            aux=list(a[ii])
            aux[0]="/"
            aux[1]="/"
            a[ii]="".join(aux)
            
        ii+=1


            
    
        
            

file_objectSal.writelines(a)


file_object.close()
file_objectSal.close()
file_objectTcDelete.close()

