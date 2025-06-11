import cv2

# 取得攝影機
v = cv2.VideoCapture(0)
# 載入opencv人臉訓練模型
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while (v.isOpened()):
    ret, frame = v.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(1)
    print(frame)
    faces = face_cascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(50, 50))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    frame = cv2.flip(frame,1)
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow('hey', frame)

   # # ESC
    if key == ord('q'):
        break
