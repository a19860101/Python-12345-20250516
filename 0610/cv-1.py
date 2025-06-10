import cv2

# img = cv2.imread('./IMG_8402.JPEG')
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_2)
img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_4)
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_8)
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_GRAYSCALE_2)
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_GRAYSCALE_4)
# img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_GRAYSCALE_8)

cv2.imshow('hello', img)

# 毫秒 1秒鐘=1000毫秒，0為不關閉
cv2.waitKey(0)

cv2.destroyWindow('hello')