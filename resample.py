import pandas as pd
from datetime import datetime , time


data = pd.read_csv('TCS_min.csv')
data['date'] = pd.to_datetime(data['date'])
data = data[(data.date.dt.time > time(9,14)) & (data.date.dt.time < time(15,30))]

data['day'] = data.apply(lambda x: x.date.date(), axis=1)
data.set_index('date', inplace = True)
gp = data.groupby('day')
dfList = []
for k, res in gp:
    resampledf = res.resample('75T', origin='start').agg({'open': 'first', 
                                   'high': 'max', 
                                 'low': 'min', 
                                 'close': 'last','volume':'sum'})
    resampledf.reset_index(inplace=True)
    display(resampledf)
    dfList.append(resampledf)

resSampleDF = pd.concat(dfList,ignore_index = True)
resSampleDF