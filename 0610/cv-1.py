import cv2

img = cv2.imread('./IMG_8402.JPEG')

cv2.imshow('hello', img)

# 毫秒
cv2.waitKey(0)