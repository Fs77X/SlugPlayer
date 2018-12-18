import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import vlc

player = vlc.MediaPlayer("/songs/Immigrant Song.mp3")
class window(QMainWindow):
    

    def __init__(self):
        super(window, self).__init__()
        self.setGeometry(50, 50, 400, 200)
        self.setWindowTitle('SlugPlayer')
        #self.setWindowIcon(QIcon('pic.png'))
        
        self.home()

    def home(self):
        btn = QPushButton('quit', self)
        btn.clicked.connect(self.close_application)

        btn.resize(btn.sizeHint())  #set to acceptable size automatic
        btn.move(0, 0)

        playbtn = QPushButton('Play', self)
        
        playbtn.clicked.connect(self.play_music)

        playbtn.resize(playbtn.sizeHint())
        playbtn.move(100, 0)

        psebtn = QPushButton('Pause', self)
        
        psebtn.clicked.connect(self.pause_music)

        psebtn.resize(psebtn.sizeHint())
        psebtn.move(200, 0)

        stopbtn = QPushButton('Stop', self)
        
        stopbtn.clicked.connect(self.stop_music)

        stopbtn.resize(stopbtn.sizeHint())
        stopbtn.move(300, 0)



        self.show()

    def close_application(self):
        sys.exit()

    def play_music(self):
        player.play()


    def pause_music(self):
        player.pause()

    def stop_music(self):
        player.stop()

def run():
    app = QApplication(sys.argv)
    Gui = window()
    sys.exit(app.exec_())
   

run()
