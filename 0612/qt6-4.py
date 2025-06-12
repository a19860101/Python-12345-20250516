from PyQt6 import QtWidgets,QtGui
import sys


app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

w.setWindowTitle('哈囉Python')
w.resize(600,400)

label = QtWidgets.QLabel(w)
label.move(50,50)
label.setText('文字標籤')

# 建立單行文字輸入框
inp = QtWidgets.QLineEdit(w)
# 設定輸入框位置
# inp.move(250, 250)
# setGeometry(x, y, w, h)
inp.setGeometry(250,250,100,30)

w.show()
sys.exit(app.exec())