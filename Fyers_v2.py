#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install fyers-apiv2


# In[ ]:


pip show fyers-apiv2


# In[ ]:


from fyers_api import fyersModel
from fyers_api import accessToken


# In[ ]:


client_id = 'client'
secret_key = 'scret'
redirect_uri = 'http://127.0.0.1:5000/login'


# In[ ]:


session=accessToken.SessionModel(client_id=client_id,
secret_key=secret_key,redirect_uri=redirect_uri, 
response_type='code', grant_type='authorization_code')


# In[ ]:


response = session.generate_authcode() 
response


# In[ ]:


auth_code = ''


# In[ ]:


session.set_token(auth_code)
response = session.generate_token()

access_token = response["access_token"]
access_token


# In[ ]:


fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)


# In[ ]:


fyers.get_profile()


# In[ ]:


fyers.funds()


# In[ ]:


fyers.holdings()


# In[ ]:




