# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:33:59 2023

@author: calanis
"""

import os
import sys
print(os.path.dirname(sys.executable)+'\Scripts\\')


contenido = os.listdir(r'C:\Users\calanis\Desktop\info sat\scrips\fops\\')

iden_tm  = '....'
iden_fop = '0841'
cont_tm = 0
for ii in contenido:
    file_ent = open(r'C:\Users\calanis\Desktop\info sat\scrips\fops\\' + ii,'r')
    file_sal = open(r'C:\Users\calanis\Desktop\info sat\scrips\fops\\' + ii[:-4] + '_resumen.txt','a')
    a = file_ent.readlines()
    jj = 0
    primer_iden_fop = False
    #seg_iden_fop = False
    while jj < len(a):
        if a[jj][:4] == iden_fop and primer_iden_fop == False:
            kk = jj
            primer_iden_fop = True
        if a[jj][:4] == iden_fop and primer_iden_fop == True:
            
            if jj > kk :
                for ll in range(kk,jj):
                    if a[ll][:4] == iden_tm:
                        cont_tm += 1
                if cont_tm > 0:
                    for ll in range(kk,jj):
                        file_sal.write(a[ll])
                    cont_tm = 0
                primer_iden_fop = False
                jj -= 1
        jj += 1
    file_ent.close()
    file_sal.close()