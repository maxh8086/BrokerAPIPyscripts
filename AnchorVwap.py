#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import pandas_ta as ta
from datetime import datetime, timedelta,date


# In[ ]:


help(ta.vwap)


# In[ ]:


df = pd.read_csv('SBI_OHLC.csv')
df["date"] = pd.to_datetime(df["date"])
df


# In[ ]:


df.set_index('date',inplace = True)
df['vwap'] = ta.vwap(df.high, df.low, df.close, df.volume,anchor ='M')
df.reset_index(inplace = True)
df


# In[ ]:


def getvwapFromAnchorDate(df,anchorDate = None):
    if anchorDate is not None:
        df = df[df.date.dt.date >= anchorDate]
    vol = df['volume'].values
    typPrice = ((df['low'] + df['close'] + df['high'])/3).values
    df['vwap'] = (typPrice * vol).cumsum() / vol.cumsum()
    return df 

anchorDate = date(2022,7,5)
sbidf = getvwapFromAnchorDate(df,anchorDate)


# In[ ]:


sbidf

