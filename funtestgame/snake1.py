import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class Ui_MainWindow9(QtWidgets.QWidget):
    game_over_signal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setupUi()
        

    def setupUi(self):
        self.setGeometry(0, 0, 620, 640)  # Pencere boyutunu ayarla
        self.setWindowTitle('Yılan Oyunu')

        # Yılanın hareket ettiği alanın arka plan rengini ayarla
        self.setStyleSheet("background-color: lightgreen;")  

        self.snake = [(20, 20), (20, 40), (20, 60)]  # Yılanın başlangıç konumu
        self.food = self.generate_food()  # Yiyecek konumu
        self.direction = QtCore.Qt.Key_Right  # Başlangıçta sağa doğru hareket
        self.timer = QtCore.QBasicTimer()
        self.timer.start(100, self)
        self.score = 0  # Puanı başlat
        
        self.statusBar = QtWidgets.QStatusBar(self)  # statusBar özelliğini oluştur
        self.statusBar.setGeometry(0, 620, 620, 20)  # StatusBar konumunu ve boyutunu ayarla
        self.statusBar.showMessage("Puan: {}".format(self.score))  # Başlangıçta puanı göster

    def generate_food(self):
        while True:
            food = (random.randint(0, 29) * 20, random.randint(0, 29) * 20)  # Rastgele yiyecek konumu
            if food not in self.snake:
                return food

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.fillRect(self.rect(), QtGui.QColor(0, 255, 51))  # Oyun alanını siyah renge boyama
        painter.setBrush(QtGui.QColor(0, 100, 0))  # Yılan rengi (koyu yeşil)
        for part in self.snake:
            painter.drawRect(part[0], part[1], 20, 20)  # Yılanı çizme
        painter.setBrush(QtGui.QColor(255, 0, 0))
        painter.drawRect(self.food[0], self.food[1], 20, 20)  # Yiyeceği çizme

    def timerEvent(self, event):
        self.move_snake()
        self.check_collisions()
        self.repaint()

    def move_snake(self):
        head = self.snake[0]
        x, y = head
        if self.direction == QtCore.Qt.Key_Right:
            x += 20
        elif self.direction == QtCore.Qt.Key_Left:
            x -= 20
        elif self.direction == QtCore.Qt.Key_Down:
            y += 20
        elif self.direction == QtCore.Qt.Key_Up:
            y -= 20
        self.snake = [(x, y)] + self.snake[:-1]
    def yilan_puan(self):
        yilan_puan=self.score
        return yilan_puan
    def check_collisions(self):
        head = self.snake[0]
        if head in self.snake[1:] or not(0 <= head[0] < 600) or not(0 <= head[1] < 600):  # Yılanın kendine veya sınıra çarpma kontrolü
            self.timer.stop()
            return False

        elif head == self.food:  # Yiyeceği yeme kontrolü
            self.snake.append(self.snake[-1])
            self.food = self.generate_food()
            self.score += 750
            self.statusBar.showMessage("Puan: {}".format(self.score))

    def reset_game(self):
        self.snake = [(20, 20), (20, 40), (20, 60)]
        self.food = self.generate_food()
        self.direction = QtCore.Qt.Key_Right
        self.score = 0
        self.statusBar.showMessage("Puan: {}".format(self.score))
        self.timer.start(100, self)
        self.close()

    def keyPressEvent(self, event):
        if event.key() in [QtCore.Qt.Key_Right, QtCore.Qt.Key_Left, QtCore.Qt.Key_Down, QtCore.Qt.Key_Up]:
            if event.key() == QtCore.Qt.Key_Right and self.direction != QtCore.Qt.Key_Left:
                self.direction = event.key()
            elif event.key() == QtCore.Qt.Key_Left and self.direction != QtCore.Qt.Key_Right:
                self.direction = event.key()
            elif event.key() == QtCore.Qt.Key_Down and self.direction != QtCore.Qt.Key_Up:
                self.direction = event.key()
            elif event.key() == QtCore.Qt.Key_Up and self.direction != QtCore.Qt.Key_Down:
                self.direction = event.key()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    snake = Ui_MainWindow9()
    snake.show()
    sys.exit(app.exec_())
