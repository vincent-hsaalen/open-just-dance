import matplotlib.pyplot as plt

# 1st line
point_1 = [1,3]
point_2 = [2,6]

# 2nd line
point_3 = [4,6]
point_4 = [1,2]

x_values = [[point_1[0], point_3[0]],[point_2[0], point_4[0]]]
y_values = [[point_1[1], point_3[1]],[point_2[1], point_4[1]]]

plt.plot(x_values, y_values, 'red')
plt.show()