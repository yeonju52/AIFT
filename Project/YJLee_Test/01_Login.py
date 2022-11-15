from pykiwoom.kiwoom import *
import pprint

### [1] 기본 함수
# 1. 기본 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)  # 블록킹 로그인
print("블록킹 로그인 완료")

# 2. 연결상태: GetConnectState()
print("미연결" if kiwoom.GetConnectState() == 0 else "연결완료")

# 3. 사용자 정보 얻어오기 : GetLoginInfo()
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수 = 1
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트 = ['8035037311']
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID = duswn52
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명 = 이연주
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부 = 0
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부 = 0
print(account_num, accounts, user_id, user_name, keyboard, firewall)

# 4. 종목 코드 얻기: GetCodeListByMarket('종목대분류?')
etf = kiwoom.GetCodeListByMarket('8')
print(len(etf), etf[0:5])


## [2] kiwoom.GetMaster++: 한 개의 종목의 정보를 알 수 있다. 인자는 종목코드를 넣으면 된다. 예) "005930" <= "삼성전자"
#### error: Process finished with exit code -1073741819 (0xC0000005) ####
#### 인코딩 에러로 추정 : GetMasterCodeName(), GetMasterListedStockCnt

# 1. 종목명 얻기: GetMasterCodeName("종목코드")
name = kiwoom.GetMasterCodeName("005930")
print(name)

# 2. 상장 주식수 얻기: 버그 존재 => 최대 21억까지만 표현 가능
stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print("삼성전자 상장주식수: ", stock_cnt)

# 3. 감리구분: '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'
risk = kiwoom.GetMasterConstruction("005930")
print(risk)

# 4. 상장일
stockdate = kiwoom.GetMasterListedStockDate("005930")
print(stockdate)
print(type(stockdate))        # datetime.datetime 객체

# 5. 전일가 = 전일 종가
LastPrice = kiwoom.GetMasterLastPrice("005930")
print(int(LastPrice))
print(type(LastPrice))

# 6. 종목 상태
StockState = kiwoom.GetMasterStockState("005930")
print(StockState)


### [3] 테마그룹: kiwoom.GetThemeGroup++
# 1. 테마명: 테마코드
group = kiwoom.GetThemeGroupList(1)
pprint.pprint(group)

# 2. 테마별 종목코드 & 종목명
tickers = kiwoom.GetThemeGroupCode('458')
for ticker in tickers:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)
