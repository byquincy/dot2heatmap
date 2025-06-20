import json

import floomaker
from mapmaker import Map
import cv2


if __name__ == "__main__":
    floors = floomaker.makeFloor()
    map1 = Map(
        cv2.imread("./image/school-alpha.png", cv2.IMREAD_GRAYSCALE),
        cv2.imread("./image/school-main.png", cv2.IMREAD_GRAYSCALE),
        cv2.imread("./image/school-cover.png", cv2.IMREAD_UNCHANGED),
        maxHeat=17200
    )

    print(floors[3].name)
    for dot in floors[3].dots:
        map1.addDot(dot)
    
    heatmap = map1.exportHeapmap()
    cv2.imshow('image', heatmap)
    cv2.imwrite('heatmap.png', heatmap)
    cv2.waitKey(0)
    cv2.destroyAllWindows()