import time as tt
import requests
import pandas as pd
from datetime import date ,timedelta
from smartapi import SmartConnect

# angel api credentials 
apikey = 'APIKEY'
username = 'USERID'
pwd = 'PASSWORD'

# telgram credentials
BOT_TOKEN = ''     # watch this to get bot token and chat id   https://youtu.be/Sq_cYIlm_pM
BOT_CHAT_ID = ''    

lookbackDay = 3

def login():
    obj=SmartConnect(api_key=apikey)
    data = obj.generateSession(username,pwd)
    refreshToken= data['data']['refreshToken']
    res = obj.getProfile(refreshToken)
    res['data']['exchanges']
    return obj


def getSymbolToken():
    url = 'https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json'
    d = requests.get(url).json()
    token_df = pd.DataFrame.from_dict(d)
    token_df['expiry'] = pd.to_datetime(token_df['expiry']).apply(lambda x: x.date())
    token_df = token_df.astype({'strike': float})
    return token_df

def getCandleData(token,obj):
   
    try:
        historicParam={
        "exchange": "NSE",
        "symboltoken": token,
        "interval": "ONE_DAY",
        "fromdate": f'{date.today()-timedelta(days=10)} 09:15' , 
        "todate": f'{date.today()} 15:30' 
        }
        return obj.getCandleData(historicParam)
    except Exception as e:
        print(f"Historic Api failed: {e.message}")


def telegram_bot_sendtext(bot_message):
    
    send_text = 'https://api.telegram.org/bot' + BOT_TOKEN + '/sendMessage?chat_id=' + BOT_CHAT_ID + \
                '&parse_mode=HTML&text=' + bot_message
    
    response = requests.get(send_text)
    print(response)


def scanStocks():
    
    start = tt.time()
    highList = []
    lowList = []
    angel_obj = login()
    token_df = getSymbolToken()
    symbol_token = token_df[(token_df.exch_seg =='NFO') & (token_df.instrumenttype =='FUTSTK')]
    fnoSymbol = symbol_token.name.unique()
    symbolDf = token_df[token_df.symbol.str.endswith('-EQ') & (token_df.exch_seg =='NSE') & token_df.name.isin(fnoSymbol)].sort_values(by ='symbol') 
    symbolDf.reset_index(inplace =True)
    symbolDf
    for i in symbolDf.index:
        try:
            symbol = symbolDf.loc[i]['symbol']
            token = symbolDf.loc[i]['token']
            res =   getCandleData(token, angel_obj) 
            candleInfo = pd.DataFrame(res['data'],columns = ['data','open','high','low','close','vol'])
            recentCandle = candleInfo.iloc[-1]
        
            lastndaysCandle = candleInfo.iloc[-(lookbackDay+1):-1]
            high = lastndaysCandle.high.max()
            low = lastndaysCandle.low.min()
            
            if recentCandle.close > high:
                print('High break', high ,recentCandle.close,   symbol)
                highList.append(symbol)
            
            elif  recentCandle.close < low:
                print('Low break',low ,recentCandle.close,   symbol)
                lowList.append(symbol)
        
            tt.sleep(0.3)
        except Exception as e:
            print("Error in scan for " ,symbol, e )

    telegram_bot_sendtext(f'High Breakout {highList}')   
    telegram_bot_sendtext(f'Low Breakout {lowList}')   
    print(tt.time() - start, ' sec ')
    
if __name__ == '__main__':
    telegram_bot_sendtext(f'Scanning Started')  
    scanStocks()
    