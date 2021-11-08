import requests

#한국 비트코인 가격
bitcoin_price = requests.get(url = 'https://api.upbit.com/v1/ticker?markets=KRW-BTC').json()[0]['trade_price']

upbit_coin_list = []
binance_coin_list = []

url = 'https://api.binance.com/api/v3/ticker/'

res = requests.get(url+'price').json()

for coin in res:
    check_btc = coin['symbol'][-3:]
    coin_object = dict()
    if check_btc == 'BTC':
        price = int(float(coin['price'])*bitcoin_price)
        coin_object['sym'] = coin['symbol'][:-3]
        coin_object['price'] = price
        binance_coin_list.append(coin_object)

print(binance_coin_list)
# res = requests.get(url+'24hr').json()[0]
