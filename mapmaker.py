import cv2
import numpy as np
import math

import tqdm

from generictype import Dot
from genericheatmap import gray2heat

MAX_HEAT = 40000

class Map:
    def __init__(self, alphaMap:cv2.typing.MatLike, mainMap:cv2.typing.MatLike, coverMap:cv2.typing.MatLike|None, maxHeat:int=MAX_HEAT):
        self.alphaMap = alphaMap
        self.mainMap = mainMap
        self.coverMap = coverMap[:,:,0:3]
        self.coverMask = coverMap[:,:, 3]
        self.mapShape:tuple = self.alphaMap.shape
        self.dots:list[Dot] = []
        self.maxHeat = maxHeat
        print(self.mapShape)

    def addDot(self, dot:Dot) -> None:
        self.dots.append(dot)

    def debugMap(self) -> cv2.typing.MatLike:
        returnMap = np.full((*self.mapShape, 3), 255, np.uint8)

        cv2.copyTo()

        return returnMap

    def exportFinal(self) -> cv2.typing.MatLike:
        pass

    def exportHeapmap(self) -> None:
        returnMap = np.full((*self.mapShape, 3), 255, np.uint8)

        for yCoord in tqdm.tqdm(range(returnMap.shape[0])):
            for xCoord in range(returnMap.shape[1]):
                returnMap[yCoord][xCoord] = gray2heat(self.calcExamine(xCoord, yCoord), makeint=True)
            # if yCoord == 1000:
            #     return returnMap
        
        return returnMap

    def calcExamine(self, x, y):
        # 각 좌표별 값
        dotDistanceSquare = np.zeros((len(self.dots)), np.float64)
        for dotIdx, dot in enumerate(self.dots):
            # 제곱 가중치
            dotDistanceSquare[dotIdx] = (x - dot.coord.x)**2 + (y - dot.coord.y)**2
        
        if 0 in dotDistanceSquare:
            for dot in self.dots:
                if (dot.coord.x == x) and (dot.coord.y == y):
                    return dot.liveCount / self.maxHeat

        dotDistanceDivided = 1 / dotDistanceSquare
        dotWeights = dotDistanceDivided / np.sum(dotDistanceDivided)
        dotLiveCounts = np.array(list(map(lambda x: x.liveCount, self.dots)))

        return np.sum(dotWeights*dotLiveCounts) / self.maxHeat



if __name__ == "__main__":
    heatmap = Map(
        cv2.imread("./image/school-alpha.png", cv2.IMREAD_GRAYSCALE),
        cv2.imread("./image/school-main.png", cv2.IMREAD_GRAYSCALE),
        cv2.imread("./image/school-cover.png", cv2.IMREAD_UNCHANGED)
    )

    cv2.imshow('image', heatmap.debugMap())
    cv2.waitKey(0)
    cv2.destroyAllWindows()