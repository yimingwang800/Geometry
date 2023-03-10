import matplotlib.pyplot as plt
import numpy as np

def draw_circle():
    #circle_1 = plt.Circle((0, 0), 0.5, color='r')
    fig, ax = plt.subplots()    #Only one subplot
    
    start_num = -10
    end_num = 10
    step = 1
    #lines
    x_1 = [0, 0]
    y_1 = [10, -10]
    plt.plot(x_1, y_1)

    x_2 = [10, -10]
    y_2 = [0, 0]
    plt.plot(x_2, y_2)
    radius = 3

    for x in range (10):
        center = (x-10, 0)     #Tuple
        x = plt.Circle(center, radius, color='r', linewidth=1, fill=False)
        ax.add_patch(x)
    for x in range (10):
        center = (x, 0)     #Tuple
        x = plt.Circle(center, radius, color='r', linewidth=1, fill=False)
        ax.add_patch(x)
    for y in range (10):
        center = (0, y-10)     #Tuple
        y = plt.Circle(center, radius, color='b', linewidth=1, fill=False)
        ax.add_patch(y)
    for y in range (10):
        center = (0, y)     #Tuple
        y = plt.Circle(center, radius, color='b', linewidth=1, fill=False)
        ax.add_patch(y)

    #labels 
    plt.grid(linestyle = '--')
    plt.gca().set_aspect('equal')
    min_x = start_num-radius
    max_x = end_num+radius
    min_y = start_num-radius
    max_y = end_num+radius
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x+step, step=step))
    ax.set_yticks(np.arange(min_y, max_y+step, step=step))
    
    plt.title('Circle Graph')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()

draw_circle()
