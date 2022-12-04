import pandas as pd
# from tqdm.auto import tqdm
import time

TR_REQ_TIME_INTERVAL = 3.4 # TODO: 가능하면 시간을 줄여보자 (0.2)
'''
횟수 제한 안내
https://kminito.tistory.com/35

3.6초 간격 : 1시간에 1,000회 -> 정상 작동
'''

# opt10081 TR 요청
def TR_day(kiwoom, item_code, yyyymmdd): # TODO: 포인터로 받아야 하나?
    kiwoom.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}   # dictionary
    
    # opt10081 TR 요청
    kiwoom.set_input_value("종목코드", item_code)
    kiwoom.set_input_value("기준일자", yyyymmdd)
    kiwoom.set_input_value("수정주가구분", 1)
    kiwoom.comm_rq_data("opt10081_req", "opt10081", 0, "0001")

    while kiwoom.remained_data == True:
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoom.set_input_value("종목코드", item_code)
        kiwoom.set_input_value("기준일자", yyyymmdd)
        kiwoom.set_input_value("수정주가구분", 1)
        kiwoom.comm_rq_data("opt10081_req", "opt10081", 2, "0001")

    return pd.DataFrame(kiwoom.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'], index=kiwoom.ohlcv['date'])

'''
    실시간 TR 받기
    TR_min()

    1. 종목코드 = 전문 조회할 종목코드
    2. 틱범위 = 1:1분, 3:3분, 5:5분, 10:10분, 15:15분, 30:30분, 45:45분, 60:60분
    3. 수정주가구분 = 0 or 1, 수신데이터 1:유상증자, 2:무상증자, 4:배당락, 8:액면분할, 16:액면병합, 32:기업합병, 64:감자, 256:권리락

'''
def TR_min(kiwoom, item_code, tick):
    kiwoom.ohlcv = {'date': [], 'open': [], 'high': [], 'low': [], 'close': [], 'volume': []}
    
    # opt10080 TR 요청 (한번에  900개)
    kiwoom.set_input_value("종목코드", item_code)
    kiwoom.set_input_value("틱범위", tick)
    kiwoom.set_input_value("수정주가구분", 1)
    kiwoom.comm_rq_data("opt10080_req", "opt10080", 0, "0001")

    while kiwoom.remained_data == True:
        # 조건문 추가 (통신량 적게)
        if kiwoom.ohlcv['date'][-1] <=  kiwoom.yyyymmddhhmmss:
            break
        
        time.sleep(TR_REQ_TIME_INTERVAL)
        kiwoom.set_input_value("종목코드", item_code)
        kiwoom.set_input_value("틱범위", tick)
        kiwoom.set_input_value("수정주가구분", 1)
        kiwoom.comm_rq_data("opt10080_req", "opt10080", 2, "0001")

    return pd.DataFrame(kiwoom.ohlcv, columns=['open', 'high', 'low', 'close', 'volume'], index=kiwoom.ohlcv['date'])