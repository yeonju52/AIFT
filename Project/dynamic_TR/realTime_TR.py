import sys 
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from dynamic_TR.const import *

realtime_transaction_info = {}
code_list = "069500"

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveRealData.connect(self._on_receive_real_data)
        self.CommmConnect()

    def CommmConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        print("login 중 ...")

    def _handler_login(self, err_code):
        if err_code == 0:
            print("login 완료")
            print("call\n")
            self.SetRealReg("2000", code_list, "215;20;214", 0)  


    def SetRealReg(self, screen_no, code_list, fid_list, real_type):
        self.ocx.dynamicCall("SetRealReg(QString, QString, QString, QString)", 
                              screen_no, code_list, fid_list, real_type)

    def DisConnectRealData(self, screen_no):
        self.ocx.dynamicCall("DisConnectRealData(QString)", screen_no)

    def GetCommRealData(self, code, fid):
        data = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, fid) 
        return data

    def _on_receive_real_data(self, code, real_type, data):
        if real_type == "장시작시간":
            pass
            gubun =  self.GetCommRealData(code, 215)
            remained_time =  self.GetCommRealData(code, 214)
            print(gubun, remained_time)
            if gubun == 4:
                self.DisConnectRealData("2000")

        elif real_type == "주식체결":
            signed_at = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 20)

            close = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 10)
            close = abs(int(close))

            high = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 17)
            high = abs(int(high))

            open = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 16)
            open = abs(int(open))

            low = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 18)
            low = abs(int(low))

            accum_volume = self.ocx.dynamicCall("GetCommRealData(QString, int)", code, 13)
            accum_volume = abs(int(accum_volume))

            print(code, signed_at, close, high, open, low, accum_volume)

            if code not in realtime_transaction_info:
                realtime_transaction_info.update({code: {}})

            realtime_transaction_info[code].update({
                "체결시간": signed_at,
                "시가": open,
                "고가": high,
                "저가": low,
                "현재가": close,
                "누적거래량": accum_volume
            })
            
    def return_data(code):
        data = [value for value, key in realtime_transaction_info.items() if key == code]
        return data[0:]
            

app = QApplication(sys.argv)
kiwoom = Kiwoom()

app.exec_()