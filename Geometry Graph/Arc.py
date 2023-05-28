import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
#from matplotlib.patches import Arc
#from matplotlib import patches

def ellipse():
    fig, ax = plt.subplots()
    arc = patches.Arc(xy = (0,0), width = 8, height = 4, angle=0, theta1=90, theta2=270, color = 'r')
    ax.add_patch(arc)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle='--')

    plt.gca().set_aspect('equal', adjustable='box')
    min_x = -5
    max_x = 5
    min_y = -5
    max_y = 5
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x, step=step))
    ax.set_yticks(np.arange(min_y, max_y, step=step))
    plt.show()

ellipse()