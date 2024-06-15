from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import random
from yeniduzen2 import Ui_MainWindow2

puan=0
class Ui_MainWindow7(object):
    def setupUi(self, MainWindow7):
        global puan
        self.MainWindow7 = MainWindow7
        MainWindow7.setObjectName("MainWindow7")
        MainWindow7.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow7)
        self.centralwidget.setObjectName("centralwidget")
        
        # Arka plan resmi için QLabel ekle
        self.background_label = QtWidgets.QLabel(self.centralwidget)
        self.background_label.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.background_label.setPixmap(QtGui.QPixmap("bck.png"))  # Arka plan resmi ekle
        self.background_label.setScaledContents(True)  # Resmi boyuta sığacak şekilde ayarla
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 801, 601))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.imglabel = QtWidgets.QLabel(self.frame)
        self.imglabel.setGeometry(QtCore.QRect(80, 30, 601, 401))
        self.imglabel.setText("")
        self.imglabel.setObjectName("imglabel")
        self.input = QtWidgets.QLineEdit(self.frame)
        self.input.setGeometry(QtCore.QRect(50, 450, 113, 22))
        self.input.setText("")
        self.input.setObjectName("input")
        font= QtGui.QFont()
        font.setPointSize(12)
        self.input.setFont(font)
        self.cizgilabel = QtWidgets.QLabel(self.frame)
        self.cizgilabel.setGeometry(QtCore.QRect(260, 430, 321, 41))
        self.cizgilabel.setObjectName("cizgilabel")
        font= QtGui.QFont()
        font.setPointSize(14)
        self.cizgilabel.setFont(font)
        self.cizgilabel.setStyleSheet("color: white")
        self.pnlabel = QtWidgets.QLabel(self.frame)
        self.pnlabel.setGeometry(QtCore.QRect(400, 500, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(12)
        self.pnlabel.setFont(font)
        self.pnlabel.setObjectName("pnlabel")
        self.pnlabel.setStyleSheet("color: white")
        self.menubut = QtWidgets.QPushButton(self.frame)
        self.menubut.setGeometry(QtCore.QRect(580, 450, 111, 41))
        self.menubut.setObjectName("menubut")
        MainWindow7.setCentralWidget(self.centralwidget)


        # Düğme ekle
        self.adambtn = QtWidgets.QPushButton(self.frame)
        self.adambtn.setGeometry(QtCore.QRect(200, 500, 151, 41))
        self.adambtn.setObjectName("pushButton")
        self.adambtn.setText("Harf Gir")

        MainWindow7.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow7)
        QtCore.QMetaObject.connectSlotsByName(MainWindow7)

        # Kelime listesi
        self.kelimeler = ["elma", "armut", "muz", "kiraz", "portakal", "muhteşem", "orman", "kelime", 
                          "su", "çorap", "şişe", "buzdolabı", "pencere", "harabe", "çarkıfelek", "arkadaş",
                          "anime", "balık", "ay", "kitap", "yatak", "ölümsüz", "bilgisayar", "araba", "film",
                          "hayat", "kader", "telefon", "akşam", "büyük", "alem", "demokratik", "hukuk"]
        # Rastgele bir kelime seç
        self.kelime = random.choice(self.kelimeler)
        self.gizli_kelime = ["_"] * len(self.kelime)
        global kelime_sayi
        kelime_sayi=len(self.kelime)
        self.cizgilabel.setText(" ".join(self.gizli_kelime))
        self.tahminler = set()
        self.hata_sayisi = 0
        

        # Resimleri yükle
        self.resimler = [QtGui.QPixmap(f"img{i}.png") for i in range(1, 8)]
        self.imglabel.setPixmap(self.resimler[0])

    def retranslateUi(self, MainWindow7):
        _translate = QtCore.QCoreApplication.translate
        MainWindow7.setWindowTitle(_translate("MainWindow7", "MainWindow"))
        self.pnlabel.setText(_translate("MainWindow7", f"PUAN: {puan}"))  # Başlangıçta puanı ekrana yazdır
        # self.adambtn.clicked.connect(self.onayla)  # Düğmeye tıklama sinyali
        self.menubut.setText(_translate("MainWindow7", "Ana Menü"))


    def onayla(self):
        global puan
        tahmin = self.input.text().lower()  # Giriş kutusundan tahmin alınıyor
        self.input.clear() 
         # Giriş kutusunu temizle
        if not tahmin:  # Check if the input field is empty
            print("Lütfen bir tahmin giriniz.")
            
        self.input.clear()

        if tahmin in self.tahminler:
            print("Bu harfi daha önce tahmin ettiniz.")
            

        if tahmin == self.kelime:
    # Gizli kelimeyi doğru tahmin edilen kelimeyle güncelle
            self.gizli_kelime = list(self.kelime)
            # Label'daki çizgilerin yerine doğru tahmin edilen kelimeyi göster
            self.cizgilabel.setText(" ".join(self.gizli_kelime))
            
            if self.hata_sayisi > 0 :  # Harf harf tahminler yapılmışsa
                puan = 2500
                QtWidgets.QMessageBox.information(self.centralwidget, "Kazandınız!", f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {self.kelime}")
                self.pnlabel.setText(f"PUAN: {puan}")  # Puanı ekrana güncelle
                return puan # Toplam puan yerine direkt 1500 puan ekle
            else:
                puan += 5000 
                QtWidgets.QMessageBox.information(self.centralwidget, "Kazandınız!", f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {self.kelime}")
                # Direkt kelime tahmin edilirse 2500 puan ekle
                self.pnlabel.setText(f"PUAN: {puan}")  # Puanı ekrana güncelle
                return puan
        else:
            if tahmin not in self.kelime:
                self.hata_sayisi += 1
                puan -= 500  # Hata yapıldığında 200 puan eksilt
                # Resmi güncelle
                self.imglabel.setPixmap(self.resimler[self.hata_sayisi])
            else:
                for i, harf in enumerate(self.kelime):
                    if harf == tahmin:
                        self.gizli_kelime[i] = harf
                puan += 750
            
            # Güncellemeleri her durumda yap
            self.cizgilabel.setText(" ".join(self.gizli_kelime))
            self.pnlabel.setText(f"PUAN: {puan}")  # Puanı ekrana güncelle
            if "_" not in self.gizli_kelime:  # Eğer gizli kelime tamamen açıldıysa
                QtWidgets.QMessageBox.information(self.centralwidget, "Kazandınız!", f"Tebrikler! Kelimeyi doğru tahmin ettiniz: {self.kelime}")
                return puan
            elif self.hata_sayisi == len(self.resimler) - 1:  # Eğer resimlerin sonuna gelindiğinde
                QtWidgets.QMessageBox.information(self.centralwidget, "Kaybettiniz", f"Maalesef, kelimeyi doğru tahmin edemediniz. Doğru kelime: {self.kelime}")
                return puan

    def adampuandon(self):
        return puan


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow7 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow7()
    ui.setupUi(MainWindow7)
    MainWindow7.show()
    sys.exit(app.exec_())
