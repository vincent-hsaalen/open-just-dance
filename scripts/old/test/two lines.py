import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5,5,100)
y1 = 2*x1+1
x2 = np.linspace(-5,5,100)
y2 = -2*x2+1
plt.plot(x1, y1, '-r', label='y=2x+1')
plt.plot(x2, y2, '-r', label='y=-2x+2')
plt.title('Graph of y=2x+1')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.legend(loc='upper left')
plt.grid()
plt.show()