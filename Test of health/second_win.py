from PyQt5 import QtGui
from PyQt5.QtCore import  Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup, QLineEdit
from instr import *
from final_win import *


class TextWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()

    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.move(win_width,win_height)
        self.resize(win_x,win_y)

    def initUI(self):
        #Labels
        self.txt_name = QLabel(txt_name)
        self.txt_age = QLabel(txt_age)
        self.text_timer = QLabel()
        self.txt_test1 = QLabel(txt_test1)
        self.txt_test2 = QLabel(txt_test2)
        self.txt_test3 = QLabel(txt_test3)
        #PushButtons
        self.but_results = QPushButton(txt_sendresults)
        self.but_starttest1 = QPushButton(txt_starttest1)
        self.but_starttest2 = QPushButton(txt_starttest2)
        self.but_starttest3 = QPushButton(txt_starttest3)
        #LineEdits
        self.hintname = QLineEdit(txt_hintname)
        self.hintage = QLineEdit(txt_hintage)
        self.hinttest1 = QLineEdit(txt_hinttest1)
        self.hinttest2 = QLineEdit(txt_hinttest2)
        self.hinttest3 = QLineEdit(txt_hinttest3)

        self.line1y = QVBoxLayout()
        self.line2y = QVBoxLayout()
        self.linex = QHBoxLayout()
        self.line1y.addWidget(self.txt_name,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hintname,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_age,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hintage,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_test1,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest1,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest1,alignment = Qt.AlignLeft)

        self.line2y.addWidget(self.text_timer,alignment= Qt.AlignCenter)

        self.line1y.addWidget(self.txt_test2,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest2,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest2,alignment = Qt.AlignLeft)

        self.line1y.addWidget(self.txt_test3,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.but_starttest3,alignment = Qt.AlignLeft)
        self.line1y.addWidget(self.hinttest3,alignment = Qt.AlignLeft)
        
        self.line1y.addWidget(self.but_results,alignment = Qt.AlignCenter)
        self.linex.addLayout(self.line1y)
        self.linex.addLayout(self.line2y)
        self.setLayout(self.linex)

    def timer_test(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)

    def timer_sits(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)

    def timer_final(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)

    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QtGui.QFont('Times', 36, QtGui.QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss')[6:8])
        self.text_timer.setFont(QtGui.QFont('Times', 36, QtGui.QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        self.text_timer.setFont(QtGui.QFont('Times', 36, QtGui.QFont.Bold))
        self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if int(time.toString('hh:mm:ss')[6:8]) >= 45 or int(time.toString('hh:mm:ss')[6:8]) <= 15:
            self.text_timer.setStyleSheet('color: rgb(0, 255, 0)')
        else:
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')

        if time.toString('hh:mm:ss') == '00:00:00':
            self.timer.stop()

    def final_click(self):
        self.hide()
        self.exp = Experiment(self.hintage.text(),self.hinttest1.text(),self.hinttest2.text(),self.hinttest3.text())
        #self.exp.results()
        self.fw = FinalWin(self.exp)

    def connects(self):
        self.but_results.clicked.connect(self.final_click)
        self.but_starttest1.clicked.connect(self.timer_test)
        self.but_starttest2.clicked.connect(self.timer_sits)
        self.but_starttest3.clicked.connect(self.timer_final)

class Experiment():
    def __init__(self,age,test1,test2,test3):
        self.age = age
        self.res1 = test1
        self.res2 = test2
        self.res3 = test3