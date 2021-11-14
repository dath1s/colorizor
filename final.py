from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QAction, qApp
from PyQt5.QtGui import QPixmap, QIcon

import sys

import time

from colorizor import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(600, 600)
        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

        MainWindow.setStyleSheet("QWidget{"
                                 "background-color: qlineargradient(spread:repeat, x1:1, y1:1, "
                                 "x2:0.85, y2:0.85, "
                                 "stop:0.5 rgba(159, 62, 213, 255), "
                                 "stop:0.500372 rgba(72, 3, 111, 255));"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 600, 400))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        self.label.setFont(font)
        self.label.setToolTip("")

        self.label.setStyleSheet("background-color: rgb(255, 255, 255);"
                                 "border-radius: 30px;"
                                 "border: 6px dashed #FFD300;")

        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setText("")

        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(4)

        self.label.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)

        self.pushButton.setGeometry(QtCore.QRect(100, 460, 400, 60))

        self.pushButton.setMinimumSize(QtCore.QSize(400, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(400, 60))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton.setStyleSheet("QPushButton{"
                                      "background-color: rgb(185, 247, 62);"
                                      "border-radius: 30px;"
                                      "}"
                                      "QPushButton:pressed{\n"
                                      "background-color: #679B00;\n"
                                      "border-radius: 30px; \n"
                                      "}")

        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Скачать фото"))


class ColorWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.download)

        colorizator.colorize_image('croped.jpg', 'color.jpg')

        time.sleep(5)

        self.pixmap = QPixmap('color.jpg')
        self.label.setPixmap(self.pixmap)

    def download(self):
        name = QFileDialog.getSaveFileName(self, 'Save File')
        if name != ('', ''):
            img = Image.open('color.jpg')
            img.save(name[0])
