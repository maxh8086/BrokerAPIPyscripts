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


# In[ ]:


#pip uninstall  websocket-client
#pip install  websocket-client


# In[ ]:


username = 'RS4567'
password = 'PASSWORD'
yob = '1976'


# In[ ]:


samco=StocknoteAPIPythonBridge()
login=samco.login(body={"userId":username,'password':password,'yob':yob})
login = json.loads(login)
samco.set_session_token(sessionToken=login['sessionToken'])
login


# In[ ]:


import pandas as pd
tokendf= pd.read_csv('https://developers.stocknote.com/doc/ScripMaster.csv')
tokendf


# In[ ]:


tokendf[(tokendf.instrument == 'OPTIDX') & (tokendf.name == 'NIFTY') &  (tokendf.expiryDate == '2022-07-28') &  (tokendf.tradingSymbol.str.endswith('PE'))]


# In[ ]:


tokendf[(tokendf.instrument == 'EQ') ]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




