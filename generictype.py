from dataclasses import dataclass, field

@dataclass
class Coord:
    x:int = None
    y:int = None

    def __str__(self):
        return "(%d, %d)"%(self.x, self.y)

@dataclass
class Dot:
    name:str = None
    coord:Coord = field(default_factory=Coord)
    liveCount:int = None
    keyworkds:list = field(default_factory=list)

    def __str__(self):
        return self.name
    
@dataclass
class FloorData:
    name:str = None
    include:list = None
    exclude:list = None
    dots:list[Dot] = field(default_factory=list[Dot])

    def __str__(self):
        return self.name