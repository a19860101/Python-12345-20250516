from PyQt6 import QtWidgets,QtGui
import sys


app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

w.setWindowTitle('哈囉Python')
w.resize(600,400)

label = QtWidgets.QLabel(w)
label.move(50,50)
label.setText('文字標籤')

inp = QtWidgets.QLineEdit(w)
inp.move(250, 250)

# 加入下拉選單
select = QtWidgets.QComboBox(w)
# 加入選項
select.addItems(['A','B','C','D'])
select.move(300,100)



w.show()
sys.exit(app.exec())