import matplotlib.pyplot as plt
import numpy as np



M1:int = 2
M2:int = -2
B1:int = 1
B2:int = 1
x1 = np.linspace(-5,5,100)
y1 = M1*x1+B1
x2 = np.linspace(-5,5,100)
y2 = M2*x2+B2

angle_bg = np.tan(np.absolute((M1-M2) / (1+M1*M2)))
print(angle_bg)
angle_gr = 360 - np.degrees(angle_bg)

print(angle_gr)
plt.plot(x1, y1, '-r', label='y=2x+1')
plt.plot(x2, y2, '-r', label='y=-2x+1')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()
