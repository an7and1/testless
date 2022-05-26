#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
 
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
# создаём направляющую вертикальную линию
line = QVBoxLayout()
# создаём объект кнопки и задаём надпись на ней
button = QPushButton('Кнопка с секретом')
# помещаем текст на направляющую линию по центру
line.addWidget(button, alignment = Qt.AlignCenter)
# добавляем получившуюся линию на окно приложения
my_win.setLayout(line)
 
#функция, которая создаёт и показывает вторую фразу
def show_fun_title():
    fun_title = QLabel('Ты просто чудо!')
    line.addWidget(fun_title, alignment = Qt.AlignCenter)
    my_win.setLayout(line)
 
# связываем нажатие на кнопку и вызов функции
button.clicked.connect(show_fun_title)
#Оставляет приложение открытым, пока не будет нажата кнопка выхода
app.exec_()
