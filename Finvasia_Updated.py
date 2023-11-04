import pyotp
import pandas as pd


from NorenRestApiPy.NorenApi import  NorenApi
class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://api.shoonya.com/NorenWClientTP/',websocket='wss://api.shoonya.com/NorenWSTP/',eodhost='https://api.shoonya.com/chartApi/getdata/')
        
api = ShoonyaApiPy()  

#credentials
user        = ''
pwd         = ''
totp_key=''

factor2     = pyotp.TOTP(totp_key).now()

vc          = ''
app_key     = ''
imei        = ''




res=api.login(userid=user, password=pwd, twoFA=factor2, vendor_code=vc, api_secret=app_key, imei=imei)
print(res)



eqdDf = pd.read_csv('https://api.shoonya.com/NSE_symbols.txt.zip',storage_options=  {"User-Agent": "pandas"})
nfoDf =  pd.read_csv('https://api.shoonya.com/NFO_symbols.txt.zip',storage_options=  {"User-Agent": "pandas"})
mcxDf = pd.read_csv('https://api.shoonya.com/MCX_symbols.txt.zip',storage_options=  {"User-Agent": "pandas"})