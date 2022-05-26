#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout
 
#создаём объект приложения
app = QApplication([])
# создаём объект главного окна
my_win = QWidget()
# создаём название главного окна
my_win.setWindowTitle('Моё первое приложение')
# задаём точку появления окна на экране компьютера
my_win.move(900, 70)
# задаём размер окна
my_win.resize(400, 200)
# даём команду окну показаться
my_win.show()
 
# создаём направляющую горизонтальную линию
line = QHBoxLayout()
# создаём объект текста
title = QLabel('Hello, world!')
# помещаем текст на направляющую линию по центру
line.addWidget(title, alignment=Qt.AlignCenter)
# добавляем получившуюся линию на окно приложения
my_win.setLayout(line)
#Оставляет приложение открытым, пока не будет нажата кнопка выхода
app.exec_()
