#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pya3


# In[ ]:


from pya3 import *
api_key = ''
alice = Aliceblue(user_id='your_userid',api_key=api_key)
alice.get_session_id()        


# In[ ]:


alice.get_balance()


# In[ ]:


alice.get_contract_master("BSE")
alice.get_contract_master("NSE")


# In[ ]:


alice.get_instrument_by_token('NSE',22)


# In[ ]:


alice.get_instrument_for_fno(exch="NFO",symbol='BANKNIFTY', expiry_date="25-08-2022", is_fut=True,strike=None, is_CE=False)


# In[ ]:


alice.get_instrument_by_symbol('NSE','ONGC')


# In[ ]:


import pandas as pd
nfo = pd.read_csv('NFO.csv')


# In[ ]:


res= alice.place_order(transaction_type = TransactionType.Buy,
                     instrument = alice.get_instrument_by_symbol('NSE', 'HDFC'),
                     quantity = 1,
                     order_type = OrderType.Market,
                     product_type = ProductType.Delivery,
                     price = 0.0,
                     trigger_price = None,
                     stop_loss = None,
                     square_off = None,
                     trailing_sl = None,
                     is_amo = False,
                     order_tag='order1')

res


# In[ ]:


alice.get_order_history('220816000001503')


# In[ ]:


alice.get_order_history('')


# In[ ]:





# In[ ]:





# In[ ]:




