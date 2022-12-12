# from pykiwoom.kiwoom import *
from real_kiwoom import Kiwoom

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

order = 0

if order == 0:
    kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")
elif order ==1 :
    kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, "005930", 10, 0, "03", "")
elif order == 2 :
    pass


def pyTrader(stock_account, order_type, code, order_quantity, order_price, order_classification, origin_order_number):
    if order_type == 0:
        if order_classification == "03":
            kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, code, order_quantity, 0, "03", "")
        elif order_classification == "00":
             kiwoom.SendOrder("지정가매수", "0101", stock_account, 1, code, order_quantity, order_price, "00", "")

    elif order_type ==1:
        if order_classification == "03":
             kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, code, order_quantity, 0, "03", "")
        elif order_classification == "00":
             kiwoom.SendOrder("지정가매도", "0101", stock_account, 2, code, order_quantity, order_price, "00", "")

    elif order_type == 2:
        pass

pyTrader(stock_account, 1, "069500", "100", 0, "03", "" )