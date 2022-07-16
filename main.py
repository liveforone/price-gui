import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pykorbit

form_class = uic.loadUiType("bit.ui")[0]

"""
윈도우 gui 세팅 -> 크기, 제목, 아이콘, 버튼
"""
class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.inquiry)

    def inquiry(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        price = pykorbit.get_current_price("BTC")
        self.lineEdit.setText(str(price)) #float -> str로 형변환

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()