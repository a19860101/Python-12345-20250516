from PyQt6 import QtWidgets
import sys

# 建立應用程式
app = QtWidgets.QApplication(sys.argv)

# 建立視窗
w = QtWidgets.QWidget()

# 設定標題
w.setWindowTitle('哈囉Python')

# 設定尺寸
w.resize(1024, 768)

# 使用網頁 CSS 樣式設定背景
# w.setStyleSheet('background-color:#ffaa00')
# w.setStyleSheet('background-color:pink')

# 顯示
w.show()

# 執行
sys.exit(app.exec())