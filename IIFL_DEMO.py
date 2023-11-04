#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Connect import XTSConnect


# In[ ]:


import pandas as pd
from datetime import datetime,date


# In[ ]:


#Market API
API_KEY_M = ""
API_SECRET_M = ""
source = "WEBAPI"


# In[ ]:


xtm = XTSConnect(API_KEY_M, API_SECRET_M, source)
xtm.marketdata_login()


# In[ ]:


exchangesegments = [ xtm.EXCHANGE_NSEFO]
response = xtm.get_master(exchangeSegmentList=exchangesegments)
response


# In[ ]:


with open("FO.txt", "w") as file1:
    file1.write(response['result'])


# In[ ]:


masterdf = pd.read_csv('FO.txt',sep='|',usecols=range(19),header = None,low_memory = True)
masterdf


# In[ ]:


masterdf.columns  = ["ExchangeSegment","ExchangeInstrumentID","InstrumentType","Name","Description","Series","NameWithSeries","InstrumentID","PriceBand.High","PriceBand.Low","FreezeQty","TickSize","LotSize","Multiplier","UnderlyingInstrumentId","UnderlyingIndexName","ContractExpiration","StrikePrice","OptionType"]
masterdf


# In[ ]:


masterdf['ContractExpiration'] = pd.to_datetime(masterdf['ContractExpiration']).apply(lambda x: x.date())   
masterdf


# In[ ]:


masterdf[(masterdf.Name == 'TCS') & (masterdf.Series == 'OPTSTK') & (masterdf.StrikePrice == 2000) &  (masterdf.ContractExpiration == date(2023,4,27)) &  (masterdf.OptionType == 3)]


# In[ ]:


exchangesegments = [ xtm.NSECM]
responseEQ = xtm.get_master(exchangeSegmentList=exchangesegments)
responseEQ


# In[ ]:


with open("CM.txt", "w") as file1:
    file1.write(responseEQ['result'])


# In[ ]:


masterEQdf = pd.read_csv('CM.txt',sep='|',usecols=range(14),header = None,low_memory = True)
masterEQdf


# In[ ]:


masterEQdf[masterEQdf[4]=='TCS-EQ']


# In[ ]:


API_KEY = ""
API_SECRET = ""
source = "WEBAPI"


# In[ ]:


xt = XTSConnect(API_KEY, API_SECRET, source)
response = xt.interactive_login()
response


# In[ ]:


response = xt.place_order(
    exchangeSegment=xt.EXCHANGE_NSEFO,
    exchangeInstrumentID=44102,
    productType=xt.PRODUCT_MIS,
    orderType=xt.ORDER_TYPE_MARKET,
    orderSide=xt.TRANSACTION_TYPE_BUY,
    timeInForce=xt.VALIDITY_DAY,
    disclosedQuantity=0,
    orderQuantity=175,
    limitPrice=0,
    stopPrice=0,
    orderUniqueIdentifier="dft",
    clientID="1")
print("Place Order: ", response)


# In[ ]:


xt.get_order_book()

