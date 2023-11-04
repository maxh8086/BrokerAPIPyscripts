#pip install pyotp
#pip --no-cache-dir install --upgrade smartapi-python


from smartapi import SmartConnect
import pyotp

apikey = 'GOP780V'
username = 'N900046'
pwd = '7890g29'
token = 'H3C5IDQRQUSINVQOKTYUNB'


obj=SmartConnect(api_key=apikey)
data = obj.generateSession(username,pwd,pyotp.TOTP(token).now())
print(data)
refreshToken= data['data']['refreshToken']
res = obj.getProfile(refreshToken)
print(res)