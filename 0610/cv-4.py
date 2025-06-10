import cv2

img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_4)

# 矩形
cv2.rectangle(img, (100,120), (240,240), (0,255,0), 3)
# 線
cv2.line(img, (200, 200), (300,300), (0, 128, 255), 2)

# 箭頭
cv2.arrowedLine(img, (300,300),(200,100),(0, 255, 100),2,5)

# 圓形
cv2.circle(img, (222,222), 100, (200, 255, 0), 2)


cv2.imshow('hello',img)

cv2.waitKey(0)

cv2.destroyWindow('hello')