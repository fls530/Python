import json
import urllib
import requests

url = f'http://v.juhe.cn/laohuangli/d?date=2014-09-11&key=05a6317956636ce7784846e3611cd8a3'
#response = requests.get(url).content.decode()
response = requests.get(url).json()
print(type(response))

