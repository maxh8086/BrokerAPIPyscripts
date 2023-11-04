#!/usr/bin/env python
# coding: utf-8

# In[ ]:


apikey = ''
username = 'HJD9KDK'
pin = '1234'
token = 'H3C5IDQRQGHJDIKDXJKFNA'


# In[ ]:


from smartapi import SmartConnect
import pyotp,json
obj=SmartConnect(api_key=apikey)
obj.generateSession(username,pin,pyotp.TOTP(token).now())
obj.rmsLimit()


# In[ ]:


obj.feed_token


# In[ ]:


cred = {'access_token':obj.access_token, 'refresh_token':obj.refresh_token ,'feed_token':obj.feed_token ,'userId':obj.userId ,'api_key':apikey}
with open("data.json", "w") as jsonfile:
       json.dump(cred, jsonfile)


# In[ ]:


obj.ltpData('NSE','NIFTY','26000')


# In[ ]:





# In[ ]:





# In[ ]:


from smartapi import SmartConnect
import json
with open('data.json', 'r') as jsonfile:
    cred = json.load(jsonfile)
print(cred)
obj2=SmartConnect(api_key=cred['api_key'],access_token=cred['access_token'], refresh_token=cred['refresh_token'] ,feed_token=cred['feed_token'], userId=cred['userId'])
obj2.rmsLimit()

