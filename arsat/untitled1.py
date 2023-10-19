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
import pandas as pd

identTmCode = "   5 0 1"
b=[]

# directorios de notebook de arsat
file_object = open(r'C:\Users\calanis\Desktop\SCC_V4795_full\mimics.ar2\AIT-Proc\AR2_PROPULSION_SS_MON_TEMP_1.DRW', 'r')#TVAC\
file_db = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_TLM.db', 'rb')
file_salida = open(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\AR2_PROPULSION_SS_MON_TEMP_1.txt', 'a')
df_tlm = pd.read_excel(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\thermal_ar2.xlsx',usecols=("A")) # columna A : codigo de TM , columna B : descripcion , columna C : temperatura codigo del sensor
df_tlm_desc = pd.read_excel(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\thermal_ar2.xlsx',usecols=("B"))
df_tlm_sensorcod = pd.read_excel(r'C:\Users\calanis\Documents\GitHub\myspace\arsat\thermal_ar2.xlsx',usecols=("C"))
# L1T0020 "CM-N TRP 1TE1-01A mon temp" Temperature (°C) of N-M01
#directorio de mi notebook

#file_object = open(r'C:\Users\crist\Desktop\SCC\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_PROP_TUBING.DRW', 'r')
# file_object = open(r'C:\Users\crist\Desktop\SCC\mimics.ar2\AIT-Proc\TVAC\AR2_TVAC_SATELLITE_APP_TEMP.DRW', 'r')
# file_db = open(r'C:\Users\crist\Desktop\myspace\arsat\AR2_TLM.db', 'rb')
# file_salida = open(r'C:\Users\crist\Desktop\myspace\arsat\pruebaa.txt', 'a')
# df_tlm = pd.read_excel(r'C:\Users\crist\Desktop\myspace\arsat\thermal_ar2.xlsx',usecols=("A"))# columna A : codigo de TM , columna B : descripcion , columna C : temperatura codigo del sensor
# df_tlm_desc = pd.read_excel(r'C:\Users\crist\Desktop\myspace\arsat\thermal_ar2.xlsx',usecols=("B"))
# df_tlm_sensorcod = pd.read_excel(r'C:\Users\crist\Desktop\myspace\arsat\thermal_ar2.xlsx',usecols=("C"))

mimic= file_object.readlines()
mydb = file_db.readlines()
# tmSohCod = df_tlm.readlines()
# tmSohDesc = df_tlm_desc.readlines()
# tmSohSensorDesc = df_tlm_sensorcod.readlines()
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

#Obtiene las coordenadas X Y de un "gp 4.9451518119490698e+000 1.2273261508325172e+002"
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

def buscarDescMimic (xm ,ym ,mimic,descPos,s):
    mylista =[]
    
    for ii in range(len(mimic)):
        
        if mimic[ii][:3] == identCord :
            xa,ya=obtenerxy(mimic[ii])
            aux=mimic[ii+3]
            if ya < (ym + 0.7) and ya > (ym - 0.7) and aux.find('"') > -1:
    
                aux=aux[aux.find('"')+1:]
                if aux.find('"') == -1:
                    aux=aux[:aux.find('\n')]
                else:
                    aux=aux[:aux.find('"')]
                if aux[:2] != "ww" and aux.find(s) == -1 :
                    mylista.append(dict(desc=aux,xref=(xm-xa)))
    tamanio=len(mylista)
    #index=0
    xx=500.0
    if tamanio==0:
        descripcion="No se encontro"
    elif tamanio == 1:
        descripcion=mylista[0]['desc']
    elif tamanio > 1 :
        for jj in range(0,tamanio):
            if descPos == "Right":
                if abs(mylista[jj]['xref']) < xx :
                    descripcion=mylista[jj]['desc']
                    xx=abs(mylista[jj]['xref'])
            elif descPos == "Left":
                if (mylista[jj]['xref']) > 0  and abs(mylista[jj]['xref'])<xx :
                    descripcion=mylista[jj]['desc']
                    xx=abs(mylista[jj]['xref'])
                    
    return descripcion
 

# tmSohCod = file_db.readlines()
# tmSohDesc = file_db.readlines()
# tmSohSensorDesc = file_db.readlines()         
def buscarTmSoh(descTm):
    tmdescsoh="____"
    tmsensorsoh="____"
    tmcode="____"
    for jj in range(0,int(len(df_tlm))):
        if df_tlm.loc[jj].to_string(index=False) == descTm :
            tmdescsoh = df_tlm_desc.loc[jj].to_string(index=False)
            tmsensorsoh = df_tlm_sensorcod.loc[jj].to_string(index=False)
            tmcode=df_tlm.loc[jj].to_string(index=False)
            
    return tmdescsoh,tmsensorsoh,tmcode
    
    
        



flag=0
ss="{:<12}".format("TM mimic") +"{:70}".format("Descripcion de la mimic") + "{:45}".format("Descripcion de la base de datos")  +"{:12}".format("TM cod SOH")  +"{:45}".format("Descripcion de la tm en el SOH") + "{:50}".format("Descripcion del sensor en el SOH") + '\n'
file_salida.write(ss)
for ii in range(0,len(mimic)):
    
    if mimic[ii][:8] == identTmCode:   #identTmCode = "   5 0 1"
        
        # b.append(mimic[ii])
        
        # b.append(mimic[ii+4])
        s = obtenerCodTm(mimic[ii])    #De la lin actual que empieza con "   5 0 1" obtengo el codigo de la tm 
        x,y=obtenerxy(mimic[ii+4])     #4 lin hacia abajo se obtiene las cordenadas X Y de la tm
        descdb=buscarDescTm(s, mydb)    #desde la base de datos
        
        pepito=buscarDescMimic(x, y, mimic,"Right",s)
        
        tmdescsoh,tmsensorsoh,tmcode=buscarTmSoh(s)

        auxs= "{:<12}".format(s) + "{:70}".format(pepito) + "{:45}".format(descdb)  +"{:12}".format(tmcode)  +"{:45}".format(tmdescsoh) + "{:50}".format(tmsensorsoh) + "{:<22}".format(str(x)) + "{:<22}".format(str(y))+'\n' #+ "    " + str(x) + "     " + str(y) 
        file_salida.write(auxs)
        

file_object.close()
file_db.close()
file_salida.close()
