from PySide.QtCore import *
from PySide.QtGui import *
from PySide.phonon import Phonon
import sys

class MediaPlayer(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Marker Tool')
        self.setGeometry(300, 300, 600, 200)
        self.media_obj = Phonon.MediaObject(self)
        self.timestamp = '00:00.000'
        self.time_ms = 0
        self.playing = False
        self.mdata = []
        self.init_ts()
        self.set_buttons()
        self.installEventFilter(self)
        self.open_file()

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_Space:
                self.play_pause()
            elif key == Qt.Key_W:
                self.set_mark_a()
            elif key == Qt.Key_A:
                self.set_mark_b()
            elif key == Qt.Key_S:
                self.set_mark_c()
            elif key == Qt.Key_D:
                self.set_mark_d()
            elif key == Qt.Key_Escape:
                self.clear_marks()
            return True
        return QWidget.eventFilter(self, widget, event)


    def set_buttons(self):
        self.playButton = QPushButton('Pause', self)
        self.markAButton = QPushButton('A', self)
        self.markBButton = QPushButton('B', self)
        self.markCButton = QPushButton('C', self)
        self.markDButton = QPushButton('D', self)

        self.markAButton.move(100, 0)
        self.markBButton.move(200, 0)
        self.markCButton.move(300, 0)
        self.markDButton.move(400, 0)

        self.playButton.clicked.connect(self.play_pause)
        self.markAButton.clicked.connect(self.set_mark_a)
        self.markBButton.clicked.connect(self.set_mark_b)
        self.markCButton.clicked.connect(self.set_mark_c)
        self.markDButton.clicked.connect(self.set_mark_d)

        self.seeker = QSlider(Qt.Orientation.Horizontal, self)
        self.seeker.setValue(0)
        self.seeker.resize(600,100)
        self.seeker.move(0, 100)
        self.seeker.sliderReleased.connect(self.seeker_update)
        self.seeker.setEnabled(False)

    def clear_marks(self):
        self.mdata = []

    def play_pause(self):
        if self.playing:
            self.playButton.setText('Play')
            self.media_obj.pause()
            self.playing = False
        else:
            self.playButton.setText('Pause')
            self.media_obj.play()
            self.playing = True

    def seeker_update(self):
        time_ms = self.seeker.value()
        self.media_obj.seek(time_ms)
        self.update_ts(time_ms)

    def init_ts(self):
        self.timeDisplay = QLCDNumber(self)
        self.timeDisplay.setDigitCount(9)
        self.timeDisplay.resize(100, 50)
        self.timeDisplay.move(500, 0)
        self.timeDisplay.setSegmentStyle(QLCDNumber.Flat)
        self.timeDisplay.display(self.timestamp)

    def update_ts(self, time_ms):
        self.time_ms = time_ms
        self.timestamp = str(time_ms  % 1000)
        time_ms /= 1000
        self.timestamp = str(time_ms % 60) + '.' + self.timestamp
        time_ms /= 60
        self.timestamp = str(time_ms) + ':' + self.timestamp
        self.timeDisplay.display(self.timestamp)

    def set_mark(self, mark):
        self.mdata.append((int(self.time_ms), mark))
        print 'mark hit %s' % mark

    def set_mark_a(self):
        self.set_mark('a')

    def set_mark_b(self):
        self.set_mark('b')

    def set_mark_c(self):
        self.set_mark('c')

    def set_mark_d(self):
        self.set_mark('d')

    def _time_change(self, time):
        if not self.seeker.isSliderDown():
            self.seeker.setValue(time)
            self.update_ts(time)

    def _total_time_change(self, time):
        self.seeker.setRange(0, time)

    def open_file(self):
        dialog = QFileDialog()
        dialog.setViewMode(QFileDialog.Detail)
        self.filename = dialog.getOpenFileName(self,
             'Open audio file', '/home',
             "Audio Files (*.mp3 *.wav *.ogg)")[0]
        self.audio_output = Phonon.AudioOutput(Phonon.MusicCategory, self)
        Phonon.createPath(self.media_obj, self.audio_output)
        self.media_obj.setCurrentSource(Phonon.MediaSource(self.filename))
        self.media_obj.tick.connect(self._time_change)
        self.media_obj.totalTimeChanged.connect(self._total_time_change)
        self.media_obj.play()
        self.playButton.setText("Pause")
        self.seeker.setEnabled(True)
        self.playing = True

    def store_mdata(self):
        print self.mdata
        f = open((self.filename + '.mdata'), 'w')
        for inst in self.mdata:
            f.write('%s %s\n' % inst)
        f.close()


if __name__ == '__main__':
    try:
        myApp = QApplication(sys.argv)
        myWindow = MediaPlayer()
        myWindow.show()
        myApp.exec_()
        myWindow.mdata.sort(key=lambda tup: tup[0])
        myWindow.store_mdata()
        sys.exit(0)
    except Exception, e:
        print 'Error', e
        pass
