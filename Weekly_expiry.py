import pandas as pd
from datetime import datetime 
symboldf = pd.read_csv('https://api.kite.trade/instruments')

def getExpiryDate(i=0):
    df = symboldf[(symboldf.exchange == 'NFO') & (symboldf.name == 'NIFTY')  & (symboldf.segment == 'NFO-OPT')]
    df['expiry'] = pd.to_datetime(df['expiry']).apply(lambda x: x.date())
    df.drop(df[df.expiry <datetime.now().date()].index, inplace=True)
    weekly_expiry = df[df.segment == 'NFO-OPT']['expiry'].unique().tolist()
    weekly_expiry.sort()
    return weekly_expiry[i]


getExpiryDate(0)