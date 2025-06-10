import cv2
import os

os.makedirs('images', exist_ok=True)

# img = cv2.imread('./IMG_8402.JPEG')
img = cv2.imread('./IMG_8402.JPEG', cv2.IMREAD_REDUCED_COLOR_4)

# jpeg,0-100, 95
cv2.imwrite('./images/output.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,2])

# png, 0-9 ,數字越大，檔案越小，壓縮時間越長
cv2.imwrite('./images/output.png',img,[cv2.IMWRITE_PNG_COMPRESSION,0])
cv2.imwrite('./images/output2.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])

# webp, 0-100
cv2.imwrite('./images/output.webp',img,[cv2.IMWRITE_WEBP_QUALITY,0])
cv2.imwrite('./images/output2.webp',img,[cv2.IMWRITE_WEBP_QUALITY,100])

