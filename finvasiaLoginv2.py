from NorenRestApiPy.NorenApi import  NorenApi
import pyotp

user        = 'FA32807'
pwd         = 'your_password'
vc          = 'FA32807_U'
app_key     = 'app_key'
token       =  'QRCodeToken'

class ShoonyaApiPy(NorenApi):
    def __init__(self):
        NorenApi.__init__(self, host='https://shoonyatrade.finvasia.com/NorenWClientTP/', websocket='wss://shoonyatrade.finvasia.com/NorenWSTP/', eodhost='https://shoonya.finvasia.com/chartApi/getdata/')
        global api
        api = self

api = ShoonyaApiPy()      

ret = api.login(userid=user, password=pwd, twoFA=pyotp.TOTP(token).now(), vendor_code=vc, api_secret=app_key, imei='dfsghwd6eydbef8hdnk')

print(ret)