#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
from datetime import datetime

df = pd.read_csv('https://api.kite.trade/instruments')
df = df[(df.exchange == 'NFO') & (df.name == 'NIFTY')  & (df.instrument_type == 'FUT')]

def getMonthlyExp(df, i = 0):
    df['expiry'] = pd.to_datetime(df['expiry']).apply(lambda x: x.date())
    df.drop(df[df.expiry <datetime.now().date()].index, inplace=True)
    weekly_expiry = df['expiry'].unique().tolist()
    weekly_expiry.sort()
    return weekly_expiry[i]


# In[27]:


getMonthlyExp(df,0)


# In[14]:


df = pd.read_csv('https://api.kite.trade/instruments')
df


# In[15]:


df = df[(df.exchange == 'NFO') & (df.name == 'NIFTY')  & (df.instrument_type == 'FUT')]
df


# In[16]:


df['expiry'].unique().tolist()





