import matplotlib.pyplot as plt
import numpy as np
import math

def fill():
    fig = plt.figure()
    ax = fig.add_subplot()
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    r = 8
    a = math.pi/3
    x_value = r*math.cos(a)
    y_value = r*math.sin(a)
    x_1 = [6, 8, 10, 18]
    y_1 = [6, 12, 15, 17]
    x_2 = [r, x_value, -x_value, -r, -x_value, x_value]
    y_2 = [0, y_value, y_value, 0, -y_value, -y_value]
    ax.fill(x_1, y_1, color='y')
    ax.fill(x_2, y_2, color='r')
    for i, xy in enumerate(zip(x_1, y_1)):
        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2)) 
    for i, xy in enumerate(zip(x_2, y_2)):
        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2))
    plt.gca().set_aspect('equal')
    plt.show()


fill()