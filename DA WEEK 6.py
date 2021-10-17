#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
# plt.plot([1,2,3,4],[2,3,5,2],':^r')
# plt.show()

x = np.linspace(-10,10,100)
def sigmoid(a):
    y = 1/(1+np.exp(-a))
    return y
C=sigmoid(x)

plt.plot(x,C,color='red')
plt.ylabel('sigmoid')
plt.xlabel('x')
plt.title('sigmoid function')
plt.show()




# In[2]:


import pandas as pd
fb=pd.read_csv('fb.csv')
a=pd.DatetimeIndex(fb.date).week

A=fb.groupby(a).mean()

A['difference']=A.high-A.low
B=A['difference'].plot(kind='line',y='diference',title='Difference between weekly max price and weekly min price')
B.set_xlabel("week")
B.set_ylabel("difference")



# In[3]:


fb['difference']=fb.high-fb.low
fb.plot(x='volume',y='difference',kind='scatter',title='relationship btw volume and diference')#logx=True,alpha=0.25)


# In[4]:


df=pd.read_csv('EQ.csv')

A=df[df['place'].str.contains('Indonesia')]
df.boxplot(column='mag',by='magType',figsize=(10,10))


# In[5]:


df['date'] = pd.to_datetime(df['time'], unit='ms')
df['MM-DD'] = df['date'].dt.strftime('%m-%d')
B=df[df['place'].str.contains('Indonesia')]

C=B.groupby('MM-DD').count()

C.plot.bar(y='tsunami')


# In[ ]:




