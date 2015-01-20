
from PyQt4 import QtGui, QtCore

class Interface(QtGui.QWidget):
    def __init__(self):
        super(Interface, self).__init__()
        self.initUI()

    def initUI(self):
        quitbtn = QtGui.QPushButton('Quit', self)
        quitbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        quitbtn.resize(quitbtn.sizeHint())
        quitbtn.move(50, 50)

        self.resize(600, 480)
        self.center()
        self.setWindowTitle('Genome Data Parser')
        self.setWindowIcon(QtGui.QIcon('icon.gif'))
        self.show()

    def center(self):
        window_frame = self.frameGeometry()
        screen_res = QtGui.QDesktopWidget().availableGeometry().center()
        window_frame.moveCenter(screen_res)
        self.move(window_frame.topLeft())