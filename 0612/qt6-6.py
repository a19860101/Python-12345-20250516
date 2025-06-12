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

select = QtWidgets.QComboBox(w)
select.addItems(['A','B','C','D'])
select.move(300,100)

# 在視窗中建立按鈕
btn = QtWidgets.QPushButton(w)
# 設定按鈕文字
btn.setText('執行')
# 設定按鈕位置
# btn.move(300,300)
btn.setGeometry(300,300,200,30)

w.show()
sys.exit(app.exec())