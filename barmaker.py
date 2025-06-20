import cv2
import numpy as np
from genericheatmap import gray2heat

LENGTH = 1080

if __name__ == "__main__":
    image = np.zeros((135, 1080, 3), np.uint8)
    
    for i in range(LENGTH):
        heatRgb = gray2heat(i/LENGTH, makeint=True)

        image[:,i,0] = heatRgb[0]
        image[:,i,1] = heatRgb[1]
        image[:,i,2] = heatRgb[2]
    
    cv2.imshow("bar", image)
    cv2.waitKey(0)
    cv2.imwrite("bar.png", image)