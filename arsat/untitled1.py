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

# directorios de notebook de arsat
file_object = open(r'C:\Users\calanis\Desktop\SCC\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_APP_TEMP.DRW', 'r')
file_db = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TLM.db', 'rb')
file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\prueba123456.txt', 'a')

#directorio de mi notebook
# file_object = open(r'C:\Users\calanis\Desktop\SCC\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_APP_TEMP.DRW', 'r')
# file_db = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TLM.db', 'rb')
# file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\prueba123.txt', 'a')

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
            aux=aux[4:]
            
            if aux[:aux.find(" ")] == tm :
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
    aux = s[s.find("_")+1:]
    aux = aux[:aux.find("_")]
    return aux



identCord = "gp "

def buscarDescMimic (xm ,ym ,mimic):
    mylista =[]
    
    for ii in range(len(mimic)):
        
        if mimic[ii][:3] == identCord :
            xa,ya=obtenerxy(mimic[ii])
            
            if ym < (ya + 0.5) and ym > (ya - 0.5) :
                
                aux=mimic[ii+3] 
                if aux.find('"') > -1 :
                    aux=aux[aux.find('"')+1:]
                    aux=aux[:aux.find('"')]
                    if aux[:2] != "ww" :
                        mylista.append(dict(desc=aux,xref=abs(xm-xa)))
    
    return mylista
          
    
    
    
        



flag=0
for ii in range(0,len(mimic)):
    
    if mimic[ii][:8] == identTmCode:
        
        # b.append(mimic[ii])
        
        # b.append(mimic[ii+4])
        s = obtenerCodTm(mimic[ii])
        x,y=obtenerxy(mimic[ii+4])
        descdb=buscarDescTm(s, mydb)
        if flag==0:
            pepito=buscarDescMimic(x, y, mimic)
            flag=1
        
        auxs= s + "    " + str(x) + "     " + str(y) + "    " + descdb + '\n'
        file_salida.write(auxs)
        

file_object.close()
file_db.close()
file_salida.close()
