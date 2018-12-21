import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import vlc
from random import *

class VLCManager(QtCore.QObject):
    durationChanged = QtCore.pyqtSignal(int)
    positionChanged = QtCore.pyqtSignal(int)

    def __init__(self, indexpl, is_playing, mylist, parent=None):
        super(VLCManager, self).__init__(parent)
        self._player = vlc.MediaPlayer()
        self._timer = QtCore.QTimer(self, interval=100, timeout=self.update_values)
        self._indexpl = indexpl
        self._is_playing = is_playing
        self._mylist = mylist

    def setFileName(self, filename):
        self._player = vlc.MediaPlayer(filename)

    def position(self):
        self.durationChanged.emit(self.duration())
        return self._player.get_time()

    def setPosition(self, time):
        if self.position() != time:
            self._player.set_time(time)

    @QtCore.pyqtSlot()
    def update_values(self):
        self.positionChanged.emit(self.position())

    def duration(self):
        return self._player.get_length()

    @QtCore.pyqtSlot()
    def play(self):
        self._player.play()
        self.update_values()
        self._timer.start()

    @QtCore.pyqtSlot()
    def pause(self):
        self._player.pause()
        self.update_values()
        self._timer.stop()

    @QtCore.pyqtSlot()
    def stop(self):
        self._player.stop()
        self.update_values()
        self._timer.stop()

    def test1(self):
        print(self._indexpl)

    def test2(self):
        print(self._is_playing)

    def test3(self):
        print(self._mylist)

    def randomize(self):
        self._is_playing = randint(10, 100)
        self._indexpl = random()
        self._mylist = randint(0,5)