import sys
from static_kiwoom import *
from tool import retrieveTR
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

if __name__ == "__main__":

    app = QApplication(sys.argv)
    kiwoom = Kiwoom()

    kiwoom.comm_connect()
    
    """ 
    1.
    조회 정보 가져오기 (DB에서)
    어떤 코드..? 날짜 어느 시점부터부터..?
    """
    # 주식 코드번호 가져오기
    item_code = "069500"

    # 날짜 정하기 (DB 존재 여부에 따라)
    # Opt1. (DB 생성 X): 해당 코드를 처음 접속한 것
    before_1_year = (datetime.today() - relativedelta(years=1)).strftime('%Y%m%d') + '000000'   # now = datetime.now().strftime('%Y%m%d%H%M%S')
    # Opt2. (DB 생성 O): 해당 코드에 접속한 적 있음. DB-update date를 받아옴 
    kiwoom.yyyymmddhhmmss = "20220518153000"

    """
    2.
    조회 시작
    조회 데이터 저장 (아직 미완)
    """
    df = retrieveTR.TR_min(kiwoom, item_code, 1)
    print(df)

    


    
