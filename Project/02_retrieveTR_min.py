import sys
from pykiwoom import *
from tool import retrieveTR
import pandas as pd

'''
횟수 제한 안내
https://kminito.tistory.com/35
'''
# TR_REQ_TIME_INTERVAL = 0.2
if __name__ == "__main__":
    app = QApplication(sys.argv)
    kiwoom = Kiwoom()
    kiwoom.comm_connect()

    item_code = "069500"
    df = retrieveTR.TR_min(kiwoom, item_code, "0", 1)
    print(df)

    