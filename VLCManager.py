import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import vlc

# next = "/songs/SampleAudio_0.4mb.mp3"


class VLCManager(QtCore.QObject):
    durationChanged = QtCore.pyqtSignal(int)
    positionChanged = QtCore.pyqtSignal(int)
    songChanged = QtCore.pyqtSignal(str)

    def __init__(self, indexpl, is_playing, mylist, mylist2, length, parent=None):
        super(VLCManager, self).__init__(parent)
        self._player = vlc.MediaPlayer()
        self._timer = QtCore.QTimer(
            self, interval=100, timeout=self.update_values)
        self._timer2 = QtCore.QTimer(
            self, interval=400, timeout=self.autoPlay_next)
        self._timer3 = QtCore.QTimer(self, interval = 100, timeout=self.update_song)
        self._indexpl = indexpl
        self._is_playing = is_playing
        self._mylist = mylist
        self._length = length
        self._mylist2 = mylist2

    def setFileName(self, filename):
        self._player = vlc.MediaPlayer(filename)

    def getSong(self):
        return self._mylist2[self._indexpl]
    
    @QtCore.pyqtSlot()
    def update_song(self):
        self.songChanged.emit(self.getSong())


    def position(self):  # updates time when playing through file in ms
        self.durationChanged.emit(self.duration())
        return self._player.get_time()

    def setPosition(self, time):  # moving time
        if self.position() != time:
            self._player.set_time(time)

    @QtCore.pyqtSlot()
    def update_values(self):
        self.positionChanged.emit(self.position())

    def duration(self):  # gets the duration of whole audio file inms
        return self._player.get_length()

    def checkStopped(self):
        if self._is_playing == 1 and self._player.is_playing == 0:
            print("woot")

    @QtCore.pyqtSlot()
    def play(self):
        self._is_playing = 1
        self._player.play()
        self.update_values()
        self._timer.start()
        self._timer2.start()
        self.update_song()
        self._timer3.start()

    @QtCore.pyqtSlot()
    def pause(self):
        self._player.pause()
        self.update_values()
        self._timer.stop()
        self._timer2.stop()
        self.update_song()
        self._timer3.stop()

    @QtCore.pyqtSlot()
    def stop(self):
        self._player.stop()
        self.update_values()
        self._timer.stop()
        self._timer2.stop()
        self.update_song()
        self._timer3.stop()

    def autoPlay_next(self):
        # print(self._timer2.isActive())
        if self._player.is_playing() == 0 and self._is_playing == 1:
            if self._indexpl == self._length - 1:  # reached end of playlist
                self._indexpl = 0
                self.setFileName(self._mylist[self._indexpl])
                self.play()
            else:
                self._indexpl = self._indexpl + 1  # havne't reachd end of playlist
                self.setFileName(self._mylist[self._indexpl])
                self.play()

    def next(self):
        self.stop()
        if self._indexpl == self._length - 1:  # reached end of playlist
            self._indexpl = 0
            self.setFileName(self._mylist[self._indexpl])
            self.play()
        else:
            self._indexpl = self._indexpl + 1  # havne't reachd end of playlist
            self.setFileName(self._mylist[self._indexpl])
            self.play()

    def prev(self):
        self.stop()
        if self._indexpl == 0:
            self._indexpl = self._length - 1
            self.setFileName(self._mylist[self._indexpl])
            self.play()
        else:
            self._indexpl = self._indexpl - 1
            self.setFileName(self._mylist[self._indexpl])
            self.play()
        # self.stop()
        # self.setFileName()
        # self.play()

        # self.stop()
        # self.setFileName(self._mylist)
        # self.play()

    # def test2(self):
    #     print(self._is_playing)

    # def test3(self):
    #     print(self._mylist)

    # def keyPressed(self, event):

    # def randomize(self):
    #     self._is_playing = randint(10, 100)
    #     self._indexpl = random()
    #     self._mylist = randint(0,5)
