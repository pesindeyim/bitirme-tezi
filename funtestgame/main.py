from PyQt5.QtWidgets import QDialog, QApplication, QSplashScreen, QMainWindow, QStackedWidget, QWidget, QMessageBox, QFileDialog,QCheckBox
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt, QTimer, QUrl
from yeniduzen import Ui_MainWindow
from yeniduzen2 import Ui_MainWindow2
from carkifelek import Ui_MainWindow3
from PyQt5.QtGui import QPixmap, QPalette, QBrush
from PyQt5 import QtCore, QtGui, QtWidgets
from cf2 import Ui_MainWindow4
from adamasmaca import Ui_MainWindow7
from renkli import Ui_MainWindow8
from snake1 import Ui_MainWindow9
import random
import sys
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

AnaPuan=0

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        loadUi("sayfabir.ui", self)

        self.setStyleSheet("background-image: url('orange.png');")
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)

        self.progressBar.setValue(0)
        self.progressBar.setMaximum(100)

        self.timer.start(30)
        self.progress_value = 0

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile("music.mp3")))
        self.mediaPlayer.setVolume(8)
        self.mediaPlayer.mediaStatusChanged.connect(self.loopMusic)
        self.mediaPlayer.play()

    def loopMusic(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.mediaPlayer.setPosition(0)
            self.mediaPlayer.play()    
    
    def update_progress(self):
        global AnaPuan
        snake_window = Ui_MainWindow9()
        snake_window.setFixedSize(snake_window.size())
        
        pencere8 = QMainWindow()
        ui8 = Ui_MainWindow8()
        ui8.setupUi(pencere8)
        pencere8.setFixedSize(pencere8.size())

        pencere7 = QMainWindow()
        ui7 = Ui_MainWindow7()
        ui7.setupUi(pencere7)
        pencere7.setFixedSize(pencere7.size())

        def ana_menu():
            pencere2.close()
            self.window2.show()
        
        def toggle_music(state):
            if state == Qt.Checked:
                self.mediaPlayer.pause()  # Müziği durdur
            else:
                self.mediaPlayer.play()  # Müziği çalmaya devam et

        self.progress_value += 1
        self.progressBar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.hide()
            self.window2 = QMainWindow()
            loadUi("yeniduzen.ui", self.window2)
            self.window2.setWindowFlags(Qt.Window)
            self.window2.setFixedSize(self.window2.size()) # boyut büyütmeyi kapatır.
            self.window2.show()
            
            def btn1_click():
                ui2.stackedWidget.setCurrentIndex(0)
                self.window2.close()

            def btn2_click():
                ui2.labelmpuan.setText(f"Puan:{AnaPuan}")
                ui2.stackedWidget.setCurrentIndex(1)
                self.window2.close()
                ui2.mb2.hide()
                ui2.mb3.hide()

            def btn3_click():
                ui2.stackedWidget.setCurrentIndex(2)
                self.window2.close()

            def pencere2kapa():
                pencere2.close()
                
            def cf_click():
                QtCore.QTimer.singleShot(3000, pencere3.show)

            def oynmnu():
                ui3.labelsonuc.clear()
                pencere2.show()
                pencere3.close()
        
            def hafiza_basla():
                pencere8.show()  

            def hafiza_kontrol():
                global AnaPuan
                if len(ui8.kullanici_renkler) > 0 and len(ui8.kullanici_renkler) == len(ui8.renkler) and ui8.kullanici_renkler != ui8.renkler  :
                        print("Selam")
                        pencere2.show()
                        pencere8.close()
                        renkp_dondur()
                        ui2.labelpuan.setText(f"Puan:{AnaPuan}")
                else:
                   QtCore.QTimer.singleShot(2000, hafiza_kontrol) 

    

            def btnkontrol_click():
                global AnaPuan
                kntrl = ui3.kontrol_et()
                if kntrl == True:
                    result = Ui_MainWindow4.cark_puan(self)
                    print("Sonuc:", result)
                    if result == 0:
                        AnaPuan = AnaPuan * 0
                        ui3.labelpuanç.setText(f"Puanın: {result}")
                        ui2.labelpuan.setText(f"Puan:{AnaPuan}")  # QLabel metnini güncelle
                    # Update QLabel text
                        print(AnaPuan)
                        print("İFLAAAAAAAAAAAAAAAAAAAAAS")
                    else:
                        AnaPuan = AnaPuan + result
                        ui3.labelpuanç.setText(f"Puanın: {result}")  # QLabel metnini güncelle
                        ui2.labelpuan.setText(f"Puan:{AnaPuan}")
                        print(AnaPuan)
                else:
                    print("yanlış cevap")

                QTimer.singleShot(5000, oynmnu)

            def yazdir():
                global AnaPuan
                resulta=ui7.adampuandon()
                AnaPuan=AnaPuan+resulta
                print(resulta) 
                ui2.labelpuan.setText(f"Puan:{AnaPuan}") 
                print(AnaPuan)


            def yilan():
                snake_window.reset_game()
                snake_window.show()
                yilan_kapa()
                
            def yilan_kapa():
                global AnaPuan
                if snake_window.check_collisions() == False:
                    pencere2.show()
                    mesaj_kutusu = QtWidgets.QMessageBox(self)
                    mesaj_kutusu.setWindowTitle('Oyun Bitti')
                    mesaj_kutusu.setText(f'OYUNU KAYBETTİN !\nPuanınız: {snake_window.score}')
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    mesaj_kutusu.setFont(font)
                    mesaj_kutusu.setStyleSheet("color: white;") 
                    mesaj_kutusu.exec_()
                    print("Gelio")
                    yilanpuan_dondur()
                    snake_window.close()
                    ui2.labelpuan.setText(f"Puan:{AnaPuan}")
    
                else:
                    QTimer.singleShot(1000, yilan_kapa)  # Bir saniye sonra fonksiyonu tekrar çağır


            def yilanpuan_dondur():
                global AnaPuan
                yilan_p=snake_window.yilan_puan()
                AnaPuan=AnaPuan+yilan_p
                print(yilan_p)
                
            def renkp_dondur():
                global AnaPuan
                renkpuan=ui8.son_kontrol()
                AnaPuan=AnaPuan+renkpuan

            def kapa():
                pencere7.close()  # MainWindow7 penceresini kapat
                puan=0                
                ui7.pnlabel.setText(f"{puan}")# Oyunu sıfırla
                ui7.kelime = random.choice(ui7.kelimeler)
                ui7.gizli_kelime = ["_"] * len(ui7.kelime)
                ui7.cizgilabel.setText(" ".join(ui7.gizli_kelime))
                ui7.tahminler = set()
                ui7.hata_sayisi = 0
                ui7.imglabel.setPixmap(ui7.resimler[0]) # Resmi başlangıç resmine geri döndür
                pencere2.show()  # Ui_MainWindow2 penceresini göster


            def marketbtn1():
                global AnaPuan
                if AnaPuan>=25000:
                    AnaPuan=AnaPuan-25000
                    ui2.labelpuan.setText(f"Puan:{AnaPuan}")
                    ui2.labelmpuan.setText(f"Puan:{AnaPuan}")
                    ui2.mb1.hide()
                    ui2.mb2.show()
            def marketbtn2():
                global AnaPuan
                if AnaPuan>=50000:
                    AnaPuan=AnaPuan-50000
                    ui2.labelpuan.setText(f"Puan:{AnaPuan}")
                    ui2.labelmpuan.setText(f"Puan:{AnaPuan}")
                    ui2.mb2.hide()
                    ui2.mb3.show()
                    
            def marketbtn3():
                global AnaPuan
                if AnaPuan>=100000:
                    AnaPuan=AnaPuan-100000
                    ui2.labelpuan.setText(f"Puan:{AnaPuan}")
                    ui2.labelmpuan.setText(f"Puan:{AnaPuan}") 
                    ui2.mb3.hide()
                    mesaj_kutusu2 = QtWidgets.QMessageBox(self)
                    mesaj_kutusu2.setWindowTitle('Oyun Bitti')
                    mesaj_kutusu2.setText(f'Oyun Bitti.  KAZANDIN VE TEŞEKKÜR EDERİM...')
                    font = QtGui.QFont()
                    font.setPointSize(15)
                    mesaj_kutusu2.setFont(font)
                    mesaj_kutusu2.setStyleSheet("color: white;") 
                    mesaj_kutusu2.exec_()
                    

            ui = Ui_MainWindow()
            ui.setupUi(self.window2)
            self.window2.show()
            
            pencere2 = QMainWindow()
            ui2 = Ui_MainWindow2()
            ui2.setupUi(pencere2)
            pencere2.setFixedSize(pencere2.size())
            
            pencere4 = QMainWindow()
            ui4 = Ui_MainWindow4()
            ui4.setupUi(pencere4)
            pencere4.setFixedSize(pencere4.size())

            pencere3 = QMainWindow()
            ui3 = Ui_MainWindow3()
            ui3.setupUi(pencere3)
            pencere3.setFixedSize(pencere3.size())

                    
            ui.btn1.clicked.connect(lambda: pencere2.show())
            ui.btn1.clicked.connect(btn1_click)

            ui.btn2.clicked.connect(lambda: pencere2.show())
            ui.btn2.clicked.connect(btn2_click)

            ui2.markmenu.clicked.connect(ana_menu)
            ui2.ayarmenu.clicked.connect(ana_menu)
            ui2.playmenu.clicked.connect(ana_menu)
            ui2.sescheck.stateChanged.connect(toggle_music)

            ui.btn3.clicked.connect(lambda: pencere2.show())
            ui.btn3.clicked.connect(btn3_click)

            ui2.obt1.clicked.connect(lambda: pencere4.show())
            ui2.obt1.clicked.connect(pencere2kapa)

            ui2.obt2.clicked.connect(lambda: pencere7.show())
            ui2.obt2.clicked.connect(pencere2kapa)

            ui3.btnkontrol.clicked.connect(btnkontrol_click)

            ui4.vdbtn1.clicked.connect(lambda: ui4.playGif())
            ui4.vdbtn1.clicked.connect(cf_click)

            ui7.adambtn.clicked.connect(lambda: ui7.onayla())
            ui7.adambtn.clicked.connect(yazdir)
            ui7.menubut.clicked.connect(kapa)

            ui2.obt3.clicked.connect(lambda: hafiza_basla())
            ui2.obt3.clicked.connect(pencere2kapa)
    
            ui8.basla_butonu.clicked.connect(lambda: ui8.oyunu_baslat())
            ui8.basla_butonu.clicked.connect(hafiza_kontrol)
            ui8.kirmizi_buton.clicked.connect(lambda: ui8.renk_secildi('Kırmızı'))
            ui8.mavi_buton.clicked.connect(lambda: ui8.renk_secildi('Mavi'))
            ui8.yesil_buton.clicked.connect(lambda: ui8.renk_secildi('Yeşil'))
            ui8.sari_buton.clicked.connect(lambda: ui8.renk_secildi('Sarı'))
            #------------------------------------------------------------------#
            ui2.mb1.clicked.connect(marketbtn1)
            ui2.mb2.clicked.connect(marketbtn2)
            ui2.mb3.clicked.connect(marketbtn3)

            ui2.obt4.clicked.connect(lambda: yilan())
            ui2.obt4.clicked.connect(pencere2kapa)
            
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
