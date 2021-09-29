#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
nyc=pd.read_csv('nyc_weather_2018.csv')
ws=pd.read_csv('weather_stations.csv')
data=nyc.merge(ws.rename(dict(id='station'),axis=1),on='station')

#data[(data.datatype == "SNOW")&(data.name.str.contains("NJ US"))]
#result=data.query('datatype=="SNOW" and name.str.contains("NJ US")',engine='python').groupby('station')

snow=data[data.datatype=="SNOW"]
station=data[data.name.str.contains("NJ US")]
a=snow.merge(station, how='inner').drop_duplicates('station')
a.elevation.mean()


# In[2]:


import pandas as pd
fb=pd.read_csv('fb.csv')
B=fb.assign(change= lambda x: x.volume.pct_change())
B.sort_values(by='change',ascending=True)
B.head(5)


# In[3]:


import pandas as pd
df=pd.read_csv('/Users\Admin\Downloads\earthquakes.csv')
data=df[df.magType =='ml']
data=data.assign(col=pd.cut(data.mag,[0,1,2,3,4,5],labels=['q1','q2','q3','q4','q5']))
data.col.value_counts()


# In[4]:


import pandas as pd
import numpy as np
data=pd.read_csv('weather_by_station.csv')
snow=data[data.datatype=="SNOW"]
a=pd.DatetimeIndex(snow.date).month
pd.crosstab(index=snow.station,columns=a,colnames=['month'],values=snow.value,aggfunc=np.mean)
pd.crosstab(index=snow.station,columns=a,colnames=['month'])


# In[ ]:




