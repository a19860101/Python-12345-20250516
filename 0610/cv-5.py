import cv2

# 載入圖片
# img = cv2.imread('2023yoasobi_20231123160349.jpg')
img = cv2.imread('yuuri-billboard-japan-2022-billboard-1548.webp')
# img = cv2.imread('antonio-verdin-TjNzMz220Wo-unsplash.jpg', cv2.IMREAD_REDUCED_COLOR_4)

# 轉灰階
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 載入 OpenCV 提供的預訓練人臉分類器
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print(face_cascade)

# 偵測人臉
faces = face_cascade.detectMultiScale(gray,
                                      scaleFactor=1.1,
                                      minNeighbors=5,
                                      minSize=(50, 50))

print(faces)

# 偵測到的人臉加上框
for (x, y, w, h) in faces:
    print(x,y,w,h)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow('hello',img)

cv2.waitKey(0)

cv2.destroyWindow('hello')

