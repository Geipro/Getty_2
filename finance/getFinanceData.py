import requests
import json

from requests.exceptions import SSLError

# 요청 포맷 http://finlife.fss.or.kr/finlifeapi/creditLoanProductsSearch.xml?auth={발급받은 인증키}&topFinGrpNo=050000&pageNo=1

key = 'fac934f307d1d0770ec3143a5f14eaa7'
URL = 'http://finlife.fss.or.kr/finlifeapi/'
bank_code = '020000'

#정기예금, 적금, 연금저축, 주택담보대출, 전세자금대출, 개인신용대출 api이용을 위한 리스트
URL_list = ['depositProductsSearch', 'savingProductsSearch', 'annuitySavingProductsSearch', 'mortgageLoanProductsSearch',
 'rentHouseLoanProductsSearch', 'creditLoanProductsSearch']

# 정기예금 { 은행이름, 상품이름, 가입경로, 만기 후 이율, 우대 조건, 가입제한, 최고한도, 유의사항}
deposit_list = []
deposit = dict()

# 적금
saving_list = []
saving = dict()

# 연금 저축
annuity_list = []
annuity = dict()

totURL_list = []
def getMaxPage():
    for url in URL_list:
        totURL_list.append(f'{URL}{url}.json?auth={key}&topFinGrpNo={bank_code}&pageNo=1')

    # for url in totURL_list:
    #     res = requests.get(url).json()

    #     print(res['result'])



# 정기예금 데이터 get
def getDeposit():
    res = requests.get(totURL_list[0]).json()
    # print(res['result']['baseList'][0])

    for result in res['result']['baseList'][:2]:
        deposit['bank_name'] = result['kor_co_nm']
        deposit['product_name'] = result['fin_prdt_nm']
        deposit['join_way'] = result['join_way']
        deposit['interest_rate'] = result['mtrt_int']
        deposit['preferential_term'] = result['spcl_cnd']
        if result['join_deny'] == '1':
            deposit['join_deny'] = '제한없음'
        elif result['join_deny'] == '2':
            deposit['join_deny'] = '서민전용'
        elif result['join_deny'] == '3':
            deposit['join_deny'] = '일부제한'
        deposit['max_limit'] = result['max_limit']
        deposit['etc_note'] = result['etc_note']
        deposit_list.append(deposit)
    print(deposit_list)

def getSaving():
    res = requests.get(totURL_list[1]).json()

    for result in res['result']['baseList'][:2]:
        saving['bank_name'] = result['kor_co_nm']
        saving['product_name'] = result['fin_prdt_nm']
        saving['join_way'] = result['join_way']
        saving['interest_rate'] = result['mtrt_int']
        saving['preferential_term'] = result['spcl_cnd']
        if result['join_deny'] == '1':
            saving['join_deny'] = '제한없음'
        elif result['join_deny'] == '2':
            saving['join_deny'] = '서민전용'
        elif result['join_deny'] == '3':
            saving['join_deny'] = '일부제한'
        saving['max_limit'] = result['max_limit']
        saving['etc_note'] = result['etc_note']
        saving_list.append(saving)
    print(saving_list)

def getData():
    pass

if __name__ == '__main__':
    getMaxPage()
    # getDeposit()
    getSaving()