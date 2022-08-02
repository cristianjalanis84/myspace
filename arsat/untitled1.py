# -*- coding: utf-8 -*-
"""
Created on Fri May  6 15:36:54 2022

@author: crist
"""

# s="  Holiss  "
# s2="\tHoliss\t"
# s3="holiss"
# print(s)
# print(s2)
# tc="CLF0007"

# aux="{:>11}".format(tc)

identTmCode = "   5 0 1"
b=[]


file_object = open(r'C:\Users\crist\Desktop\SCC_V4795_full\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_APP_TEMP.DRW', 'r')
file_db = open(r'C:\Users\crist\Desktop\satelite\scrips\AR2_TLM.db', 'rb')
file_salida = open(r'C:\Users\crist\Desktop\satelite\scrips\prueba123.txt', 'a')
mimic= file_object.readlines()
mydb = file_db.readlines()

def buscarDescTm(tm , base):
    print("holiss")
    
    identBdTm = "&def_param {"
    auxDesc="No encontre nada"
    for ii in range(len(base)):
        # aux2 = base[ii][:12]
        aux2=str(base[ii][:12])
        if aux2[2:14] ==identBdTm:
            
            # aux = base[ii+1]
            aux=str(base[ii+1])
            if aux[4:11] == tm :
                # index = aux.find('"')
                # aux=aux[index+1:]
                aux=aux[aux.find('"')+1:]
                # index=aux.find('"')
                # aux=aux[:index]
                auxDesc=aux[:aux.find('"')]
                # auxDesc=aux
                break
        
    return auxDesc
#gp 4.9451518119490698e+000 1.2273261508325172e+002

def obtenerxy (s):
    auxx = s[s.find(" ") + 1:s.find("e")]
    expx = s[s.find("e")+4]
    expx = float (expx)
    auxx = float (auxx)
    aux = s [s.find("e")+1:]
    auxy = aux[aux.find(" ") + 1:aux.find("e")]
    auxy = float(auxy)
    expy = aux[aux.find("e")+4]
    expy = float(expy)
    return auxx*(10**expx), auxy*(10**expy)


# 5 0 17 "AR2TLM_OIT0124_A\000"

def obtenerCodTm (s):
    return s[s.find("_")+1:s.find("_")+8]
    
        




for ii in range(0,len(mimic)):
    
    if mimic[ii][:8] == identTmCode:
        
        # b.append(mimic[ii])
        
        # b.append(mimic[ii+4])
        s = obtenerCodTm(mimic[ii])
        x,y=obtenerxy(mimic[ii+4])
        descdb=buscarDescTm(s, mydb)
        auxs= s + "    " + str(x) + "     " + str(y) + "    " + descdb + '\n'
        file_salida.write(auxs)
        

file_object.close()
file_db.close()
file_salida.close()
