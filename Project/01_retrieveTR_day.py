import sys
from pykiwoom import *
from tool import retrieveTR
import pandas as pd
import sqlite3

# TR_REQ_TIME_INTERVAL = 0.2
if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    item_code = "069500"
    df = retrieveTR.TR_day(kiwoom, item_code, "20170224")
    print(df)

    # con = sqlite3.connect("kiwoom_" + item_code)
    # df.to_sql('069500', con, if_exists='append')