#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user        = 'FG6703'
pwd         = '1234893'
vc          = 'FG6703_U'
app_key     = '54da64GHDdjbcdjddbcd3bc9498d0411a779d'
token       = 'VNBXSBJXSNL347BT2QIKM6NPH2Q427'


# In[14]:


from NorenRestApiPy.NorenApi import  NorenApi
import pyotp



class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
        global api
        api = self

api = ShoonyaApiPy()      

ret = api.login(userid=user, password=pwd, twoFA=pyotp.TOTP(token).now(), vendor_code=vc, api_secret=app_key, imei='dfsghwd6eydbef8hdnk')

api.get_limits()


# In[15]:


import pandas as pd
from datetime import datetime,date
symbolDf = pd.read_csv('https://shoonya.finvasia.com/NFO_symbols.txt.zip')
symbolDf['Expiry'] = pd.to_datetime(symbolDf['Expiry']).apply(lambda x: x.date())   
symbolDf


# In[16]:


ocdf = symbolDf[(symbolDf.Symbol == 'BANKNIFTY') & (symbolDf.Expiry == date(2022,10,13)) ]
ocdf


# In[18]:


api.get_quotes(exchange='NSE', token='26009')


# In[24]:


Pedf =ocdf[ocdf.OptionType == 'PE'] 
Pedf


# In[25]:


ltp = 220
strikeList = []
for i in Pedf.index:
    strikeInfo = Pedf.loc[i]
    res = api.get_quotes(exchange='NFO', token=str(strikeInfo.Token))
    res = {'tsym': res['tsym'], 'lp': float(res['lp']),'lotSize':strikeInfo.LotSize,'token':res['token']}
    strikeList.append(res)
strikedf = pd.DataFrame(strikeList)
strikedf.sort_values(by = 'lp',inplace = True)
strikedf['diff'] = abs(strikedf['lp'] - ltp)
strikedf.sort_values(by = 'diff',inplace = True)
strikedf.iloc[0]


