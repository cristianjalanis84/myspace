# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 11:26:29 2022

@author: crist
"""

from datetime import datetime
TM = "CTA0009"




fecha = datetime.now()
print(fecha)

dia = fecha.strftime("%A")

mes = fecha.strftime("%B")

anio = fecha.strftime("%Y")

hora = fecha.strftime("%X")

fecha_frt = fecha.strftime("%c")
print("********************************************************************")
print("*  " + fecha_frt)
print("Busqueda de la TM " + TM )
print("********************************************************************")

