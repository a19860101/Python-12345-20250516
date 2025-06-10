import cv2

# img = cv2.imread('./IMG_8402.JPEG')
img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_4)

# print(img.shape)
# print(img.size)

# flip
# 上下翻轉
# img = cv2.flip(img, 0)
# 左右翻轉
# img = cv2.flip(img, 1)
# 上下左右翻轉
# img = cv2.flip(img, -1)

# 逆時針旋轉90deg
# img = cv2.transpose(img)

# roate
# 旋轉180
# img = cv2.rotate(img, cv2.ROTATE_180)
# 順時鐘旋轉90
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# 逆時鐘旋轉90
# img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# resize
# img = cv2.resize(img,(300,300))


cv2.imshow('hello', img)

# 毫秒 1秒鐘=1000毫秒，0為不關閉
cv2.waitKey(0)

cv2.destroyWindow('hello')