# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd

data = pd.DataFrame(data=pd.read_csv('dataset.csv'))
examples = np.array(data.iloc[:,0:-1])
targetconcept = np.array(data.iloc[:,-1])

##targetconcept=data[1];

print(targetconcept)
#print(examples)


specifich = ["0" for i in range(len(examples[0]))]
print("Initialization of specifich and generalh")
print("specifich: ",specifich)
generalh = [["?" for i in range(len(specifich))] for i in range(len(specifich))]

for i, h in enumerate(examples):
   if targetconcept[i] == "Qualify":
      for x in range(len(specifich)):
         if h[x] != specifich[x]:
             if(specifich[x] == "0"):
                 specifich[x]=h[x]
             else:
                 specifich[x] = '?'
                 generalh[x][x] = '?'
   if targetconcept[i] == "Disqualify":
            for x in range(len(specifich)):
                if h[x] != specifich[x]:
                    generalh[x][x] = specifich[x]
                else:
                    generalh[x][x] = '?'
                    
print("\nSteps  ",i+1)

indices = [i for i, val in enumerate(generalh) if val == ['?', '?', '?']]

for i in indices:
 generalh.remove(['?', '?', '?'])


print("\nFinal Specifich:", specifich, sep="\n")
print("Final Generalh:",generalh, sep="\n")