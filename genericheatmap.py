import numpy as np

def interpolate(val:float, y0:float, x0:float, y1:float, x1:float):
    return ((val-x0)*(y1-y0)/(x1-x0)) + y0

def base(val:float):
    if ( val <= -0.75 ): return 0
    elif ( val <= -0.25 ): return interpolate( val, 0.0, -0.75, 1.0, -0.25 )
    elif ( val <= 0.25 ): return 1.0
    elif ( val <= 0.75 ): return interpolate( val, 1.0, 0.25, 0.0, 0.75 )
    else: return 0.0

def gray2heat(gray:float, makeint:bool=False) -> tuple[int, int, int]|tuple[float, float, float]:
    gray = gray*2 - 1
    # BGR
    bgrbase = np.array((base(gray + 0.5), base(gray), base(gray - 0.5)))

    if makeint == True:
        return (bgrbase*255).astype(np.uint8)
    else:
        return bgrbase


if __name__ == "__main__":
    print(gray2heat(1))