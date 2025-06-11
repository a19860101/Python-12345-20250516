import cv2
import os
from datetime import datetime

# 取得攝影機
v = cv2.VideoCapture(0)
# 載入opencv人臉訓練模型
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 建立儲存資料夾
save_dir = "faces"
os.makedirs(save_dir, exist_ok=True)

while (v.isOpened()):
    ret, frame = v.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(1000)
    # print(frame)
    faces = face_cascade.detectMultiScale(gray,
                                         scaleFactor=1.1,
                                         minNeighbors=5,
                                         minSize=(50, 50))
    saved_count = 0
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.putText(frame,
                    'Face Detected',
                    (x, y - 5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    1)


        # 自動儲存臉部區域圖片
        face_img = frame[y:y + h, x:x + w]
        # 建立時間字串
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        # 建立檔名
        filename = os.path.join(save_dir, f"face_{timestamp}_{saved_count}.jpg")
        # 儲存
        cv2.imwrite(filename, face_img)
        print(f"儲存：{filename}")
        saved_count += 1

    cv2.imshow('hey', frame)

   # # ESC
    if key == 27:
        break

"""
FONT_HERSHEY_SIMPLEX：正常大小無襯線字體、
FONT_HERSHEY_PLAIN：小號無襯線字體、
FONT_HERSHEY_DUPLEX：正常大小無襯線字體，比FONT_HERSHEY_SIMPLEX複雜一點、
FONT_HERSHEY_COMPLEX：正常大小有襯線字體、
FONT_HERSHEY_TRIPLEX：正常大小有襯線字體，比FONT_HERSHEY_COMPLEX複雜一點、
FONT_HERSHEY_COMPLEX_SMALL：FONT_HERSHEY_COMPLEX的小號、
FONT_HERSHEY_SCRIPT_SIMPLEX：手寫風格細體、
FONT_HERSHEY_SCRIPT_COMPLEX：手寫風格粗體，
"""
