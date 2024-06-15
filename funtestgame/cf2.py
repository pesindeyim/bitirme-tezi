from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random


class Ui_MainWindow4(object):
    
    def setupUi(self, MainWindow4):
        MainWindow4.setObjectName("MainWindow4")
        MainWindow4.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Çerçevesiz pencere
        MainWindow4.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Şeffaf arka plan
        MainWindow4.resize(721, 576)
        self.centralwidget = QtWidgets.QWidget(MainWindow4)
        self.centralwidget.setObjectName("centralwidget")
        self.vdbtn1 = QtWidgets.QPushButton(self.centralwidget)
        self.vdbtn1.setGeometry(QtCore.QRect(300, 510, 131, 51))
        self.vdbtn1.setObjectName("vdbtn1")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.vdbtn1.setFont(font)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 631, 421))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow4.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow4)

        # GIF dosyasını yükle
        self.movie = QtGui.QMovie("example.gif")
        self.label.setMovie(self.movie)

        # Butona tıklandığında GIF'i oynat ve pencereyi kapat
        self.vdbtn1.clicked.connect(self.playGif)

    def retranslateUi(self, MainWindow4):
        _translate = QtCore.QCoreApplication.translate
        MainWindow4.setWindowTitle(_translate("MainWindow4", "MainWindow"))
        self.vdbtn1.setText(_translate("MainWindow4", "Çarkı Çevir!"))
        self.label.setText(_translate("MainWindow4", "TextLabel"))
    def cark_puan(self):
        randn = random.randint(1, 100)
        if randn<20:
            res=0
        elif randn<50:
            res=1000
        elif randn<70:
            res=3000
        elif randn<85:
            res=5000
        elif randn<92:
            res=7000
        elif randn<95:
            res=10000
        elif randn<99:
            res=50000
        elif randn<100:
            res=100000
        # QMessageBox.information(QMainWindow, "Sonuç", f"Rastgele Sayı: {randn}\n{res}")
        print(randn)
        print(res)
        return res

    def playGif(self):
        self.movie.start()
        # QTimer kullanarak 3 saniye bekleyip pencereyi kapat
        QtCore.QTimer.singleShot(3000, self.closeMainWindow)

    def closeMainWindow(self):
        # Pencereyi kapat
        self.centralwidget.window().close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow4()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
