import matplotlib.pyplot as plt
import numpy as np
import math

def fill ():
    fig = plt.figure()
    ax = fig.add_subplot()
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    x = [-2, 4, -1]
    y = [2, 1, -3]
    ax.fill(x, y, color='y')

    x = [-1, 5, -1]
    y = [1, 2, -3]
    x.fill(x, y, color='z')
