import cv2

# 載入圖片
img = cv2.imread('2023yoasobi_20231123160349.jpg')

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 載入 OpenCV 提供的預訓練人臉分類器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print(face_cascade)
