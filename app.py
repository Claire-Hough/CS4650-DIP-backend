from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import sys

Ui_Dialog, QDialog = loadUiType("app.ui")

class App(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.imageBox.setScaledContents(True)

        self.image = QPixmap('yourImg.jpg')
        self.imgFileName = 'yourImg.jpg'
        self.placeholderFileName = 'yourImg.jpg'
        self.placeholder = QPixmap('yourImg.jpg')
        self.imageBox.setPixmap(self.placeholder)

        self.setWindowTitle("Insta Photo Editor")
        self.timer = QTimer()


        self.importButton.clicked.connect(self.getFile)
        self.exportButton.clicked.connect(self.saveFile)
        self.redSlide.valueChanged.connect(self.redChanged)
        self.greenSlide.valueChanged.connect(self.greenChanged)
        self.blueSlide.valueChanged.connect(self.blueChanged)
        self.sharpSlide.valueChanged.connect(self.sharpChanged)
        self.contrastSlide.valueChanged.connect(self.contrastChanged)
        self.rgbRadio.toggled.connect(self.rgbChecked)
        self.grayscaleRadio.toggled.connect(self.grayscaleChecked)
        self.sizeBox.currentIndexChanged.connect(self.sizeChanged)

    def getFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Image files (*.jpg *.gif)")
        
        if fname != "":
            pixmap = QPixmap(fname)
            self.updateImg(pixmap)
            self.imgFileName = fname
        else:
            self.errorSuccess.setStyleSheet("color: red; font: 12pt; MS Shell Dlg;")
            self.errorSuccess.setText("Error: No filename specified")
            self.timer.timeout.connect(self.onTimeout)
            self.timer.start(5000)

    def saveFile(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save file', 
            'c:\\',"Image files (*.jpg *.gif)")
        if fname == "": 
            self.errorSuccess.setStyleSheet("color: red; font: 12pt; MS Shell Dlg;")
            self.errorSuccess.setText("Error: No filename specified")
            self.timer.timeout.connect(self.onTimeout)
            self.timer.start(5000)
        elif self.imgFileName == self.placeholderFileName:
            self.errorSuccess.setStyleSheet("color: red; font: 12pt; MS Shell Dlg;")
            self.errorSuccess.setText("Error: No image uploaded")
            self.timer.timeout.connect(self.onTimeout)
            self.timer.start(5000)
        else:
            self.image.save(fname)
            self.errorSuccess.setStyleSheet("color: green; font: 12pt; MS Shell Dlg;")
            self.errorSuccess.setText("Successfully saved!")
            self.timer.timeout.connect(self.onTimeout)
            self.timer.start(5000)

    def updateImg(self, pixmap):
        self.image = pixmap
        self.imageBox.setPixmap(pixmap)

    def redChanged(self):
        print("red")

    def greenChanged(self):
        print("green")

    def blueChanged(self):
        print("blue")

    def sharpChanged(self):
        print("sharp")

    def contrastChanged(self):
        print("contrast")

    def rgbChecked(self):
        if self.rgbRadio.isChecked():
            print("rgb")

    def grayscaleChecked(self):
        if self.grayscaleRadio.isChecked():
            print("grayscale")

    def sizeChanged(self):
        print(self.sizeBox.currentText())


    def onTimeout(self):
        self.errorSuccess.setText("")

def main():
    app = QApplication(sys.argv)
    form = App()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
