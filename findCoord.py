import cv2
import time

IMAGE_DIR = "./image/school.png"
lastClick = time.time()

def onMouse(event, x, y, flags, param):
    global lastClick

    if event == cv2.EVENT_LBUTTONDOWN:
        nowClick = time.time()
        if (nowClick - lastClick) > 3:
            print()
        print("(%d, %d)"%(x, y))

        lastClick = nowClick

img = cv2.imread(IMAGE_DIR)
cv2.imshow('image', img)
cv2.setMouseCallback('image', onMouse)
cv2.waitKey()