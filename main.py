import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen, QBrush
from PyQt5.QtWidgets import QApplication, QMainWindow


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)


    def paintEvent(self,event):
        if self.do_paint:
            painter = QPainter(self)
            painter.setBrush(QBrush(QColor("#c56c00")))
            painter.drawEllipse(randint(0,781), randint(0,431), 200, 200)

            painter.end()

    def paint(self):
        self.do_paint = True
        self.repaint()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPage()

    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())