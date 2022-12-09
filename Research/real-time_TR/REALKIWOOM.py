import sys 
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
import datetime
from cost import *



class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real")
        self.setGeometry(300, 300, 300, 400)

        self.universe_realtime_transaction_info = {}

        btn = QPushButton("Register", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clicked)

        btn2 = QPushButton("DisConnect", self)
        btn2.move(20, 100)
        btn2.clicked.connect(self.btn2_clicked)

        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)
        self.ocx.OnReceiveRealData.connect(self._on_receive_real_data)
        self.CommmConnect()

    def btn_clicked(self):
        self.SetRealReg("1000", "005930", "20", 0)
        #self.SetRealReg("2000", "", "215;20;214", 0)
        print("called\n")

    def btn2_clicked(self):
        self.DisConnectRealData("1000")

    def CommmConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.statusBar().showMessage("login 중 ...")

    def _handler_login(self, err_code):
        if err_code == 0:
            self.statusBar().showMessage("login 완료")


    def _handler_real_data(self, code, real_type, data):
        print(code, real_type, data)
        if real_type == "장시작시간":
            gubun =  self.GetCommRealData(code, 215)
            remained_time =  self.GetCommRealData(code, 214)
            print(gubun, remained_time)            


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

            print(signed_at, close, high, open, low, accum_volume)

            if code not in self.universe_realtime_transaction_info:
                self.universe_realtime_transaction_info.update({code: {}})

            self.universe_realtime_transaction_info[code].update({
                "체결시간": signed_at,
                "시가": open,
                "고가": high,
                "저가": low,
                "현재가": close,
                "누적거래량": accum_volume
            })

            def get_fid(search_value):
                keys = [key for key, value in FID_CODES.items() if value == search_value]
                return keys[0]



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    
    app.exec_()