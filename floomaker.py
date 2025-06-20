from dataclasses import dataclass, field
import csv
import json

from generictype import Coord, Dot, FloorData
    

CSV_DIR = "./data/dots.csv"
FILTER_DIR = "./data/filter.json"

def readData(filterDir:str, csvDir:str) -> tuple[list[FloorData], list[Dot]]:
    with open(FILTER_DIR, "r") as f:
        data:dict = json.load(f)
        floors = list(
            map(lambda items: FloorData(items[0], items[1]["include"], items[1]["exclude"]), data.items())
        )

    with open(CSV_DIR, "r") as f:
        dots = []
        rdr = csv.reader(f, skipinitialspace=True)
        next(rdr)

        for line in rdr:
            dots.append(Dot(
                name=line[0], liveCount=int(line[1]), coord=Coord(int(line[2]), int(line[3])), keyworkds=json.loads(line[4])
            ))
    
    return floors, dots

def filterData(floors:list[FloorData], dots:list[Dot]) -> list[FloorData]:
    for dot in dots:
        for floor in floors:
            for key in floor.include:
                if key in dot.keyworkds:
                    floor.dots.append(dot)
                    break

    for floor in floors:
        dot2del:list = []
        for i, dot in enumerate(floor.dots):
            for key in dot.keyworkds:
                if key in floor.exclude:
                    dot2del.insert(0, i)
                    break
        for i in dot2del:
            del floor.dots[i]
    
    return floors

def makeFloor() -> list[FloorData]:
    return filterData(
        *readData(FILTER_DIR, CSV_DIR)
    )

if __name__ == "__main__":
    # filter
    floors = makeFloor()
    
    for floor in floors:
        print("==%s==(%d)"%(floor.name, len(floor.dots)))
        for dot in floor.dots:
            print(dot, end=", ")
        print("\n")