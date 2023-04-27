import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon(x_center,y_center,radius):
    half_r = radius/2
    x = [x_center+x_value, x_center, x_center-x_value, x_center-x_value, x_center, x_center+x_value]
    y= [y_center+half_r, y_center+radius, y_center+half_r, y_center-half_r, y_center-radius, y_center-half_r]
    
    return x,y

def get_centers():
    for i in range(0,rows):
            if i%2 ==0:
                for j in range(0, columns):
                    x_centers_value = int_x_center + 2*j*x_value
                    x_centers_list.append(x_centers_value)
                    y_centers_value = int_y_center - (3/2)*radius*i
                    y_centers_list.append(y_centers_value)
            if i%2 ==1:
                for j in range(0, columns):
                    x_centers_value = int_x_center + x_value + 2*j*x_value
                    x_centers_list.append(x_centers_value)
                    y_centers_value = int_y_center - (3/2)*radius*i
                    y_centers_list.append(y_centers_value)
    return x_centers_list, y_centers_list

def plot_hexagon():
    color=[]
    fig = plt.figure()
    ax = fig.add_subplot()
    get_centers()
    i=0
    while i < len(x_centers_list):
        x, y = Hexagon(x_centers_list[i],y_centers_list[i],radius) 
        color.append(tuple(np.random.choice(range(0,2),size=3)))
        ax.fill(x, y, color = 'none', edgecolor='black')
        # ax.fill(x, y, color=color[i])
        # ax.fill(x, y, color='g')
        i+=1
    plt.gca().set_aspect('equal') 
    plt.show()


x_centers_list = []
y_centers_list = []
radius=int(input('Radius: '))
int_x_center =int(input('x-coordinate of initial hexagon center: '))
int_y_center =int(input('y-coordinate of initial hexagon center: '))
rows = int(input('Number of rows: '))
columns = int(input('Number of colums: '))
x_value = math.sqrt(radius**2 - (radius/2)**2) 

plot_hexagon()

