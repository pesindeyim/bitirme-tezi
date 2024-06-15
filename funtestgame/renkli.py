# -*- coding: utf-8 -*-

import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox, QWidget
from PyQt5.QtCore import QTimer, Qt
from yeniduzen2 import Ui_MainWindow2

class Ui_MainWindow8(object):  
    def setupUi(self, MainWindow8):
        MainWindow8.setObjectName("MainWindow8")
        MainWindow8.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow8)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QHBoxLayout(self.centralwidget)

        self.sol_layout = QVBoxLayout()

        self.buton_layout = QGridLayout()
        spacer = QWidget(self.centralwidget)
        spacer.setFixedSize(200, 150)
        self.buton_layout.addWidget(spacer, 0, 0, 1, 2)

        self.kirmizi_buton = QPushButton('Kırmızı', self.centralwidget)
        self.kirmizi_buton.setStyleSheet('background-color: red')
        self.kirmizi_buton.setFixedSize(100, 50)
        self.buton_layout.addWidget(self.kirmizi_buton, 0, 0)

        self.yesil_buton = QPushButton('Yeşil', self.centralwidget)
        self.yesil_buton.setStyleSheet('background-color: green')
        self.yesil_buton.setFixedSize(100, 50)
        self.buton_layout.addWidget(self.yesil_buton, 0, 1)

        self.mavi_buton = QPushButton('Mavi', self.centralwidget)
        self.mavi_buton.setStyleSheet('background-color: blue')
        self.mavi_buton.setFixedSize(100, 50)
        self.buton_layout.addWidget(self.mavi_buton, 1, 0)

        self.sari_buton = QPushButton('Sarı', self.centralwidget)
        self.sari_buton.setStyleSheet('background-color: yellow')
        self.sari_buton.setFixedSize(100, 50)
        self.buton_layout.addWidget(self.sari_buton, 1, 1)

        self.sol_layout.addLayout(self.buton_layout)

        self.basla_butonu = QPushButton('Başla', self.centralwidget)
        self.basla_butonu.setFixedSize(100, 50)
        self.sol_layout.addWidget(self.basla_butonu, alignment=Qt.AlignCenter)

        self.label = QLabel(self.centralwidget)
        self.label.setFixedSize(550, 400)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('border: 2px solid black; border-radius: 10px; background-color: white')

        self.puan_label = QLabel('Puan: 0', self.centralwidget)
        self.puan_label.setFixedSize(200, 50)
        self.puan_label.setAlignment(Qt.AlignCenter)
        self.puan_label.setStyleSheet('font-size: 20px')

        self.layout.addLayout(self.sol_layout)
        self.layout.addWidget(self.label, alignment=Qt.AlignRight)
        self.layout.addWidget(self.puan_label, alignment=Qt.AlignTop | Qt.AlignRight)

        MainWindow8.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow8)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 26))
        self.menubar.setObjectName("menubar")
        MainWindow8.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow8)
        self.statusbar.setObjectName("statusbar")
        MainWindow8.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow8)
        QtCore.QMetaObject.connectSlotsByName(MainWindow8)

        self.puan = 0
        self.seviye = 1
        self.renkler = []
        self.kullanici_renkler = []
        self.buton_renkleri = ["Kırmızı", "Yeşil", "Mavi", "Sarı"]
        self.renk_haritalama = {
            "Kırmızı": "red",
            "Yeşil": "green",
            "Mavi": "blue",
            "Sarı": "yellow"
        }
        self.timer = QTimer(self.centralwidget)
        self.timer.timeout.connect(self.zaman_doldu)

        # self.basla_butonu.clicked.connect(self.oyunu_baslat)
        # self.kirmizi_buton.clicked.connect(lambda: self.renk_secildi('Kırmızı'))
        # self.yesil_buton.clicked.connect(lambda: self.renk_secildi('Yeşil'))
        # self.mavi_buton.clicked.connect(lambda: self.renk_secildi('Mavi'))
        # self.sari_buton.clicked.connect(lambda: self.renk_secildi('Sarı'))

    def retranslateUi(self, MainWindow8):
        _translate = QtCore.QCoreApplication.translate
        MainWindow8.setWindowTitle(_translate("MainWindow8", "Renk Hafıza Oyunu"))

    def oyunu_baslat(self):
        self.seviye = 1
        self.puan = 0
        self.renkler = []
        self.guncelle_puan()
        self.kullanici_renkler = []
        self.oyunu_siradaki_seviye()

    def oyunu_siradaki_seviye(self):
        self.renkler.append(random.choice(self.buton_renkleri))
        self.label.setStyleSheet(f'background-color: {self.renk_haritalama[self.renkler[-1]]}')
        self.label.setText('')
        self.renk_goster_index = 0
        self.goster_beyaz = False
        self.kullanici_renkler=[]
        self.goster_sirasi()

    def goster_sirasi(self):
        if self.goster_beyaz:
            self.label.setStyleSheet('background-color: white')
            self.goster_beyaz = False
            QTimer.singleShot(700, self.goster_sirasi)
        elif self.renk_goster_index < len(self.renkler):
            self.label.setStyleSheet(f'background-color: {self.renk_haritalama[self.renkler[self.renk_goster_index]]}')
            self.renk_goster_index += 1
            self.goster_beyaz = True
            QTimer.singleShot(1500, self.goster_sirasi)
        else:
            self.label.setText('Renkleri hatırlayıp sırasıyla butonlara basın:')
            self.label.setStyleSheet('background-color: white')
            self.kullanici_renkler = []

    def zaman_doldu(self):
        self.timer.stop()
        self.kontrol_et()

    def renk_secildi(self, renk):
        self.kullanici_renkler.append(renk)
        if len(self.kullanici_renkler) == len(self.renkler):
            self.kontrol_et()

    def kontrol_et(self):
        if len(self.kullanici_renkler) > 0:
            if self.kullanici_renkler == self.renkler:
                self.puan += 1000
                self.guncelle_puan()
                QMessageBox.information(self.centralwidget, 'Sonuç', 'Doğru tahmin! Bir sonraki seviyeye geçiyorsunuz.')
                self.oyunu_siradaki_seviye()
            else:
                self.puan -= 250
                self.guncelle_puan()
                QMessageBox.information(self.centralwidget, 'Sonuç', f'Yanlış tahmin! Doğru renk dizisi: {" ".join(self.renkler)}')
                return False
        else:
            pass

    def son_kontrol(self):
        sondeger = self.puan
        return sondeger

    def guncelle_puan(self):
        self.puan_label.setText(f'Puan: {self.puan}')

    def oyunu_resetle(self):
        self.seviye = 1
        self.puan = 0
        self.renkler = []
        self.kullanici_renkler = []
        self.guncelle_puan()
        self.label.setText('Oyun sıfırlandı. Yeni bir oyun başlatmak için Başla butonuna basın.')
        self.label.setStyleSheet('background-color: white')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow8 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow8()
    ui.setupUi(MainWindow8)
    MainWindow8.show()
    sys.exit(app.exec_())
