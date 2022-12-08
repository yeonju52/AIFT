import sys
from static_kiwoom import *
from tool import retrieveTR
# from tool import manageDB

import sqlite3
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

st_code = ['069500', '114800', '226490']
nm_code = ['kodex_200', 'kodex_inverse', 'kodex_kospi']

if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    sql = sqlite3.connect("kiwoom.db")

    before_1_year = (datetime.today() - relativedelta(years=1)).strftime('%Y%m%d') + '000000'
    kiwoom.yyyymmddhhmmss = before_1_year
    df = retrieveTR.TR_min(kiwoom, '069500', 60)

    # df.to_sql('069500_60', sql, if_exists='append')
    df.index.name = 'date'
    df.reset_index()
    print(df.index)
    print(df)
    # df.to_csv('data/069500_60.csv')
    
    

    


    
