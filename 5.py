#подключаем модуль с направляющими линиями
from PyQt5.QtCore import Qt
#подключаем необходимые виджеты
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QRadioButton, QButtonGroup
 
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
 
# создаём объекты радиокнопок
radio_button_1 = QRadioButton('1')
# устанавливаем, какая радиокнопка будет выбрана при запуске программы
radio_button_1.setChecked(True)
 
radio_button_2 = QRadioButton('2')
radio_button_3 = QRadioButton('3')
 
# создаём группу радиокнопок и добавляем туда созданные нами ранее объекты радиокнопок
button_group = QButtonGroup()
button_group.addButton(radio_button_1, id = 1)
button_group.addButton(radio_button_2, id = 2)
button_group.addButton(radio_button_3, id = 3)
 
# размещаем радиокнопки на вертикальной направляющей
line.addWidget(radio_button_1)
line.addWidget(radio_button_2)
line.addWidget(radio_button_3)
 
# создаём объект кнопки и задаём надпись на ней
button = QPushButton('Проверить')
 
# помещаем кнопку на направляющую линию по центру
line.addWidget(button, alignment = Qt.AlignCenter)
 
# добавляем получившуюся линию на окно приложения
my_win.setLayout(line)
 
# создаём поле, где далее будет отображаться текст про выбранную кнопку
title = QLabel()
line.addWidget(title, alignment = Qt.AlignCenter)
my_win.setLayout(line)
 
#функция, которая изменяет информацию (текст) о новой кнопке
def radio_button_check():
    title.setText("Выбрана кнопка под номером " + str(button_group.checkedId()))
 
# связываем нажатие на кнопку и вызов функции
button.clicked.connect(radio_button_check)
 
#Оставляет приложение открытым, пока не будет нажата кнопка выхода
app.exec_()
