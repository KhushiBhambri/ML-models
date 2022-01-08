# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 14:07:38 2021

@author: KHUSHI
"""

import pandas as pd
import matplotlib.pyplot  as plt
import math

df=pd.read_csv("train.csv")
x=[]
y=[]
x=df.x
y=df.y


xmean=x.mean()
ymean=y.mean()
df['diff_x']=xmean-x
df['diff_y']=ymean-y
df['diff']=df['diff_x']*df['diff_y']
df['sqdiff_x']=df['diff_x']**2
sum1=df['diff'].sum()
sum2=df['sqdiff_x'].sum()

m=sum1/sum2  #slope

c=ymean-xmean*m  #intercept    as per y=m*x+c
def predict(value):
    return m*value+c

df2=pd.read_csv("test.csv")
df2['predicted']=predict(df2['x'])
df2['error']=df2['y']-df2['predicted']
df2['sqerror']=df2['error']**2
sumerror=df2['sqerror'].sum()
sumerror
n=len(df2)


rmserror=math.sqrt(sumerror);
rmserror=rmserror/n
print(df)

plt.scatter(df2.x,df2.y,color='yellow')
plt.plot(x,m*x+c,color='black')
plt.xlabel("X")
plt.ylabel("Y")

print('root mean square error is: ' ,rmserror)