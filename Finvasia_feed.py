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



#start of our program
api = ShoonyaApiPy()


 
#make the api call
ret = api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)

ret['stat']


# In[ ]:


api.searchscrip(exchange='MCX', searchtext='SILVERMIC')


# In[ ]:


api.searchscrip(exchange='MCX', searchtext='CRUDEOIL')


# In[ ]:


feed_opened = False


feedJson = {}
from datetime import datetime
def event_handler_feed_update(tick_data):
    if 'lp' in tick_data and 'tk' in tick_data :
        timest = datetime.fromtimestamp(int(tick_data['ft'])).isoformat()
        feedJson[tick_data['tk']] = {'ltp':tick_data['lp'] , 'tt': timest}
        print(f"feed update {tick_data['tk']}  {tick_data['lp']} {timest}")

    
def event_handler_order_update(tick_data):
    print(f"oRDER update {tick_data}")

def open_callback():
    global feed_opened
    feed_opened = True


api.start_websocket( order_update_callback=event_handler_order_update,
                     subscribe_callback=event_handler_feed_update, 
                     socket_open_callback=open_callback)

while(feed_opened==False):
    pass



#subscribe to multiple tokens
api.subscribe(['MCX|231993', 'MCX|234196'])


# In[ ]:


feedJson


# In[ ]:




