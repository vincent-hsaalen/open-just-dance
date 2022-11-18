import numpy as np

M1:int = 2
M2:int = -2

def calculateAngle(m1, m2) -> np.float64:
    angle_bg = np.tan(np.absolute((m1 - m2) / (1+m1*m2)))
    angle_gr = 360 - np.degrees(angle_bg)
    return np.round_(angle_gr, decimals=2)

print(calculateAngle(M1, M2))