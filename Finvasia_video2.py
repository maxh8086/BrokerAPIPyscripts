#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install C:\Users\hari\Desktop\NorenRestApiPy-0.0.16-py2.py3-none-any.whl


# In[ ]:


user        = 'FA67507'
pwd         = 'password'
factor2     = 'pan_no'
vc          = 'FA67507_U'
app_key     = 'your_api_key'
imei        = 'mac_address'


# In[ ]:


from NorenRestApiPy.NorenApi import  NorenApi


class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')


# In[ ]:


import logging
 


#start of our program
api = ShoonyaApiPy()


 
#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

print(ret)


# In[ ]:


dir(api)


# In[ ]:


api.searchscrip(exchange='NFO', searchtext='NIFTY 24FEB 17500')


# In[ ]:


api.get_security_info('NSE', '22')


# In[ ]:


api.get_quotes('MCX', '230195')


# In[ ]:


from datetime import datetime
lastBusDay = datetime.today()
lastBusDay = lastBusDay.replace(hour=0, minute=0, second=0, microsecond=0)
ret = api.get_time_price_series(exchange='NSE', token='22', starttime=lastBusDay.timestamp(), interval=1)


# In[ ]:


import pandas
pd.DataFrame(ret)


# In[ ]:


oc = api.get_option_chain('NFO', 'NIFTY24FEB22P17500', 17500, 6)
pd.DataFrame(oc['values'])


# In[ ]:




