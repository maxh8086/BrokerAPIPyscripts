#!/usr/bin/env python
# coding: utf-8

# In[ ]:


apikey = 'api_key'
username = 'username'
pwd = 'password'


# In[ ]:


from smartapi import SmartConnect

obj=SmartConnect(api_key=apikey)
data = obj.generateSession(username,pwd)
#print(data)
refreshToken= data['data']['refreshToken']
res = obj.getProfile(refreshToken)
print(f"Angel Logged in {res['data']['exchanges']}")


# In[ ]:


import pandas as pd
import requests
url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
d = requests.get(url).json()
token_df = pd.DataFrame.from_dict(d)
token_df['expiry'] = pd.to_datetime(token_df['expiry']).apply(lambda x: x.date())
token_df = token_df.astype({'strike': float})

bnf = token_df[(token_df['name'] == 'NIFTY') & (token_df['instrumenttype'] == 'FUTIDX') ]
bnfSymbol = bnf.iloc[0]


# In[ ]:


bnfSymbol


# In[ ]:


def placeorder(obj,token,symbol,qty,buy_sell,exch_seg):
    try:
        orderparams = {
            "variety": 'NORMAL',
            "tradingsymbol": symbol,
            "symboltoken": token,
            "transactiontype": buy_sell,
            "exchange": exch_seg,
            "ordertype": 'MARKET',
            "producttype": "INTRADAY",
            "duration": "DAY",
            "price": 0,
            "squareoff": "0",
            "stoploss": "0",
            "quantity": qty,
            "triggerprice":0
            }
        print(orderparams)
        orderId=obj.placeOrder(orderparams)
        print(f"The order id is: {orderId}")
        return orderId
    except Exception as e:
        print(f"Order placement failed: {e}")


# In[ ]:


import math
tradeLot = 200
MAX_LOTLIMIT = 56
ordernum = math.floor(tradeLot/MAX_LOTLIMIT)
lastOrder =  tradeLot%MAX_LOTLIMIT 
lotQty = int(bnfSymbol['lotsize'])
orderList = []
for i in range(0,ordernum):
    print(f'Order No {i+1}')
    orderid= placeorder(obj,bnfSymbol['token'],bnfSymbol['symbol'],MAX_LOTLIMIT*lotQty,'BUY',bnfSymbol['exch_seg'])
    orderList.append(orderid)

if lastOrder > 0:
    print(f'Placing Last order {lastOrder}')
    placeorder(obj,bnfSymbol['token'],bnfSymbol['symbol'],lastOrder*lotQty,'BUY',bnfSymbol['exch_seg'])
    orderList.append(orderid)

orderList


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




