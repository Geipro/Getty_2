import requests

bitcoin_price = requests.get(url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC').json()[0]['trade_price']

url = 'https://api.binance.com/api/v3/ticker/'

res = requests.get(url+'price').json()[0]

print(res)

res = requests.get(url+'24hr').json()[0]

print(res)

print(bitcoin_price)