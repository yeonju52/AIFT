import sys
from static_kiwoom import *
from tool import retrieveTR
from tool import manageDB
import pandas as pd
from datetime import datetime

# 주식 코드번호 
# company_info의 PRIMARY KEY 이자, query의 TABLE NAME
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
    kiwoom.upperBound = datetime.today().strftime('%Y%m%d') + '000000' # 오늘 00시 00분 전까지
    for i in range(len(st_code)):   # 없으면 IndexError: list index out of range
        if last_update[i] > kiwoom.upperBound:
            continue
        kiwoom.lowerBound = last_update[i]

        dt_start = datetime.now().strftime('%Y%m%d%H%M%S')
        df = retrieveTR.TR_min(kiwoom, st_code[i], 1)
        # sql로 저장
        sql.set_query(st_code[i], df)
        # 조회 정보 가져오기 (정보 코드와 정보 코드명), last_update를 업데이트
        sql.update_comany_info([st_code[i], kiwoom.get_master_code_name(st_code[i]), dt_start])
        
    
