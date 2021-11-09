import requests
import json
import math

#url 호출을 위한 list
check_list = []

#coin 객체 = {'KRW-BTC' : {이름 : , 가격 : , 최고가(52주) : , 최저가(52주) : , 거래량(일): },     '이더리움' : {}} 과 같은 구조로 생긴 객체 생성
coin_object = dict()
coin_list = []

#업비트 API 호출을 위한 URL
url = 'https://api.upbit.com/v1/ticker?markets='

#coin 객체에 이름, 심볼명 주기적으로 업데이트
def get_coin_symbol():
    res = requests.get('https://api.upbit.com/v1/market/all').json()
    for li in res:
        if 'KRW' in str(li.values()):
            coin_sym = li['market']
            coin_object[coin_sym] = dict()
            coin_object[coin_sym]['name'] = str(list(li.values())[1])
            coin_object[coin_sym]['sym'] = str(coin_sym)[4:]
            check_list.append(coin_sym)



#coin_object 안에 데이터 넣기
#얼마마다 갱신할 지
def update_coin_data():
    for coin in check_list[:3]:
        tot_URL = url + coin
        res = requests.get(tot_URL).json()[0]
        # print(res)
        pri = res['trade_price']
        hi_pri = res['highest_52_week_price']
        low_pri = res['lowest_52_week_price']
        trade_vol = res['acc_trade_price_24h']
        coin_object[coin]['price'] = pri
        coin_object[coin]['day_chage_price'] = res['signed_change_price']
        coin_object[coin]['day_change_rate'] = res['signed_change_rate']
        coin_object[coin]['highest_52_week_price'] = hi_pri
        coin_object[coin]['highest_52_week_rate'] = round((hi_pri - pri)/hi_pri*100, 2)*-1
        coin_object[coin]['lowest_52_week_price'] = low_pri
        coin_object[coin]['lowest_52_week_rate'] = round((pri - low_pri)/low_pri*100, 2)
        coin_object[coin]['acc_trade_volume_24h'] = res['acc_trade_volume_24h']
        coin_object[coin]['acc_trade_price_24h'] = trade_vol
        coin_list.append(coin_object[coin])
    print(coin_list)

def sort_by_name_upper():
    coin_list.sort(key=lambda x : x['name'], reverse=True)

def sort_by_name_lower():
    coin_list.sort(key=lambda x : x['name'])

def sort_by_price_upper():
    coin_list.sort(key=lambda x : x['price'], reverse=True)

def sort_by_price_lower():
    coin_list.sort(key=lambda x : x['price'])

def sort_by_change_rate_upper():
    coin_list.sort(key=lambda x : x['day_change_rate'], reverse=True)

def sort_by_change_rate_lower():
    coin_list.sort(key=lambda x : x['day_change_rate'])

def sort_by_highest_52_week_upper():
    coin_list.sort(key=lambda x : x['highest_52_week_rate'], reverse=True)

def sort_by_highest_52_week_lower():
    coin_list.sort(key=lambda x : x['highest_52_week_rate'])

def sort_by_lowest_52_week_upper():
    coin_list.sort(key=lambda x : x['lowest_52_week_rate'], reverse=True)

def sort_by_lowest_52_week_lower():
    coin_list.sort(key=lambda x : x['lowest_52_week_rate'])

def sort_by_trade_vol_upper():
    coin_list.sort(key=lambda x : x['acc_trade_price_24h'], reverse=True)
    
def sort_by_trade_vol_lower():
    coin_list.sort(key=lambda x : x['acc_trade_price_24h'])

def print_all():
    for coin in coin_list:
        print(coin, end='\n')

if __name__ == '__main__':
    get_coin_symbol()
    update_coin_data()
    sort_by_name_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('이름 순 upper 정렬')
    print_all()
    sort_by_name_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('이름 순 lower 정렬')
    print_all()
    sort_by_price_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('가격 순 upper 정렬')
    print_all()
    sort_by_price_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('가격 순 lower 정렬')
    print_all()
    sort_by_change_rate_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('변동률 순 upper 정렬')
    print_all()
    sort_by_change_rate_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('변동률 순 lower 정렬')
    print_all()
    sort_by_highest_52_week_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('고가대비 순 upper 정렬')
    print_all()
    sort_by_highest_52_week_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('고가대비 순 lower 정렬')
    print_all()
    sort_by_lowest_52_week_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('저가대비 순 upper 정렬')
    print_all()
    sort_by_lowest_52_week_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('저가대비 순 lower 정렬')
    print_all()
    sort_by_trade_vol_upper()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('거래액 순 upper 정렬')
    print_all()
    sort_by_trade_vol_lower()
    print('--------------------------------------------------------------------------------------------------------------------------')
    print('거래액 순 lower 정렬')
    print_all()