#!/usr/bin/env python
# coding: utf-8

# # How to get credentials
# # Dhan Python sdk install
# # Login 
# # Symbol Token Master list
# # See example of availble API

# In[ ]:


cleintid = 'clientID'
accessToken = 'accessToken'


# In[ ]:


pip install dhanhq


# In[ ]:


from dhanhq import dhanhq


# In[ ]:


dhan = dhanhq(cleintid,accessToken)


# In[ ]:


dhan.get_fund_limits()


# In[ ]:


import pandas as pd


# In[ ]:


masterList = pd.read_csv('https://images.dhan.co/api-data/api-scrip-master.csv',nrows=1)
masterList = pd.read_csv('https://images.dhan.co/api-data/api-scrip-master.csv',usecols=masterList.columns,low_memory=False)
masterList[['SYMBOL', 'EXP_DATE','EXP_MONTH','STRIKE','OPT_TYPE']] = masterList['SEM_CUSTOM_SYMBOL'].str.split(' ', n=4, expand=True)
masterList


# In[ ]:


masterList[(masterList.SEM_INSTRUMENT_NAME == 'EQUITY') & (masterList.SEM_TRADING_SYMBOL == 'HDFC-EQ')]


# In[ ]:


masterList[ (masterList.SEM_EXM_EXCH_ID == 'MCX') & (masterList.SYMBOL == 'CRUDEOIL')  & (masterList.SEM_INSTRUMENT_NAME == 'FUTCOM')]


# In[ ]:


masterList[ (masterList.SEM_EXM_EXCH_ID == 'NSE') & (masterList.SYMBOL == 'NIFTY')  & (masterList.OPT_TYPE == 'CALL') & (masterList.STRIKE == '18000')  & (masterList.EXP_DATE == '05') & (masterList.EXP_MONTH == 'JAN') ]


# In[ ]:


dhan.place_order(security_id= '1330',   #hdfcbank
    exchange_segment= dhan.NSE,
    transaction_type= dhan.BUY,
    quantity=10,
    order_type=dhan.MARKET,
    product_type= dhan.INTRA,
    price=0)


# In[ ]:


dir(dhan)


# In[ ]:


dhan.get_order_list()


# In[ ]:


dhan.get_positions()


# In[ ]:


dhan.get_trade_book()


# In[ ]:


dhan.get_fund_limits()


# In[ ]:




