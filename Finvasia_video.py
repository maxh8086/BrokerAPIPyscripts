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

ret['actid']


# In[ ]:


dir(api)


# In[ ]:


api.searchscrip(exchange='MCX', searchtext='SILVERMIC')


# In[ ]:


api.get_security_info('NSE', '22')


# In[ ]:


api.get_quotes('NSE', 'Nifty 50')


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


ret = api.place_order(buy_or_sell='B', product_type='I',
                        exchange='MCX', tradingsymbol='SILVERMIC28FEB22', 
                        quantity=1, discloseqty=0,price_type='LMT', price=63500, trigger_price=0,
                        retention='DAY', remarks='my_order_001')
ret


# In[ ]:


retMod = api.modify_order(exchange='MCX', tradingsymbol='SILVERMIC28FEB22', orderno='22021000287410',
                                   newquantity=1, newprice_type='LMT', newprice=63600)
retMod


# In[ ]:


api.cancel_order(orderno='22021000287410')


# In[ ]:


pd.DataFrame(api.get_positions())


# In[ ]:


pd.DataFrame(api.get_order_book())


# In[ ]:


pd.DataFrame(api.get_trade_book())


# In[ ]:


api.get_holdings()


# 
# # STEP 1:  Get index ltp
# 
# # STEP 2:  Get ATM Strike
# 
# # STEP 3:  Get ATM Symbol Details
# 
# # STEP 4:  Place Sell/Buy Order
# 

# In[ ]:


def getSymbol(txt):
    res = api.searchscrip('NFO',txt)
    resDf = pd.DataFrame(res['values'])
    return resDf.sort_values(by='weekly').iloc[0]


qRes = api.get_quotes('NSE', 'Nifty Bank')
indexLtp = float(qRes['lp'])
print(indexLtp)
import math
mod = int(indexLtp)%100
if mod < 50:
    atmStrike =  int(math.floor(indexLtp / 100)) * 100
else:
     atmStrike=  int(math.ceil(indexLtp /100)) * 100


        
print(atmStrike)



month = 'FEB'
cesymbolInfo = getSymbol(f'BANKNIFTY {month} {atmStrike} CE')
cesymbolInfo['tsym'] , int(cesymbolInfo['ls']) 

pesymbolInfo = getSymbol(f'BANKNIFTY {month} {atmStrike} PE')
pesymbolInfo['tsym'] , int(pesymbolInfo['ls']) 

qty = int(pesymbolInfo['ls'])*2

api.place_order(buy_or_sell='S', product_type='I',
                        exchange='NFO', tradingsymbol=cesymbolInfo['tsym'], 
                        quantity=qty, discloseqty=0,price_type='MKT', price=0, trigger_price=0,
                        retention='DAY', remarks='DFT')

api.place_order(buy_or_sell='S', product_type='I',
                        exchange='NFO', tradingsymbol=pesymbolInfo['tsym'], 
                        quantity=qty, discloseqty=0,price_type='MKT', price=0, trigger_price=0,
                        retention='DAY', remarks='DFT')


# In[ ]:





# In[ ]:


txt = 'NIFTY FEB 17300 CE'
res = api.searchscrip('NFO',txt)
resDf = pd.DataFrame(res['values'])
resDf


# In[ ]:





# In[ ]:


cesymbolInfo['tsym'] , pesymbolInfo['tsym'] 


# In[ ]:





# In[ ]:





# In[ ]:




