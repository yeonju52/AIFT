import sys
from static_kiwoom import *
from tool import retrieveTR
from tool import manageDB
import pandas as pd

# 주식 코드번호 가져오기 (.py로 보여주기)
# dictionary 순서 기억함
# { # company_info의 PRIMARY KEY 이자, query의 TABLE NAME
#     '069500',   # : 'kodex_200',
#     '114800',   # : 'kodex_inverse',
#     '226490'    # : 'kodex_kospi'    
# }

st_code = ['069500', '114800', '226490']
nm_code = ['kodex_200', 'kodex_inverse', 'kodex_kospi']

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    
    """ 
    1.
    조회 정보 가져오기 (DB에서)
    어떤 코드..? 날짜 어느 시점부터부터..?
    """
    # 1. 조회 정보 가져오기 (DB 저장, 이전 조회 정보) : 해당 코드에 정보 없으면 1년전 00시 00분 반환
    sql_company_info = manageDB.sqlReader()
    last_update = sql_company_info.get_last_update(st_code)

    """
    2.
    조회 시작
    조회 데이터 저장 (아직 미완)
    """

    for i in range(len(st_code)):
        kiwoom.yyyymmddhhmmss = last_update[i]
        df = retrieveTR.TR_min(kiwoom, st_code[i], 1)
        print(df, '\n')

    


    
