import sys
from static_kiwoom import *
from tool import retrieveTR
import pandas as pd
import sqlite3

# TR_REQ_TIME_INTERVAL = 0.2
if __name__ == "__main__":
    
    """
    <connect>: Kiwoom->kiwoom, sqlite3->sql
    """
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    sql = sqlite3.connect("kiwoom.db")
    
    """
    <data provider> and <save_sql>
    """
    # tr_dic = {
    #     'opt10080': {'069500':'kodex_200', '114800':'kodex_inverse', '226490':'kodex_kospi'}
    # }
    item_code = "069500"
    df = retrieveTR.TR_day(kiwoom, item_code, "20180224")
    df.to_sql(item_code, sql, if_exists='append')