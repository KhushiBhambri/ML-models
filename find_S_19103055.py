# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import csv
with open("find_S.csv",'r')as f:
    reader=csv.reader(f)
    data=list(reader)



h=['0','0','0','0','0','0']

for row in data :
    if row[-1]=='TRUE':
        j=0
        for col in row :
            if col!='TRUE':
                if col!=h[j] and h[j]=='0':
                    h[j]=col
                elif col!=h[j] and h[j]!='0':
                    h[j]='?'
            j=j+1

            
print("maximally specific hypothesis -  ",h)
    
           
    