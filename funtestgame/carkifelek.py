# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
from yeniduzen2 import Ui_MainWindow2
from cf2 import Ui_MainWindow4
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer



class Ui_MainWindow3(QMainWindow):
    def setupUi(self, MainWindow3):
        self.MainWindow3 = MainWindow3
        
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(1450, 850)
        MainWindow3.setStyleSheet("")

        # Arka plan resmini yükle
        pixmap = QtGui.QPixmap("cfbg.png")  # Arka plan resminin dosya yolu
        background = QtWidgets.QLabel(MainWindow3)
        background.setPixmap(pixmap)
        background.setGeometry(0, 0, 1450, 850)  # Pencere boyutuyla aynı olmalı
        background.lower()

        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.labelsoru = QtWidgets.QLabel(self.centralwidget)
        self.labelsoru.setGeometry(QtCore.QRect(40, 230, 611, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labelsoru.setFont(font)
        self.labelsoru.setObjectName("labelsoru")
        
        # Diğer widget'lar buraya gelecek...

        font = QtGui.QFont()
        font.setFamily("Time News Roman")
        font.setPointSize(13)
        self.labelsoru.setFont(font)
        self.labelsoru.setObjectName("labelsoru")
        self.labelsoru.setStyleSheet("color: white;")
        self.linecvp = QtWidgets.QLineEdit(self.centralwidget)
        self.linecvp.setGeometry(QtCore.QRect(180, 400, 341, 71))
        self.linecvp.setStyleSheet("color: black;")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.linecvp.setFont(font)
        self.linecvp.setObjectName("linecvp")
        self.labelisim = QtWidgets.QLabel(self.centralwidget)
        self.labelisim.setGeometry(QtCore.QRect(430, 80, 451, 51))
        self.labelisim.setObjectName("labelisim")
        self.labelisim.setStyleSheet("color: white;")
        self.labelisim.setStyleSheet("background-image: url(:/img/carkifelek.png);")
        self.labelisim.setText("")
        self.btnkontrol = QtWidgets.QPushButton(self.centralwidget)
        self.btnkontrol.setGeometry(QtCore.QRect(260, 620, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btnkontrol.setFont(font)
        self.btnkontrol.setObjectName("btnkontrol")
        self.labelpuanç = QtWidgets.QLabel(self.centralwidget)
        self.labelpuanç.setGeometry(QtCore.QRect(980, 250, 291, 201))
        self.labelpuanç.setStyleSheet("color: white;")
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelpuanç.setFont(font)
        self.labelpuanç.setObjectName("labelpuanç")
        self.labelsonuc = QtWidgets.QLabel(self.centralwidget)
        self.labelsonuc.setGeometry(QtCore.QRect(180, 500, 341, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.labelsonuc.setFont(font)
        self.labelsonuc.setObjectName("labelsonuc")
        self.labelsonuc.setStyleSheet("color: white;")
        MainWindow3.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)
        # Veritabanı bağlantısı oluştur
        self.conn = sqlite3.connect("carkifeleksoru.db")
        self.cur = self.conn.cursor()

        # İlk soruyu yükle
        
        self.yeni_soru()
        

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "MainWindow"))
        self.btnkontrol.setText(_translate("MainWindow3", "Kontrol Et"))
        self.labelpuanç.setText(_translate("MainWindow3", ""))

    def yeni_soru(self):
        # Veritabanından rastgele bir soru çek
        
        self.cur.execute("SELECT soru, cevap FROM carkifeleksoru ORDER BY RANDOM() LIMIT 1")
        soru, self.cevap = self.cur.fetchone()
        self.labelsoru.setText(soru)
        
    def yeni_soru_delayed(self):
        QTimer.singleShot(5000, self.yeni_soru)

    
    
    def kontrol_et(self):
    # Kullanıcının girdiği cevabı kontrol et
        kullanici_cevabi = self.linecvp.text()
        
        # Doğru cevapla karşılaştırma yapın
        if kullanici_cevabi.lower() == self.cevap.lower():
            self.labelsonuc.setText("Doğru!")
            kontrol = True
        else:
            self.labelsonuc.setText("Yanlış! Doğru cevap: " + self.cevap)
            kontrol = False

        self.linecvp.clear()
        self.yeni_soru_delayed()  # Yeni soruyu 5 saniye sonra getir
        return kontrol


        
    # Yeni bir soru yükle
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec_())
