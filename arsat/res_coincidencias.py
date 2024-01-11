# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 14:08:23 2023

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
    while jj < len(a):
        cont_tm = 0
        cont_iden_fop = 0
        if a[jj][:4] == iden_fop:
            
            cont_iden_fop += 1
            kk=jj
            
            while  kk < len(a) and cont_iden_fop < 2 :
                
                if a[kk][:4] == iden_tm:
                    cont_tm += 1
                    print('cont' + '\n')
                kk += 1
                if kk != len(a) and a[kk] == iden_fop:
                    cont_iden_fop += 1
            if cont_tm > 0 :
                for ll in range(jj,kk):
                    file_sal.write(a[ll])
                    print('write' + '\n')
            jj = kk - 1
        else :
            jj += 1
            
    file_ent.close()
    file_sal.close()
    
            
        
        