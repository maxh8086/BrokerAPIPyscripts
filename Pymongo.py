#!/usr/bin/env python
# coding: utf-8

# In[ ]:


apikey = 'api_key'
username = 'username'
pwd = 'passowrd'


# In[ ]:


import pandas as pd
from smartapi import SmartConnect
obj=SmartConnect(api_key=apikey)

data= obj.generateSession(username,pwd)
data['data']['exchanges']


# In[ ]:


def getData(obj, token,symbolName):
    historicParam={
            "exchange": "NSE",
            "symboltoken": token,   #3045 SBIN      HDFC 1330
            "interval": "ONE_MINUTE",
            "fromdate": "2022-01-01 09:15", 
            "todate": "2022-03-10 15:30"
            }
            
        
    res_json =obj.getCandleData(historicParam)
    columns = ['timestamp','open','high','low','close','volume']
    df = pd.DataFrame(res_json['data'], columns=columns)
    df['timestamp'] = pd.to_datetime(df['timestamp'],format = '%Y-%m-%dT%H:%M:%S')
    df['symbol'] = symbolName
   
    return df


# In[ ]:


getData(obj,1330,'HDFC')


# In[ ]:





# In[ ]:





# In[ ]:


pip install pymongo


# In[ ]:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["demoDatabase"]


# In[ ]:


myclient.list_database_names()


# In[ ]:


ohlcTable = mydb["historicalData"]


# In[ ]:


datadf = getData(obj,3045,'SBIN')
datadf


# In[ ]:


ohlcTable.insert_many(datadf.to_dict('records'))


# In[ ]:


pd.DataFrame(list(ohlcTable.find()))


# In[ ]:


pd.DataFrame(list(ohlcTable.find({'symbol':'SBIN'})))

