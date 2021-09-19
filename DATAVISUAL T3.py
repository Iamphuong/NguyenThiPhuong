#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
df=pd.read_csv('/Users\Admin\Downloads\earthquakes.csv')

#1
df.loc[(df.magType =='ml') & (df.type == 'explosion')]['type'].count()


# In[2]:


#2
df[(df['place'].str.contains('Alaska'))&~(df['place'].str.contains(r'\d{3,}'))]['mag'].mean()

