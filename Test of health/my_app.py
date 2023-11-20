from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QButtonGroup, QLineEdit
from instr import *
from second_win import *
from final_win import *


class Main_win(QWidget):
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
        self.hello_text = QLabel(txt_hello)
        self.but_next = QPushButton(txt_next)
        self.txt_instruction = QLabel(txt_instruction)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.hello_text,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.txt_instruction,alignment = Qt.AlignLeft)
        self.layout.addWidget(self.but_next,alignment = Qt.AlignLeft)
        self.setLayout(self.layout)

    def next_click(self):
        self.tw = TextWin()
        self.hide()

    def connects(self):
        self.but_next.clicked.connect(self.next_click)


app = QApplication([])
mw = Main_win()
app.exec_()
