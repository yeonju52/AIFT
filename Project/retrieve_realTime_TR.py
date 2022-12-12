import sys
from static_TR.static_kiwoom import *
from tool import manageDB
import pandas as pd
from datetime import datetime, timedelta
import pandas as pd

from dynamic_TR.realTime_TR import *
from dynamic_TR.pytrader import *

# 주식 코드번호 
# company_info의 PRIMARY KEY 이자, query의 TABLE NAME
st_code = ['069500', '114800', '226490']

if __name__ == "__main__":
    kiwoom = Kiwoom()   # 이름 혹시모르니 변경생각해보자
    
    for code in st_code:
        real_data = kiwoom.return_data(code)    # 실시간 데이터 받음
        print(real_data)