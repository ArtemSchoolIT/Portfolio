from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup
from instr import *


class FinalWin(QWidget):
    def __init__(self,exp):
        super().__init__()
        self.exp = exp
        self.set_appear()
        self.index_show()
        self.initUI()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width,win_height)
        self.resize(win_x,win_y)

    def index_show(self):
        self.index = (4*(int(self.exp.res1) + int(self.exp.res2) + int(self.exp.res3)) -200)/10

    def results(self):
        #>15 лет
        if int(self.exp.age) >= 15:
            if self.index >= 15:
                return text_res1
            elif self.index <= 14.9 and self.index >= 11 :
                return text_res2
            elif self.index <= 10.9 and self.index >= 6:
                return text_res3
            elif self.index <= 5.9 and self.index >= 0.5:
                return text_res4
            else:
                return text_res5
        #13-14 лет
        elif int(self.exp.age) >= 13 and int(self.exp.age) <= 14:
            if self.index >= 16.5:
                return text_res1
            elif self.index <= 16.4 and self.index >= 12.5 :
                return text_res2
            elif self.index <= 12.4 and self.index >= 7.5:
                return text_res3
            elif self.index <= 7.4 and self.index >= 2:
                return text_res4
            else:
                return text_res5
        # 11-12 лет
        elif int(self.exp.age) >= 11 and int(self.exp.age) <= 12:
            if self.index >= 18:
                return text_res1
            elif self.index <= 17.9 and self.index >= 14 :
                return text_res2
            elif self.index <= 13.9 and self.index >= 9:
                return text_res3
            elif self.index <= 8.9 and self.index >= 3.5:
                return text_res4
            else:
                return text_res5
        #9-10 лет
        elif int(self.exp.age) >= 9 and int(self.exp.age) <= 10:
            if self.index >= 19.5:
                return text_res1
            elif self.index <= 19.4 and self.index >= 15.5 :
                return text_res2
            elif self.index <= 15.4 and self.index >= 10.5:
                return text_res3
            elif self.index <= 10.4 and self.index >= 5:
                return text_res4
            else:
                return text_res5
        #0-8 лет
        elif int(self.exp.age) >= 0 and int(self.exp.age) <= 8:
            if self.index >= 21:
                return text_res1
            elif self.index <= 20.9 and self.index >= 17 :
                return text_res2
            elif self.index <= 16.9 and self.index >= 12:
                return text_res3
            elif self.index <= 11.9 and self.index >= 6.5:
                return text_res4
            else:
                return text_res5

    def initUI(self):
        if self.index < 0:
            self.text_finalwin = QLabel(txt_finalwin+ '0')
        else:
            self.text_finalwin = QLabel(txt_finalwin+ str(self.index))
        self.text_workheart = QLabel(txt_workheart + self.results())
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text_finalwin,alignment = Qt.AlignCenter)
        self.layout.addWidget(self.text_workheart,alignment = Qt.AlignCenter)
        self.setLayout(self.layout)

    