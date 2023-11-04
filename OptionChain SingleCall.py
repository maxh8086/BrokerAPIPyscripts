#!/usr/bin/env python
# coding: utf-8

# 
# 
# 
# 
# 
# 
# 

# In[ ]:


pip install stocknotebridge


# In[ ]:


from snapi_py_client.snapi_bridge import StocknoteAPIPythonBridge
import json
import pandas as pd


# In[ ]:


#pip uninstall  websocket-client
#pip install  websocket-client


# In[ ]:


username = 'RS31209'
password = 'PASSWORD'
yob = '1994'


# In[ ]:


samco=StocknoteAPIPythonBridge()
login=samco.login(body={"userId":username,'password':password,'yob':yob})
login = json.loads(login)
samco.set_session_token(sessionToken=login['sessionToken'])
login


# In[ ]:


ocres=samco.get_option_chain(search_symbol_name='Nifty',exchange=samco.EXCHANGE_NFO,expiry_date='2022-10-20')
ocres = json.loads(ocres)
ocdf = pd.DataFrame(ocres['optionChainDetails'])
ocdf = ocdf[['tradingSymbol','optionType','expiryDate','lastTradedPrice','openInterest','openInterestChange','volume','strikePrice']]
ocdf = ocdf.astype({"strikePrice": float, "lastTradedPrice": float, "openInterest": int, "openInterestChange": int, "volume": int})
ocdf = ocdf[ocdf.openInterest >0]
ocdf


# In[ ]:


ceocdf = ocdf[ocdf.optionType =='CE' ]
peocdf = ocdf[ocdf.optionType =='PE' ]


# In[ ]:


ceocdf


# In[ ]:


peocdf


# In[ ]:


ceocdf.merge(peocdf,on = 'strikePrice')

