#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install C:\Users\hari\Desktop\NorenRestApiPy-0.0.16-py2.py3-none-any.whl


# In[9]:


user        = 'FA507567'
pwd         = 'PASSWORD'
factor2     = 'AJT633AA'
vc          = 'FA507567_U'
app_key     = '30082c2625256ab64be86516868djs5b11'
imei        = 'ca57e1ccjdicjjml8'





from NorenRestApiPy.NorenApi import  NorenApi


class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')


# In[11]:


import logging
 
#enable dbug to see request and responses
logging.basicConfig(level=logging.DEBUG)

#start of our program
api = ShoonyaApiPy()


 
#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)


# In[12]:


dir(api)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




