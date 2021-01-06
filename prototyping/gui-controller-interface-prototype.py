import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tetris - button inputs'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()
        self.move(700, 300)
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button = QPushButton('Soft/Fast Drop', self)
        button.setToolTip('Drop blocks at faster speeds')
        button.move(100,140)
        button.clicked.connect(self.soft_drop_clicked)

        button = QPushButton('Normal Drop', self)
        button.setToolTip('Drop blocks at speed of gravity G')
        button.move(100,70)
        button.clicked.connect(self.normal_drop_clicked)
        
        button = QPushButton('Hard Drop', self)
        button.setToolTip('Instantaneously drop block to the ground.')
        button.move(100,100)
        button.clicked.connect(self.hard_drop_clicked)

        button = QPushButton('Move right', self)
        button.setToolTip('Move block/cursor a space right.')
        button.move(180,100)
        button.clicked.connect(self.right_clicked)

        button = QPushButton('Move left', self)
        button.setToolTip('Move block/cursor a space left.')
        button.move(20,100)
        button.clicked.connect(self.left_clicked)

        self.show()

    @pyqtSlot()
    def soft_drop_clicked(self):
        print('set to soft drop')
    @pyqtSlot()
    def normal_drop_clicked(self):
        print('set to normal drop')
    @pyqtSlot()
    def hard_drop_clicked(self):
        print('set to hard drop')
    @pyqtSlot()
    def left_clicked(self):
        print('move left')
    @pyqtSlot()
    def right_clicked(self):
        print('move right')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())