{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "from PyQt5.QtWidgets import *\n",
    "from PyQt5.QtGui import *\n",
    "from PyQt5.QAxContainer import *\n",
    "\n",
    "class MyWindow(QMainWindow):\n",
    "    def __init__(self):\n",
    "        super().__init__()\n",
    "        self.setWindowTitle(\"PyStock\")\n",
    "        self.setGeometry(300, 300, 300, 150)\n",
    "\n",
    "        self.kiwoom = QAxWidget(\"KHOPENAPI.KHOpenAPICtrl.1\")\n",
    "\n",
    "        btn1 = QPushButton(\"Login\", self)\n",
    "        btn1.move(20, 20)\n",
    "        btn1.clicked.connect(self.btn1_clicked)\n",
    "\n",
    "        btn2 = QPushButton(\"Check state\", self)\n",
    "        btn2.move(20, 70)\n",
    "        btn2.clicked.connect(self.btn2_clicked)\n",
    "\n",
    "    def btn1_clicked(self):\n",
    "        ret = self.kiwoom.dynamicCall(\"CommConnect()\")\n",
    "\n",
    "    def btn2_clicked(self):\n",
    "        if self.kiwoom.dynamicCall(\"GetConnectState()\") == 0:\n",
    "            self.statusBar().showMessage(\"Not connected\")\n",
    "        else:\n",
    "            self.statusBar().showMessage(\"Connected\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app = QApplication(sys.argv)\n",
    "    myWindow = MyWindow()\n",
    "    myWindow.show()\n",
    "    app.exec_()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.8.13 ('AIFT2022')",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "0a27c5ebec152789ea3ce4d4f8bbf956dd396bd25302156e0d286449572054d6"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
