import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.patches as patches
#from matplotlib.patches import Arc
#from matplotlib import patches

def ellipse(x_center, y_center, arc_width, arc_height, rotation_angle, start_theta, end_theta):
    fig, ax = plt.subplots()
    arc = patches.Arc(xy = (x_center,y_center), width = arc_width, height = arc_height, 
                      angle=rotation_angle, theta1=start_theta, theta2=end_theta, color = 'r')
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

x_center =float(input('x-coordinate of origin: '))
y_center =float(input('y-coordinate of origin: '))
arc_width = float(input('Width: '))
arc_height= float(input('Height: '))
rotation_angle = float(input('Rotation of the ellipse in degrees: '))
start_theta = float(input('Starting angle: '))
end_theta = float(input('Ending angle: '))

ellipse(x_center, y_center, arc_width, arc_height, rotation_angle, start_theta, end_theta)