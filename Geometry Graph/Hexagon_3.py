import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon(center_x1, center_y1,center_x2, center_y2, r):
    fig = plt.figure()
    ax = fig.add_subplot()
 #   names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    half_r = r/2
    x_value = math.sqrt(r**2 - half_r**2)
    x1 = [center_x1+x_value, center_x1, center_x1-x_value, center_x1-x_value, center_x1, center_x1+x_value]
    y1 = [center_y1+half_r, center_y1+r, center_y1+half_r, center_y1-half_r, center_y1-r, center_y1-half_r]
    ax.fill(x1, y1, color='y')

#    for i, xy in enumerate(zip(x1, y1)):
#        ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2)) 

    x2 = [center_x2+x_value, center_x2, center_x2-x_value, center_x2-x_value, center_x2, center_x2+x_value]
    y2 = [center_y2+half_r, center_y2+r, center_y2+half_r, center_y2-half_r, center_y2-r, center_y2-half_r]
    ax.fill(x2, y2, color='r')

 #   for i, xy in enumerate(zip(x2, y2)):
 #       ax.annotate(' {} {}'.format(names[i], xy), xy = xy, textcoords='offset points', xytext=(5, 2)) 
    
    plt.gca().set_aspect('equal')
    plt.show()


def main():

    #center_x1 = int(input())
    #center_y2 = int(input())
    #r = int(input())
    r=2
    center_x1 = 0
    center_y1 = 0
    center_x2 = center_x1+math.sqrt(r**2 - (r/2)**2)
    center_y2 = 3
    Hexagon(center_x1, center_y1,center_x2, center_y2, r)

if __name__ == "__main__":
    main()

# center_x = int(input())
# center_y = int(input())
# r = int(input())
# fill(center_x, center_y, r)
