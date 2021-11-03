import requests
import json
import math

check_list = []

#coin 객체 = {'KRW-BTC' : {이름 : , 가격 : , 최고가(52주) : , 최저가(52주) : , 거래량(일): },     '이더리움' : {}} 과 같은 구조로 생긴 객체 생성
coin_object = dict()




res = requests.get('https://api.upbit.com/v1/market/all').json()
for li in res:
    # print(str(li.values()))
    if 'KRW' in str(li.values()):
        coin_sym = li['market']
        coin_name = list(li.values())[1]
        coin_object[f'{coin_sym}'] = dict()
        coin_object[f'{coin_sym}']['name'] = str(list(li.values())[1])
        coin_object[f'{coin_sym}']['sym'] = str(coin_sym)[4:]
        check_list.append(coin_sym)


# print(check_list)
# print(coin_object)
# print(json_obejct['market'])

#coin_object 안에 데이터 넣기
#얼마마다 갱신할 지
print('-----------------------------------------------------------------------------------')
url = 'https://api.upbit.com/v1/ticker?markets='
for coin in check_list[:1]:
    tot_URL = url + coin
    res = requests.get(tot_URL).json()[0]
    print(res)
    pri = res['trade_price']
    hi_pri = res['highest_52_week_price']
    low_pri = res['lowest_52_week_price']
    coin_object[coin]['price'] = pri
    coin_object[coin]['day_chage_price'] = res['signed_change_price']
    coin_object[coin]['day_change_rate'] = res['signed_change_rate']
    coin_object[coin]['highest_52_week_price'] = hi_pri
    coin_object[coin]['highest_52_week_rate'] = round((hi_pri - pri)/hi_pri*100, 2)
    coin_object[coin]['lowest_52_week_price'] = low_pri
    coin_object[coin]['lowest_52_week_rate'] = round((pri - low_pri)/low_pri*100, 2)
    print(coin_object[coin])

    # print(res)
# res = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-BTC').json()
# print(res[0])