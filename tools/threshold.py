import cv2

img = cv2.imread("./image/school-building-bw.png", cv2.IMREAD_GRAYSCALE)
img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('image', img)
cv2.waitKey()

cv2.imwrite("abcd.png", img)