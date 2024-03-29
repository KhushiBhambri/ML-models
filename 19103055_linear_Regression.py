# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 22:12:23 2021

@author: KHUSHI
"""

import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np
train_data = pd.read_csv('train.csv')

m=0
c=0
# y=mx+c

#  m=sum((x-mean(x))*(y-mean(y)))/(sum(x-mean(x)))
# c = mean(y)-m*(mean(x))
sx=0
sy=0

def mean(train_data):
    sx=0
    sy=0
    n=len(train_data)
    for i in range(n):
        sx=sx+train_data['x'][i]
        sy=sy+train_data['y'][i]
    return sx/n,sy/n    

def get_num_deno(sx,sy,data):
    num=0
    deno=0
    n=len(train_data)
    for i in range(n):
        num = (train_data['x'][i]-sx)*(train_data['y'][i]-sy)
        deno = (train_data['x'][i]-sx)*(train_data['x'][i]-sx)
    return num,deno   

def get_value(train_data):
    n = len(train_data)
    lx = []
    for i in range(n):
        lx.append(train_data['x'][i])
    return lx

def accuracy(c,m,data):
    n = len(data)
    x=0
    y=0
    p=0
    acc=0
    y_mean=0
    for i in range(n):
       x = data['x'][i]
       y = data['y'][i]
       p = c + m*x
       y_mean = y_mean + (y-p)
    y_mean = y_mean/n
    for i in range(n):
        # x = data['x'][i]
        y = data['y'][i]
        # p = c + m*x
        acc = acc + (y-y_mean)*(y-y_mean)
    return math.sqrt(acc)
    
    
    
sx,sy=mean(train_data)
num,deno = get_num_deno(sx,sy,train_data)
lx = get_value(train_data)

m=num/deno
c=sy-m*sx

# prediction time

test_data = pd.read_csv('test.csv')
n= len(test_data)
x = []
y = []
# print(lx)
lx = np.array(lx)
# print(lx)
for i in range(n):
    x.append(test_data['x'][i])
    y.append(test_data['y'][i])

plt.scatter(x,y,color='black')
plt.plot(lx,c+m*lx,color='red')
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")


acc=accuracy(c,m,test_data)
acc = acc/n
print("Root mean square error of model : ",acc)