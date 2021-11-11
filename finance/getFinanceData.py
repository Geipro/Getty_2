import requests
from bs4 import BeautifulSoup as bs


key = 'fac934f307d1d0770ec3143a5f14eaa7'
URL = 'http://finlife.fss.or.kr/finlifeapi/'
bank_code = '020000'

#정기예금, 적금, 주택담보대출, 전세자금대출, 개인신용대출 api이용을 위한 리스트
URL_list = ['depositProductsSearch', 'savingProductsSearch', 'mortgageLoanProductsSearch',
 'rentHouseLoanProductsSearch', 'creditLoanProductsSearch']

# 정기예금 : { 은행이름, 상품이름, 가입경로, 만기 후 이율, 우대 조건, 가입제한, 최고한도, 유의사항}
deposit_list = []
deposit = dict()

# 적금 : 예금과 동일
saving_list = []
saving = dict()

# 분할상환 방식, 변동금리 기준 -> 네이버가 분할상환, 변동금리 기준으로 제공
# 주택담보대출 : { 은행이름, 상품이름, 가입방법, 중도상환수수료, 연체이자율, 대출한도, 담보유형, 대출금리 최저, 최고, 전월평균 }
mortgage_list = []

# 만기일시 상환방식, 변동금리 기준
# 전세자금대출 : 주택담보대출과 동일
rentHouse_list = []


# 신용대출 : { 은행이름, 상품이름, 가입방법, 대출종류명, 신용평가회사, 900점 초과 금리, 801 ~ 900, 701 ~ 800, 
# 601 ~ 700, 501 ~ 600, 401 ~ 500, 301 ~ 400, 300이하, 평균 금리 }
creditLoan_list = []

totURL_list = []

# 금융 정보 가져올 API url 생성
def make_total_URL():
    cnt = 0
    for url in URL_list:
        cnt += 1
        if cnt < 3:
            totURL_list.append(f'{URL}{url}.json?auth={key}&topFinGrpNo={bank_code}&pageNo=1')
        else:
            totURL_list.append(f'{URL}{url}.xml?auth={key}&topFinGrpNo={bank_code}&pageNo=1')


# 정기예금 데이터 get
def getDeposit():
    res = requests.get(totURL_list[0]).json()
    for result in res['result']['baseList']:
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

# 적금 데이터 get
def getSaving():
    res = requests.get(totURL_list[1]).json()

    for result in res['result']['baseList']:
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

# 주택담보대출 API get
def getMortgage():
    res = requests.get(totURL_list[2])._content
    xml_obj = bs(res, 'lxml-xml')
    for result in xml_obj.find_all('product'):
        mortgage = dict()
        base = result.find('baseinfo')
        options = result.find_all('option')
        mortgage['bank_name'] = base.find('kor_co_nm').text
        mortgage['product_name'] = base.find('fin_prdt_nm').text
        mortgage['join_way'] = base.find('join_way').text
        mortgage['loan_inci_expn'] = base.find('loan_inci_expn').text
        mortgage['erly_rpay_fee'] = base.find('erly_rpay_fee').text
        mortgage['dly_rate'] = base.find('dly_rate').text
        mortgage['loan_lmt'] = base.find('loan_lmt').text
        for option in options:
            if option.find('rpay_type_nm').text == '분할상환방식' and option.find('lend_rate_type_nm').text == '변동금리':
                mortgage['mrtg_type_nm'] = option.find('mrtg_type_nm').text
                mortgage['lend_rate_min'] = option.find('lend_rate_min').text
                mortgage['lend_rate_max'] = option.find('lend_rate_max').text
                mortgage['lend_rate_avg'] = option.find('lend_rate_avg').text
        mortgage_list.append(mortgage)
    for mg in mortgage_list:
        print(mg, end='\n\n-----------------------------------------------------------------------\n\n')

# 전세자금 API get
def getRentHouse():
    res = requests.get(totURL_list[3])._content
    xml_obj = bs(res, 'lxml-xml')

    for result in xml_obj.find_all('product'):
        rentHouse = dict()
        base = result.find('baseinfo')
        options = result.find_all('option')
        rentHouse['bank_name'] = base.find('kor_co_nm').text
        rentHouse['product_name'] = base.find('fin_prdt_nm').text
        rentHouse['join_way'] = base.find('join_way').text
        rentHouse['loan_inci_expn'] = base.find('loan_inci_expn').text
        rentHouse['erly_rpay_fee'] = base.find('erly_rpay_fee').text
        rentHouse['dly_rate'] = base.find('dly_rate').text
        rentHouse['loan_lmt'] = base.find('loan_lmt').text
        for option in options:
            if option.find('rpay_type_nm').text == '만기일시상환방식' and option.find('lend_rate_type_nm').text == '변동금리':
                rentHouse['lend_rate_min'] = option.find('lend_rate_min').text
                rentHouse['lend_rate_max'] = option.find('lend_rate_max').text
                rentHouse['lend_rate_avg'] = option.find('lend_rate_avg').text
        rentHouse_list.append(rentHouse)
        for mg in rentHouse_list:
            print(mg, end='\n\n-----------------------------------------------------------------------\n\n')

# 개인신용대출 API get
def getcreditLoan():
    res = requests.get(totURL_list[4])._content
    xml_obj = bs(res, 'lxml-xml')

    for result in xml_obj.find_all('product'):
        creditLoan = dict()
        base = result.find('baseinfo')
        options = result.find_all('option')
        creditLoan['bank_name'] = base.find('kor_co_nm').text
        creditLoan['product_name'] = base.find('fin_prdt_nm').text
        creditLoan['join_way'] = base.find('join_way').text
        creditLoan['cb_name'] = base.find('cb_name').text
        creditLoan['crdt_prdt_type_nm'] = base.find('crdt_prdt_type_nm').text
        for option in options:
            if option.find('crdt_lend_rate_type_nm').text == '대출금리':
                creditLoan['crdt_grad_1'] = option.find('crdt_grad_1').text
                creditLoan['crdt_grad_4'] = option.find('crdt_grad_4').text
                creditLoan['crdt_grad_5'] = option.find('crdt_grad_5').text
                creditLoan['crdt_grad_6'] = option.find('crdt_grad_6').text
                creditLoan['crdt_grad_10'] = option.find('crdt_grad_10').text
                creditLoan['crdt_grad_11'] = option.find('crdt_grad_11').text
                creditLoan['crdt_grad_12'] = option.find('crdt_grad_12').text
                creditLoan['crdt_grad_13'] = option.find('crdt_grad_13').text
                creditLoan['crdt_grad_avg'] = option.find('crdt_grad_avg').text
        creditLoan_list.append(creditLoan)
        for mg in creditLoan_list:
            print(mg, end='\n\n-----------------------------------------------------------------------\n\n')

if __name__ == '__main__':
    make_total_URL()
    getDeposit()
    getSaving()
    getMortgage()
    getRentHouse()
    getcreditLoan()