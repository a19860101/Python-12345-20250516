from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.resize(300,200)
widget.setWindowTitle('盎司毫升轉換器')

label1 = QtWidgets.QLabel(widget)
label1.setText('請輸入轉換的容量:')

label2 = QtWidgets.QLabel(widget)
label2.setText('請選擇換算單位:(oz/cc)')

resultLabel = QtWidgets.QLabel(widget)
resultLabel.setText('換算結果')

input1 = QtWidgets.QLineEdit(widget)

input2 = QtWidgets.QComboBox(widget)
input2.addItems(['oz','cc'])

btn = QtWidgets.QPushButton(widget)
btn.setText('換算')

# grid = QtWidgets.QGridLayout(widget)
#
# grid.addWidget(label1,1,1)
# grid.addWidget(label2,2,1)
# grid.addWidget(input1,1,2)
# grid.addWidget(input2,2,2)
# grid.addWidget(btn, 3,1, 1, 2)
# grid.addWidget(resultLabel, 4, 1)

form = QtWidgets.QFormLayout(widget)
form.addRow(label1,input1)
form.addRow(label2,input2)
form.addRow(btn)
form.addRow(resultLabel)


widget.show()
sys.exit(app.exec())