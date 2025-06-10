import cv2

# 捕捉影像
v = cv2.VideoCapture(0)

print(v.isOpened())

while (v.isOpened()):
   ret, frame = v.read()
   print(frame)
   cv2.imshow('hey', frame)
   key = cv2.waitKey(1)
   # ESC
   if key == 27:
      break
   # if key == ord('q'):
   #    break