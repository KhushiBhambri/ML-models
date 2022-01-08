#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


import os
os.getcwd()

data= pd.read_csv("IRIS_dataset.csv")

data.head()

from sklearn.preprocessing import LabelEncoder
g=data["species"]
le= LabelEncoder()
data["species"]=LabelEncoder().fit_transform(g)

data["species"].value_counts()

data_sample = data.sample(frac =1)

train_size = int(0.7 *150) 

train = data_sample[:train_size]

test =data_sample[train_size:]


train.shape


# In[15]:


test.shape


# In[16]:


x_train=train.iloc[:,:4]
y_train=train.iloc[:,-1:]


# In[17]:


x_train.head()


# In[18]:


y_train.head()


# In[19]:


y_train.value_counts()


# In[20]:


x_train.shape


# In[21]:


x1=x_train.iloc[:,0]


# In[22]:


x1


# In[23]:


x11=x1.to_numpy()
x11


# In[24]:


x11[0]


# In[25]:


x22=x_train.iloc[:,1].to_numpy()


# In[26]:


x33=x_train.iloc[:,2].to_numpy()


# In[27]:


x44=x_train.iloc[:,3].to_numpy()
x44


# In[28]:


y11=y_train.to_numpy()
y11[0]==1


# In[41]:


def Average(lst): 
    return sum(lst) / len(lst) 

import statistics
    #mean1=Average(ty);


# In[65]:



#let k be 2

#pehle ek variable ka sabhi var se distance nikaala and uske baad k ke acc 3 min values ka y value ka mode nikaala agar woh match kr gya toh f->1 else f->0

k=2
lx=[]
ly=[]

f=[]
y_pred=[]
ty=[]
for i in range(0,105):
    for j in range(0,104):
        if(i==j):
            j=j+1
        dis=np.sqrt((np.square(x11[i]-x11[j]))+(np.square(x22[i]-x22[j]))+(np.square(x33[i]-x33[j]))+(np.square(x44[i]-x44[j])))
        lx.append((dis))
        ly.append(y11[j])
    #print(lx)
    
    for l in range(0,k):
        minpos = lx.index(min(lx)) 

        t=ly[minpos]
        ty.append(int(t))
        lx.pop(minpos)
        ly.pop(minpos)
    
    #ty
    lx.clear()
    
    
    m1=statistics.mode(ty)
    
    
    if(y11[i]==m1):
        f.append(1)
    else:
        f.append(0)
        
    y_pred.append(m1)
    


# In[66]:


#i=0
#j=1
#dis=np.sqrt((np.square(x11[i]-x11[j]))+(np.square(x22[i]-x22[j]))+(np.square(x33[i]-x33[j]))+(np.square(x44[i]-x44[j])))
#dis


# In[67]:


#l=[3, 3, 1, 2, 3, 3, 2, 2, 3, 3, 0, 2, 3, 0, 3, 0, 2, 0, 0, 2, 0, 1, 0, 2, 2, 0, 1, 3, 1, 3, 2, 0, 3, 3, 0, 0, 2, 0, 1, 0, 2, 3, 1, 2, 1, 1, 3, 0, 2, 3, 3, 1, 1, 3, 0, 2, 2, 1, 3, 1, 1, 3, 2, 1, 0, 2, 1, 3, 3, 1, 0, 1, 3, 2, 1, 2, 1, 1, 0, 1, 0, 2, 2, 1, 0, 1, 1, 2, 2, 0, 2, 1, 3, 3, 2, 0, 2, 2, 0, 0, 2, 2, 3, 2]

#minpos = l.index(min(l)) 
#m1=statistics.mode(l)


# In[69]:


from sklearn.neighbors import KNeighborsClassifier
k=KNeighborsClassifier()


# In[70]:


k.fit(x_train,y_train)


# In[71]:


y_pred2=k.predict(x_train)


# In[72]:


from sklearn.metrics import accuracy_score
accuracy_score(y_train,y_pred2)


# In[68]:


sum(f)


# In[73]:


y_pred2


# In[74]:


y_pred


# In[ ]:




