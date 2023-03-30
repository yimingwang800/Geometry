import matplotlib.pyplot as plt
import numpy as np

def fill():
    fig = plt.figure()
    ax = fig.add_subplot()
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    x_1 = [6, 8, 10, 18]
    y_1 = [6, 12, 15, 17]
    x_2 = [4, 2, -2, -4, -2, 2]
    y_2 = [0, 3, 3, 0, -3, -3]
    ax.fill(x_1, y_1, color='y')
    ax.fill(x_2, y_2, color='r')
    for i, xy in enumerate(zip(x_1, y_1)):
        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2)) 
    for i, xy in enumerate(zip(x_2, y_2)):
        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2))
    plt.show()

fill()