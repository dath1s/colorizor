from final import *

from PyQt5.QtWidgets import QMessageBox

import os

import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(800, 500)

        MainWindow.setMinimumSize(QtCore.QSize(800, 650))
        MainWindow.setMaximumSize(QtCore.QSize(800, 650))

        MainWindow.setStyleSheet("QWidget"
                                 "{\n"
                                 "background-color: qlineargradient(spread:repeat, "
                                 "x1:1, y1:1, "
                                 "x2:0.85, y2:0.85, "
                                 "stop:0.5 rgba(159, 62, 213, 255), "
                                 "stop:0.500372 rgba(72, 3, 111, 255));"
                                 "}")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.crop_photo = QtWidgets.QLabel(self.centralwidget)
        self.crop_photo.setGeometry(QtCore.QRect(0, 10, 600, 400))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)

        self.crop_photo.setFont(font)

        self.crop_photo.setToolTip("")

        self.crop_photo.setStyleSheet("background-color: rgb(255, 255, 255);"
                                      "border-radius: 30px;"
                                      "border: 6px dashed #FFD300;")
        self.crop_photo.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.crop_photo.setText("")

        self.crop_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.crop_photo.setIndent(4)

        self.crop_photo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.crop_photo.setObjectName("crop_photo")

        self.next_btn = QtWidgets.QPushButton(self.centralwidget)

        self.next_btn.setGeometry(QtCore.QRect(30, 570, 750, 60))

        self.next_btn.setMinimumSize(QtCore.QSize(750, 60))
        self.next_btn.setMaximumSize(QtCore.QSize(750, 60))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.next_btn.setFont(font)

        self.next_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.next_btn.setStyleSheet("QPushButton{"
                                    "background-color: rgb(185, 247, 62);"
                                    "border-radius: 30px;"
                                    "}"
                                    "QPushButton:pressed{\n"
                                    "background-color: #679B00;\n"
                                    "border-radius: 30px; \n"
                                    "}")

        self.next_btn.setObjectName("next_btn")

        self.next_btn.setEnabled(False)

        self.crop_btn = QtWidgets.QPushButton(self.centralwidget)

        self.crop_btn.setGeometry(QtCore.QRect(30, 430, 750, 60))

        self.crop_btn.setMinimumSize(QtCore.QSize(750, 60))
        self.crop_btn.setMaximumSize(QtCore.QSize(750, 60))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.crop_btn.setFont(font)

        self.crop_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.crop_btn.setStyleSheet("QPushButton{"
                                    "background-color: rgb(185, 247, 62);"
                                    "border-radius: 30px;"
                                    "}"
                                    "QPushButton:pressed{\n"
                                    "background-color: #679B00;\n"
                                    "border-radius: 30px; \n"
                                    "}")

        self.crop_btn.setObjectName("crop_btn")

        self.skip_btn = QtWidgets.QPushButton(self.centralwidget)

        self.skip_btn.setGeometry(QtCore.QRect(30, 500, 750, 60))

        self.skip_btn.setMinimumSize(QtCore.QSize(750, 60))
        self.skip_btn.setMaximumSize(QtCore.QSize(750, 60))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.skip_btn.setFont(font)

        self.skip_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.skip_btn.setStyleSheet("QPushButton{"
                                    "background-color: rgb(185, 247, 62);"
                                    "border-radius: 30px;"
                                    "}"
                                    "QPushButton:pressed{\n"
                                    "background-color: #679B00;\n"
                                    "border-radius: 30px; \n"
                                    "}")

        self.skip_btn.setObjectName("crop_btn")

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)

        self.gridLayoutWidget.setGeometry(QtCore.QRect(620, 40, 161, 341))

        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 40))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(100, 16777215))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)

        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 40))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 40))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 40))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.x1 = QtWidgets.QLabel(self.gridLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.x1.setFont(font)
        self.x1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x1.setObjectName("x1")

        self.gridLayout.addWidget(self.x1, 0, 0, 1, 1)

        self.y1 = QtWidgets.QLabel(self.gridLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.y1.setFont(font)
        self.y1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y1.setObjectName("y1")

        self.gridLayout.addWidget(self.y1, 1, 0, 1, 1)

        self.x2 = QtWidgets.QLabel(self.gridLayoutWidget)

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.x2.setFont(font)
        self.x2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.x2.setObjectName("x2")

        self.gridLayout.addWidget(self.x2, 2, 0, 1, 1)

        self.y2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.y2.setMinimumSize(QtCore.QSize(50, 0))

        font = QtGui.QFont()
        font.setFamily("Porsche Next")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.y2.setFont(font)
        self.y2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.y2.setObjectName("y2")

        self.gridLayout.addWidget(self.y2, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Редактор фото"))
        self.next_btn.setText(_translate("MainWindow", "Далее"))
        self.crop_btn.setText(_translate("MainWindow", "Обрезать фото"))
        self.skip_btn.setText(_translate("MainWindow", "Пропустить шаг"))

        self.x1.setText(_translate("MainWindow", "     X1"))
        self.y1.setText(_translate("MainWindow", "     Y1"))
        self.x2.setText(_translate("MainWindow", "     X2"))
        self.y2.setText(_translate("MainWindow", "     Y2"))


class EditWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.next_btn.clicked.connect(self.nex_widget)
        self.crop_btn.clicked.connect(self.crop_photo_edit)
        self.skip_btn.clicked.connect(self.skip)

        self.photo_path_edit = None
        self.pixmap_edit = None

        self.photo_to_edit = Photo_saver(self.photo_path_edit, self.pixmap_edit)

        self.color_widget = ColorWidget()

    def crop_photo_edit(self):
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
            self.photo_to_edit.add_data(self.pixmap_edit, 'to_edit.jpg')
            # img_size = Image.open('to_edit.jpg').size()
            if int(self.lineEdit.text()) < 0 and int(self.lineEdit_2.text()) < 0 and int(self.lineEdit_3.text()) < 0 \
                    and int(self.lineEdit_4.text()) < 0 or int(self.lineEdit.text()) > int(self.lineEdit_3.text()) or \
                    int(self.lineEdit_2.text()) > int(self.lineEdit_4.text()):
                msg = QMessageBox()
                msg.setText("Проверьте корректность ввода:\n"
                            "   Все координаты должны быть целыми и положительными\n"
                            "   Начальные координаты должны быть меньше конечных")
                msg.setWindowTitle("Неверный ввод")
                msg.setIcon(QMessageBox.Critical)
                msg.setStyleSheet("background-color: rgb(0, 0, 0);")
                msg.setStyleSheet("text-color: rgb(255, 255, 255);")
                msg.exec_()
                self.crop_photo.setPixmap(QPixmap('to_edit.jpg'))

                self.next_btn.setEnabled(False)
            else:
                self.photo_to_edit.crop_image(int(self.lineEdit.text()),
                                              int(self.lineEdit_2.text()),
                                              int(self.lineEdit_3.text()),
                                              int(self.lineEdit_4.text()))
                time.sleep(2)

                self.next_btn.setEnabled(True)
            # Image.open('croped.jpg')
            self.pixmap = QPixmap('croped.jpg')
            self.crop_photo.setPixmap(self.pixmap)
        else:
            img = Image.open('to_edit.jpg')
            img.save('croped.jpg')

            self.next_btn.setEnabled(True)

    def nex_widget(self):
        colorizator.colorize_image('croped.jpg', 'color.jpg')
        self.new_pixmap = QPixmap('color.jpg')
        self.color_widget.label.setPixmap(self.new_pixmap)
        time.sleep(2)
        self.color_widget.show()

    def skip(self):
        img = Image.open('to_edit.jpg')
        img.save('croped.jpg')
        colorizator.colorize_image('croped.jpg', 'color.jpg')
        self.new_pixmap = QPixmap('color.jpg')
        self.color_widget.label.setPixmap(self.new_pixmap)
        time.sleep(2)
        self.color_widget.show()
