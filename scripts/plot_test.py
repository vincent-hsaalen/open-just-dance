import matplotlib.pyplot as plt 
from matplotlib import rcParams

def main():
    POINTS: list = [[1, 3], [2, 6], [4, 6], [1, 2]] # [point1, point2, point3, point4]

    x_values: list = [[POINTS[0][0], POINTS[2][0]],[POINTS[1][0], POINTS[3][0]]]
    y_values: list = [[POINTS[0][1], POINTS[2][1]],[POINTS[1][1], POINTS[3][1]]]
   
    rcParams["toolbar"] = "None"
    plt.plot(x_values, y_values , "red")
    plt.title("Example")
    plt.show()


if __name__ == "__main__":
    main()
