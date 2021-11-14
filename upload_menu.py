from edit_menu import *
from PyQt5.QtWidgets import QComboBox
from database import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")

        MainWindow.resize(600, 600)

        MainWindow.setMinimumSize(QtCore.QSize(600, 600))
        MainWindow.setMaximumSize(QtCore.QSize(600, 600))

        MainWindow.setStyleSheet("QWidget\n"
                                 "{\n"
                                 "background-color: qlineargradient(spread:repeat, "
                                 "x1:1, y1:1, "
                                 "x2:0.85, y2:0.85, "
                                 "stop:0.5 "
                                 "rgba(159, 62, 213, 255), "
                                 "stop:0.500372 rgba(72, 3, 111, 255));"
                                 "}"
                                 )

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(0, 25, 600, 400))

        font = QtGui.QFont()

        font.setFamily("Porsche Next")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.photo.setFont(font)

        self.photo.setToolTip("")
        self.photo.setStyleSheet("background-color: rgb(255, 255, 255);"
                                 "border-radius: 30px;"
                                 "border: 6px dashed #FFD300;"
                                 )

        self.photo.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.photo.setAlignment(QtCore.Qt.AlignCenter)

        self.photo.setIndent(4)

        self.photo.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.photo.setObjectName("photo")

        self.upload_btn = QtWidgets.QPushButton(self.centralwidget)

        self.upload_btn.setGeometry(QtCore.QRect(100, 450, 400, 60))

        self.upload_btn.setMinimumSize(QtCore.QSize(400, 60))
        self.upload_btn.setMaximumSize(QtCore.QSize(400, 60))

        font = QtGui.QFont()

        font.setFamily("Porsche Next")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        self.upload_btn.setFont(font)

        self.upload_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.upload_btn.setStyleSheet("QPushButton{"
                                      "background-color: rgb(185, 247, 62);"
                                      "border-radius: 30px;"
                                      "}"
                                      "QPushButton:pressed{\n"
                                      "background-color: #679B00;\n"
                                      "border-radius: 30px; \n"
                                      "}")

        self.upload_btn.setObjectName("upload_btn")

        self.next_btn = QtWidgets.QPushButton(self.centralwidget)

        self.next_btn.setGeometry(QtCore.QRect(100, 520, 400, 60))

        self.next_btn.setMinimumSize(QtCore.QSize(400, 60))
        self.next_btn.setMaximumSize(QtCore.QSize(400, 60))

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

        self.combo = QComboBox(self)
        self.combo.addItems(["Выбрать предзагруженное фото", "Эйнштейн", "Кот", "Мужчина с собакой"])
        self.combo.move(30, 50)
        self.combo.setMinimumSize(QtCore.QSize(200, 20))
        self.combo.setStyleSheet("background-color: rgb(185, 247, 62);")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("Colorizor", "Colorizor"))
        self.photo.setText(_translate("MainWindow", "Загрузи сюда фото"))
        self.upload_btn.setText(_translate("MainWindow", "Загрузить фото"))
        self.next_btn.setText(_translate("MainWindow", "Далее"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.upload_btn.clicked.connect(self.upload_photo)
        self.next_btn.clicked.connect(self.next_widget)

        self.edit_app = EditWidget()

        self.pixmap = None

        self.combo.activated[str].connect(self.onActivated)

    def upload_photo(self):
        file_name = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Картинка (*.jpg);;'
                'Картинка (*.jpeg);;'
                'Все файлы (*)')[0]

        if file_name != '':
            self.pixmap = QPixmap(file_name)
            self.photo.setPixmap(self.pixmap)
            with Image.open(file_name) as im:
                im.save('to_edit.jpg')

    def next_widget(self):
        if self.photo.text() != "Загрузи сюда фото":
            self.edit_app.show()
            self.edit_app.crop_photo.setPixmap(self.pixmap)

    def onActivated(self, text):
        if text != "Выбрать предзагруженное фото":
            fromDB2Img(["Выбрать предзагруженное фото", "Эйнштейн", "Мужчина с собакой", "Кот"].index(text))
            self.pixmap = QPixmap('to_edit.jpg')
            self.photo.setPixmap(self.pixmap)
