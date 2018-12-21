import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import vlc
from VLCManager import VLCManager


class window(QtWidgets.QMainWindow):    
    def __init__(self):
        super(window, self).__init__()
        idx = 0

        self._manager = VLCManager(0, 0, 0)
        self._manager.setFileName("/songs/Immigrant Song.mp3")
        self.setWindowTitle('SlugPlayer')
        self.home()

    def home(self):
        quitbtn = QtWidgets.QPushButton('quit')
        quitbtn.clicked.connect(self.close)

        playbtn = QtWidgets.QPushButton('Play')
        playbtn.clicked.connect(self._manager.play)

        psebtn = QtWidgets.QPushButton('Pause', self)
        psebtn.clicked.connect(self._manager.pause)

        stopbtn = QtWidgets.QPushButton('Stop', self)
        stopbtn.clicked.connect(self._manager.stop)

        test1 = QtWidgets.QPushButton('Test1', self)
        test1.clicked.connect(self._manager.test1)

        test2 = QtWidgets.QPushButton('Test2', self)
        test2.clicked.connect(self._manager.test2)

        test3 = QtWidgets.QPushButton('Test3', self)
        test3.clicked.connect(self._manager.test3)
        rand = QtWidgets.QPushButton('Random', self)
        rand.clicked.connect(self._manager.randomize)

        self.sl = QtWidgets.QSlider(orientation=QtCore.Qt.Horizontal)
        self.sl.setFocusPolicy(QtCore.Qt.NoFocus)
        self._manager.durationChanged.connect(self.sl.setMaximum)
        self._manager.positionChanged.connect(self.sl.setValue)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)

        hlay = QtWidgets.QHBoxLayout()
        for b in (quitbtn, playbtn, psebtn, stopbtn, test1, test2, test3, rand ):
            hlay.addWidget(b)
        lay.addLayout(hlay)
        lay.addWidget(self.sl)
        self.sl.valueChanged[int].connect(self._manager.setPosition)
        self.show()

def run():
    app = QtWidgets.QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()