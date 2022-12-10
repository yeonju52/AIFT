import sys
from static_kiwoom import *
from tool import retrieveTR
from tool import manageDB
import pandas as pd
from datetime import datetime, timedelta

# 주식 코드번호 
st_code = ['069500', '114800', '226490']

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    
    """ 
    1.
    조회 정보 가져오기 (DB에서)
    어떤 코드..? 날짜 어느 시점부터부터..?
    """
    # 조회 정보 가져오기 (DB = 이전 조회 정보) : 해당 코드에 정보 없으면 1년전 00시 00분 반환
    sql = manageDB.sqlReader()
    last_update = sql.get_last_update(st_code)
    print(last_update)
    
    """
    2.
    키움 조회 시작
        - 조회하고 싶은 날짜의 조건
            date : lowerBound < date < upperBound
            1) lowerBound는 DB에서 받고, (코드마다 last update date가 다를 수 있음)
            2) upperBound는 조회 시점 날짜의 정각으로 설정한다.
        
    조회 데이터 저장 (아직 미완)
    - 조회 데이터 저장 (update): 조회하고자 하는 sql query는 미리 만들어놈 init과 동시에
    - company_info 저장 (update)
    """
    # lowerBound : kiwoom.lowerBound   
    # upperBound : kiwoom.upperBound
    # 시간 외 단일가까지 ~18시 : https://contents.premium.naver.com/finup/moneysurfer/contents/220523153223136wv
    kiwoom.upperBound = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d') + '150000' # 오늘 00시 00분 전까지
    for i in range(len(st_code)):   # 없으면 IndexError: list index out of range
        kiwoom.lowerBound = last_update[i]    # remained_data일 때까지 받고 싶다면, '0'을 할당하면 됌
        # 새로운 데이터가 있는 경우 upperBound와 같거나 적을 때,
        if kiwoom.lowerBound >= kiwoom.upperBound:  # 새로 업데이트 된 데이터가 없음: 키움 분봉 조회 실행 X
            continue
        else:
            df = retrieveTR.TR_min(kiwoom, st_code[i], 60)  # 60분봉으로 변경
            sql.set_query(st_code[i], df) # sql로 저장
            # last_update를 업데이트, 조회 정보 가져오기 (정보 코드와 정보 코드명), 
            sql.update_comany_info([st_code[i], kiwoom.get_master_code_name(st_code[i]), df['date'][0]])