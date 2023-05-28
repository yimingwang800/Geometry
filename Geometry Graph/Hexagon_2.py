import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon():
    fig = plt.figure()
    ax = fig.add_subplot()
    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # r = 8
    # center_x = 0
    # center_y = 0
    half_r = r/2
    x_value = math.sqrt(r**2 - half_r**2)
    x = [center_x+x_value, center_x, center_x-x_value, center_x-x_value, center_x, center_x+x_value]
    y = [center_y+half_r, center_y+r, center_y+half_r, center_y-half_r, center_y-r, center_y-half_r]
    ax.fill(x, y, color='y')

    for i, xy in enumerate(zip(x, y)):
        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2)) 
    
    plt.gca().set_aspect('equal')

    plt.show()

Hexagons = []


print("Do you want to generate more hexagons? (Y or N)")
answer = input()
while (answer == 'Y'):
    center_x = int(input())
    center_y = int(input())
    r = int(input())
    Hexagon(center_x, center_y, r)
    print("Do you want to generate more hexagons? (Y or N)")
    answer = input()


# center_x = int(input())
# center_y = int(input())
# r = int(input())
# fill(center_x, center_y, r)
