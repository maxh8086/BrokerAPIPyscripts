#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install breeze-connect==1.0.12


# In[ ]:


from breeze_connect import BreezeConnect
session_key = 'session_key'
api_key = 'your_api_key'
api_secret = 'your_secret_key'

breeze = BreezeConnect(api_key=api_key)

breeze.generate_session(api_secret=api_secret,session_token=session_key)


# In[ ]:


breeze.get_funds()


# In[ ]:


import pandas as pd
res = breeze.get_historical_data(interval="1minute",
                            from_date= "2019-03-15T07:00:00.000Z",
                            to_date= "2019-03-28T07:00:00.000Z",
                            stock_code="CNXBAN",
                            exchange_code="NFO",
                            product_type="options",
                            expiry_date="2019-03-28T07:00:00.000Z",
                            option_type="call",
                            strike_price="29100")

histdf = pd.DataFrame(res['Success'])
histdf


# In[ ]:





# In[ ]:


tokendf = pd.read_csv('https://traderweb.icicidirect.com/Content/File/txtFile/ScripFile/StockScriptNew.csv')
tokendf


# In[ ]:


listSymbols = tokendf[tokendf.EC == 'NFO'].NS.unique()
listSymbols


# In[ ]:


tokendf[tokendf.NS == 'NIFTY BANK']

