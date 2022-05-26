from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QWidget, QApplication,  QPushButton, QHBoxLayout, QVBoxLayout
 
# главное окно:
app = QApplication([])
window = QWidget()
window.setWindowTitle('Испытай удачу, друг!')
window.resize(300, 300)
 
#1 шаг. Создать пять кнопок с цифрами
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
 
#2 шаг. Создать 4 направляющие: 3 горизонтальных и 1 вертикальную
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
 
#3 шаг. Привязать объекты к горизонтальным направляющим. Не забудь использовать параметр alignment
layoutH1.addWidget(button1, alignment = Qt.AlignLeft)
layoutH1.addWidget(button2, alignment = Qt.AlignRight)
layoutH2.addWidget(button3, alignment = Qt.AlignCenter)
layoutH3.addWidget(button4, alignment = Qt.AlignLeft)
layoutH3.addWidget(button5, alignment = Qt.AlignRight)
 
#4 шаг. Привязать горизонтальные направляющие к вертикальной направляющей
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)
window.setLayout(layoutV)
 
window.show()
app.exec_()
