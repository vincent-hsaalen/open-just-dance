import numpy as np

def calculateAngle(m1: np.float64, m2: np.float64):
    global counter
    angle_bg = np.arctan(np.absolute((m1 - m2) / (1+m1*m2)))
    angle_gr = np.degrees(angle_bg)

    if angle_gr < 0:
        counter += 1
        print(f"[{counter}. Aufruf] -> kleiner als 0!(Negativ)")
        angle_gr = 180 + angle_gr

print(calculateAngle(0, 0))

