import random
from realTime_TR import *
from pytrader import *


code = "0000" # 주식종목 코드

real_data = kiwoom.return_data(code)

def model(real_data):
    
    x = random.randint(0, 3)
    order_quantity = random.randint(0, 10)

    pyTrader(stock_account, x, code, order_quantity, 0, "03", "")
    return x

