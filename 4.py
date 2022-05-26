from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
 
app = QApplication([])
window = QWidget()
window.setWindowTitle('Языки программирования')
window.resize(400, 300)
 
#1 шаг. Создать 6 надписей с названиями языков программирования
sentence1 = QLabel('PHP')
sentence2 = QLabel('JavaScript')
sentence3 = QLabel('Python')
sentence4 = QLabel('Pascal')
sentence5 = QLabel('SQL')
sentence6 = QLabel('C++')
 
#2 шаг. Создать 4 направляющие: 3 горизонтальные и 1 вертикальную
layoutV = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
 
#3 шаг. Привязать 6 объектов к горизонтальным направляющим
layoutH1.addWidget(sentence1, alignment = Qt.AlignCenter)
layoutH1.addWidget(sentence2, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence3, alignment = Qt.AlignCenter)
layoutH2.addWidget(sentence4, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence5, alignment = Qt.AlignCenter)
layoutH3.addWidget(sentence6, alignment = Qt.AlignCenter)
 
#4 шаг. Привязать горизонтальные направляющие к вертикальной направляющей
layoutV.addLayout(layoutH1)
layoutV.addLayout(layoutH2)
layoutV.addLayout(layoutH3)
window.setLayout(layoutV)
 
window.show()
app.exec_()
