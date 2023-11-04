#!/usr/bin/env python
# coding: utf-8

# ## Connect Google Sheet 

# In[ ]:


import pandas as pd


# In[ ]:


import gspread
gc = gspread.service_account(filename='sheetAuth.json')
sh = gc.open("gsheetDemo")


# In[ ]:


wkpnl =sh.worksheet("PNL")
wkob =sh.worksheet("OB")
wktb =sh.worksheet("TB")


# ## Login Broker  

# In[ ]:


#credentials
user        = ''
pwd         = ''
totp_key    =''

factor2     = pyotp.TOTP(totp_key).now()
vc          = user+'_U'
app_key     = ''
imei        = ''


# In[ ]:


from NorenRestApiPy.NorenApi import  NorenApi
import pyotp
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
        global api
        api = self
api = ShoonyaApiPy()  



res=api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(api.get_limits())


# In[ ]:


pnldf = pd.DataFrame(api.get_positions())
pnldf


# In[ ]:


obdf = pd.DataFrame(api.get_order_book())
obdf.fillna(0,inplace = True)
obdf


# In[ ]:


tbdf = pd.DataFrame(api.get_trade_book())
tbdf.fillna(0,inplace = True)
tbdf


# In[ ]:





# In[ ]:


wkpnl.update('B2',[pnldf.columns.values.tolist()] + pnldf.values.tolist())


# In[ ]:





# In[ ]:


wktb.update('B74',[tbdf.columns.values.tolist()] + tbdf.values.tolist())


# In[ ]:


wkob.update('C49',[obdf.columns.values.tolist()] + obdf.values.tolist())


# In[ ]:





