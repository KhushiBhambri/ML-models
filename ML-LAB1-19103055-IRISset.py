# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 20:53:47 2021

@author: KHUSHI
"""
import pandas as pd
from matplotlib import pyplot as plot
import math

def divide_data(train_data,test_data,DataSet):
    d1=[]
    d2=[]
    d3=[]
    for i in range (0,DataSet['species'].count()):
        if DataSet['species'].values[i]=='Iris-setosa':
            d1.append(i)
        elif DataSet['species'].values[i]=='Iris-versicolor':
            d2.append(i)
        elif DataSet['species'].values[i]=='Iris-virginica':
            d3.append(i)
            
    for i in range (0,int(len(d1)*0.7)):
        train_data.append(d1[i])
    for i in range (int(len(d1)*0.7),len(d1)):
        test_data.append(d1[i])
        
    for i in range (0,int(len(d2)*0.7)):
        train_data.append(d2[i])
    for i in range (int(len(d2)*0.7),len(d2)):
        test_data.append(d2[i])
        
    for i in range (0,int(len(d3)*0.7)):
        train_data.append(d3[i])    
    for i in range (int(len(d3)*0.7),len(d3)):
        test_data.append(d3[i])
    return train_data,test_data

def KNN(DataSet,test_data,train_data,k):
    dic={}   
    accurate=0
    
    for i in range (0,len(test_data)):                          
        sl=DataSet['sepal_length'][test_data[i]]
        sw=DataSet['sepal_width'][test_data[i]]
        pl=DataSet['petal_length'][test_data[i]]
        pw=DataSet['petal_width'][test_data[i]]
        for j in range(0,len(train_data)):
            SL=DataSet['sepal_length'][train_data[j]]-sl         
            SW=DataSet['sepal_width'][train_data[j]]-sw          
            PL=DataSet['petal_length'][train_data[j]]-pl
            PW=DataSet['petal_width'][train_data[j]]-pw 
            ans=SL*SL+SW*SW+PL*PL+PW*PW
            ans=math.sqrt(ans)                      
            dic[ans]=DataSet['species'][train_data[j]]
        c1=0
        c2=0
        c3=0     
        count=0
    
        for a in sorted(dic):
            if(count==k): break
            if(dic[a]=='Iris-setosa'): c1=c1+1
            if(dic[a]=='Iris-versicolor'): c2=c2+1
            if(dic[a]=='Iris-virginica'): c3=c3+1
            count=count+1
        maxi=max(c1,max(c2,c3))
        if(maxi==c1):
            if(DataSet['species'][test_data[i]]=="Iris-setosa"):
                accurate=accurate+1
        elif(maxi==c2):
            if(DataSet['species'][test_data[i]]=="Iris-versicolor"):
                accurate=accurate+1
        elif(maxi==c3):
            if(DataSet['species'][test_data[i]]=="Iris-virginica"):
                accurate=accurate+1
        dic.clear()  
    return accurate 

DataSet = pd.read_csv('IRIS_dataset.csv')
test_data=[]
train_data=[]
train_data,test_data=divide_data(train_data,test_data,DataSet)
xi=[]
yi=[]
print(" K   ACCURACY")
for k in range(1,100,2):  
    correct=0
    correct=KNN(DataSet,test_data,train_data,k)
    percnt=correct/len(test_data)*100
    print(" ",k,"   ",percnt)
    xi.append(k)
    yi.append(percnt)
    
plot.plot(xi,yi)
plot.xlabel("Value of k")
plot.ylabel("Accuracy")
plot.title("ACCURACY v/s K")
plot.show()