import numpy as np

def calculateSlope(x1, y1, x2, y2) -> np.float64:
    return np.round_((y2 - y1) / (x2 - x1), decimals=2)

x1 = np.float64(603.836)
y1 = np.float64(151.419)
x2 = np.float64(603.867)
y2 = np.float64(200.3)

# x          y
# 603.836, 151.419
# 603.867, 200.3
print(calculateSlope(x1, y1, x2, y2))

