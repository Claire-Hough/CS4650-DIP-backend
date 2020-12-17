from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import cv2
import time
# import numpy as np
# import matplotlib.pyplot as plt
import sys
from backend import *

Ui_Dialog, QDialog = loadUiType("app.ui")

class App(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.imageBox.setScaledContents(True)

        #self.image = QPixmap('yourImg.jpg')
        self.img = cv2.imread('yourImg.jpg')
        self.imgFileName = 'yourImg.jpg'
        self.placeholderFileName = 'yourImg.jpg'
        #self.placeholder = QPixmap('yourImg.jpg')
        self.placeholder = cv2.imread('yourImg.jpg')

        height, width, channel = self.placeholder.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.placeholder.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()

        self.imageBox.setPixmap(QPixmap(qImg))

        self.setWindowTitle("Insta Photo Editor")
        self.timer = QTimer()


        self.importButton.clicked.connect(self.getFile)
        self.exportButton.clicked.connect(self.saveFile)
        self.redSlide.valueChanged.connect(self.redChanged)
        self.redSlide.setMaximum(200)
        self.greenSlide.valueChanged.connect(self.greenChanged)
        self.greenSlide.setMaximum(200)
        self.blueSlide.valueChanged.connect(self.blueChanged)
        self.blueSlide.setMaximum(200)
        self.sharpSlide.toggled.connect(self.sharpChanged)
        self.blurSlide.toggled.connect(self.blurChanged)
        self.rgbRadio.toggled.connect(self.rgbChecked)
        self.grayscaleRadio.toggled.connect(self.grayscaleChecked)
        self.sizeBox.currentIndexChanged.connect(self.sizeChanged)

    def getFile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Image files (*.jpg *.gif)")
        
        if fname != "":
            self.updateImg(fname)
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
            height, width, channel = self.image.shape
            bytesPerLine = 3 * width
            qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
            toSave = QPixmap(qImg)
            toSave.save(fname)
            self.errorSuccess.setStyleSheet("color: green; font: 12pt; MS Shell Dlg;")
            self.errorSuccess.setText("Successfully saved!")
            self.timer.timeout.connect(self.onTimeout)
            self.timer.start(5000)

    def updateImg(self, fname):
        self.image = cv2.imread(fname)

        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        
        self.imageBox.setPixmap(QPixmap(qImg))

    def updateImg2(self, imagename):
        height, width, channel = self.image.shape
        bytesPerLine = 3 * width
        qImg = QImage(self.image.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        
        self.imageBox.setPixmap(QPixmap(qImg))

    def redChanged(self, value):
        self.updateImg(self.imgFileName)
        img = change_red(self.image, value)
        self.updateImg2(self.image)

    def greenChanged(self, value):
        self.updateImg(self.imgFileName)
        img = change_green(self.image, value)
        self.updateImg2(self.image)

    def blueChanged(self, value):
        self.updateImg(self.imgFileName)
        img = change_blue(self.image, value)
        self.updateImg2(self.image)

    def sharpChanged(self):
        # self.updateImg(self.imgFileName)
        # img = sharpChanged(self.image, value)
        # self.updateImg2(self.image)

        cv2.imshow('Original Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        self.updateImg(self.imgFileName)
        img = sharpChanged(self.image)

        cv2.imshow('Sharpened Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        self.updateImg2(img)

    def blurChanged(self, value):
        cv2.imshow('Original Image', self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        self.updateImg(self.imgFileName)
        img = cv2.GaussianBlur(self.image,(5,5),100)

        cv2.imshow('Blurred Image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        self.updateImg2(img)

    def rgbChecked(self):
        if self.rgbRadio.isChecked():
            print("rgb")

    def grayscaleChecked(self):
        # if self.grayscaleRadio.isChecked():
        img = grayConversion(self.image)
        self.updateImg2(img)
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
