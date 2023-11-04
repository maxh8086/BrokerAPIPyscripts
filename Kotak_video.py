#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install git+https://github.com/osparamatrix/ks-orderapi-python.git


# In[ ]:


access_token = 'access_token_in_tradeApi_portal'
consumer_key='consumerkey_in_tradeapi_portal'
app_id ='secret_key_in_tradeapi_portal'


userid='your_user_id'
password = 'your_password'
access_code = 'acess_code_OTP'


# In[ ]:


from ks_api_client import ks_api
# Defining the host is optional and defaults to https://tradeapi.kotaksecurities.com/apim
# See configuration.py for a list of all supported configuration parameters.
client = ks_api.KSTradeApi(access_token = access_token, userid = userid,                 consumer_key =consumer_key, ip = "127.0.0.1", app_id = app_id)
client.login(password = password)
client.session_2fa(access_code = access_code)


# In[ ]:





# In[ ]:


url = 'https://tradeapi.kotaksecurities.com/apim/scripmaster/1.1/filename'


# In[ ]:


import requests
headers = {'accept' : 'application/json', "consumerKey": f"{consumer_key}" , "Authorization": f"Bearer {access_token}" }
res = requests.get(url, headers=headers).json()
res


# In[ ]:


cashurl = res['Success']['cash']
fnourl = res['Success']['fno']
cashurl , fnourl


# In[ ]:


cashurl


# In[ ]:


fnourl


# In[ ]:


import pandas as pd
cashdf = pd.read_csv(cashurl,sep='|')
cashdf


# In[ ]:


cashdf[(cashdf.instrumentName =='ITC') & (cashdf.exchange =='NSE') &  (cashdf.instrumentType =='EQ')]


# In[ ]:


import pandas as pd
FNOdf = pd.read_csv(fnourl,sep='|')
FNOdf


# In[ ]:


FNOdf.head(2)


# In[ ]:


FNOdf.segment.unique()


# In[ ]:


niftyOIToken = FNOdf[(FNOdf['segment'] == 'FO') & (FNOdf.instrumentType == 'OI') & (FNOdf.instrumentName == 'NIFTY') & (FNOdf.expiry == '06JAN22')]


# In[ ]:


niftyOIToken


# In[ ]:


client.session_token


# In[ ]:


import requests
url = 'https://tradeapi.kotaksecurities.com/apim/margin/1.0/margin'
headers = {'accept' : 'application/json', "consumerKey": consumer_key ,"sessionToken": client.session_token, "Authorization": f"Bearer {access_token}" }
res = requests.get(url, headers=headers).json()
res


# In[ ]:


orderes = client.place_order(order_type = "MIS", instrument_token = 1407, transaction_type = "BUY",                       quantity = 1, price =0, disclosed_quantity = 0, trigger_price = 220,                            validity = "GFD", variety = "REGULAR", tag = "string")
orderes


# In[ ]:


client.order_report()


# In[ ]:


modify_res= client.modify_order(order_id = "2220107094152", quantity = 1, price = 217, disclosed_quantity = 0, trigger_price = 0, validity = "GFD")
modify_res


# In[ ]:


client.cancel_order(order_id = "2220107094152")


# In[ ]:


client.positions(position_type = "TODAYS")


# In[ ]:




