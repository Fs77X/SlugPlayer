import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
import os
import vlc
from VLCManager import VLCManager


class window(QtWidgets.QMainWindow):    
    def __init__(self):
        super(window, self).__init__()
        mylist = self.getList()
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        mylist2 = os.listdir(scriptDir + "/songs")

        if mylist != -1:
            self._manager = VLCManager(0, 0, mylist, mylist2, len(mylist))
            self._manager.setFileName(mylist[0])
            self.setWindowTitle('SlugPlayer')
            self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'slug.png'))


            extractAction = QAction('&Quit', self)
            extractAction.setShortcut('Ctrl+Q')
            extractAction.triggered.connect(self.close)

            self.statusBar()

            mainMenu = self.menuBar()
            fileMenu = mainMenu.addMenu('&File')
            fileMenu.addAction(extractAction)

            self.home()
        else:
            self.setWindowTitle("ERROR404")
            self.setGeometry(200, 100, 300, 100) #x, y (where it initially opens on screen) w, h (size of window)
            self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + 'cyber-slugeditnotallowed.png'))
            self.setFixedSize(self.size())
            self.error()


    def home(self):
    
        # quitbtn = QtWidgets.QPushButton('Quit')
        # quitbtn.clicked.connect(self.close)

        playbtn = QtWidgets.QPushButton('Play')
        playbtn.clicked.connect(self._manager.play)
        

        psebtn = QtWidgets.QPushButton('Pause', self)
        psebtn.clicked.connect(self._manager.pause)

        stopbtn = QtWidgets.QPushButton('Stop', self)
        stopbtn.clicked.connect(self._manager.stop)

        nextbtn = QtWidgets.QPushButton('Next', self)
        nextbtn.clicked.connect(self._manager.next)
        prevbtn = QtWidgets.QPushButton('Prev', self)
        prevbtn.clicked.connect(self._manager.prev)

        self.playing = QtWidgets.QLabel()
        self.playing.setText("Nothing Playing")
        # self.currentP = QtWidgets.QLabel()
        # self.currentP.setText("0:00:00")
        
        # self.remP = QtWidgets.QLabel()
        # self.remP.setText("-0:00:00")
        self._manager.songChanged.connect(self.playing.setText)

        self.sl = QtWidgets.QSlider(orientation=QtCore.Qt.Horizontal)
        self.sl.setFocusPolicy(QtCore.Qt.NoFocus)
        self._manager.durationChanged.connect(self.sl.setMaximum)
        self._manager.positionChanged.connect(self.sl.setValue)


        # grid = QGridLayout()

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)

        hlay = QtWidgets.QHBoxLayout()
        for b in (prevbtn, playbtn, psebtn, stopbtn, nextbtn ): #prevbtn, playbtn, psebtn, stopbtn, nextbtn 
            hlay.addWidget(b)
        lay.addLayout(hlay)
        lay.addWidget(self.sl)
        # central_widget2 = QtWidgets.QWidget()
        # self.setCentralWidget(central_widget2)
        # lay2 = QtWidgets.QVBoxLayout()
        # lay2.addLayout(lay)
        # lay2.addWidget(self.currentP)
        lay.addWidget(self.playing)
        self.sl.valueChanged[int].connect(self._manager.setPosition)
        self.show()

    def error(self):
        quitbtn = QtWidgets.QPushButton('quit')
        quitbtn.clicked.connect(self.close)

        Error = QtWidgets.QLabel()
        Error.setText("Error 404: No music sound")
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QVBoxLayout(central_widget)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(quitbtn)
        lay.addLayout(hlay)
        lay.addWidget(Error)
        self.show()


    # def keyPressEvent(self, event):
    #     if event.key() == Qt.Key_Right:
    #         self.sl.setValue(self.sl.value() + 5000)
    #     elif event.key() == Qt.Key_Left:
    #         self.s1.setValue(self.s1.value() - 5000)
    #     else:
    #         QWidget.keyPressEvent(self,event)




    def getList(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        mylist = os.listdir(scriptDir + "/songs")
        if not mylist:
            return -1
        else:
            length = len(mylist)
            for x in range(length):
                mylist[x] = "/songs/" + mylist[x]
            return mylist

def run():
    app = QtWidgets.QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())

run()