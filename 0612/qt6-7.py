from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.resize(600,400)
widget.setWindowTitle('盎司毫升轉換器')

label1 = QtWidgets.QLabel(widget)
label1.setText('請輸入轉換的容量:')

label2 = QtWidgets.QLabel(widget)
label2.setText('請選擇換算單位:(oz/cc)')

input1 = QtWidgets.QLineEdit(widget)

input2 = QtWidgets.QComboBox(widget)
input2.addItems(['oz','cc'])

btn = QtWidgets.QPushButton('換算')

widget.show()
sys.exit(app.exec())