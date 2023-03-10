import matplotlib.pyplot as plt
import numpy as np

def draw_circle():
    #circle_1 = plt.Circle((0, 0), 0.5, color='r')
    fig, ax = plt.subplots()    #Only one subplot
    
    center = (0, 0)     #Tuple
    radius = 5
    circle_1 = plt.Circle(center, radius, color='r', linewidth=1, fill=False)
    ax.add_patch(circle_1)

    center = (0, 0)     #Tuple
    radius = 10
    circle_2 = plt.Circle(center, radius, color='b', linewidth=1, fill=False)
    ax.add_patch(circle_2)

    #lines
    x_1 = [0, 0]
    y_1 = [10, -10]
    plt.plot(x_1, y_1)

    x_2 = [10, -10]
    y_2 = [0, 0]
    plt.plot(x_2, y_2)

    #labels 
    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')
    
    plt.title('Circle Graph')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

draw_circle()
