from PyQt6 import QtWidgets,QtGui
import sys


app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

w.setWindowTitle('哈囉Python')
w.resize(600,400)

font = QtGui.QFont()
# 粗體
font.setBold(True)
# 斜體
font.setItalic(True)
# 底線
font.setUnderline(True)
# 字體
font.setFamily('新細明體')
# 大小
font.setPointSize(20)


label = QtWidgets.QLabel(w)
label.move(50,50)
label.setText('文字標籤')

l2 = QtWidgets.QLabel(w)
l2.move(200,200)
l2.setText('文字二')

# 套用樣式
label.setFont(font)
l2.setFont(font)

w.show()
sys.exit(app.exec())