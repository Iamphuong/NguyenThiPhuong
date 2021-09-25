#!/usr/bin/env python
# coding: utf-8

# # BAI 1

# In[2]:


import pandas as pd
#1 
fb=pd.read_csv('fb.csv')
amazon=pd.read_csv('amzn.csv')
netflix=pd.read_csv('nflx.csv')
google=pd.read_csv('goog.csv')
apple=pd.read_csv('aapl.csv')

#2
fb['ticker']='FB'
amazon['ticker']='AMZN'
netflix['ticker']='NFLX'
google['ticker']='GOOG'
apple['ticker']='AAPL'

#3
Faang= pd.concat([fb,amazon,google,apple], axis=0, join='inner')
Faang.head(2)


# In[3]:


#4
data=pd.DataFrame.to_csv(Faang,'faang.csv')
#5
Faang=Faang.assign(date=lambda x: pd.to_datetime(x.date),volume=lambda x: x.volume.astype('int'))
Faang.sort_values(by=['date','ticker'],ascending=[True,False])


# In[4]:


#6
Faang.sort_values(by=['volume'],ascending=[True]).head(7)


# # BAI 2

# In[60]:


import pandas as pd
#1
covid=pd.read_csv('covid19_cases.csv')
#2
covid['date']= pd.to_datetime(covid.dateRep)


# In[47]:


#3
a=covid.set_index('date',inplace=True)
covid.sort_values(by='date',ascending=True)


# In[62]:


#4
covid['countriesAndTerritories']=covid['countriesAndTerritories'].str.replace('United_States_of_America','USA').str.replace('United_Kingdom','UK')
#5
covid['countriesAndTerritories']=covid['countriesAndTerritories'][covid['countriesAndTerritories'].str.contains('Argentina|Brazil|China|Colombia|India|Italy|Mexico|Peru|Russia|Spain|Turkey|UK|USA')]
covid.set_index(['countriesAndTerritories'],inplace=True)
covid.sort_index(axis=0)['Argentina':'USA']


# In[19]:


#6
pivot=covid.pivot(index='date', columns='countriesAndTerritories',values='cases')
pivot.fillna(0)


# In[ ]:




