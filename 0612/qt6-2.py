from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
w = QtWidgets.QWidget()

w.setWindowTitle('哈囉Python')
w.resize(600,400)

# 加入文字標籤
label = QtWidgets.QLabel(w)
# 移動位置
label.move(150,50)
# 設定文字
label.setText('文字標籤')
# 設定文字樣式
# label.setStyleSheet('font-size:30px; color:red')

w.show()
sys.exit(app.exec())