import matplotlib.pyplot as plt
import numpy as np
import math
fig, ax = plt.subplots()


def triangle():
    for i in range(0,3):
        Triangle_x_coordinates =float(input(f'x-coordinate of Triangle point {i+1}:'))
        triangle_x_coordinates_list.append(Triangle_x_coordinates)
        Triangle_y_coordinates =float(input(f'y-coordinate of Triangle point {i+1}:'))
        triangle_y_coordinates_list.append(Triangle_y_coordinates)
    
    names = ['P', 'Q', 'R']
    for i, xy in enumerate(zip(triangle_x_coordinates_list, triangle_y_coordinates_list)):
        if i != len(triangle_x_coordinates_list):
            ax.annotate(f'{names[i]} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))
    ax.fill(triangle_x_coordinates_list, triangle_y_coordinates_list, color = 'none', edgecolor='black')

def incenter():
    p = math.sqrt((triangle_y_coordinates_list[1]-triangle_y_coordinates_list[2])**2 + (triangle_x_coordinates_list[1]-triangle_x_coordinates_list[2])**2 )
    q = math.sqrt((triangle_y_coordinates_list[2]-triangle_y_coordinates_list[0])**2 + (triangle_x_coordinates_list[2]-triangle_x_coordinates_list[0])**2 )
    r = math.sqrt((triangle_y_coordinates_list[1]-triangle_y_coordinates_list[0])**2 + (triangle_x_coordinates_list[1]-triangle_x_coordinates_list[0])**2 )

    incenter_x = ((p*triangle_x_coordinates_list[0]+q*triangle_x_coordinates_list[1]+r*triangle_x_coordinates_list[2])/(p+q+r))
    incenter_y = ((p*triangle_y_coordinates_list[0]+q*triangle_y_coordinates_list[1]+r*triangle_y_coordinates_list[2])/(p+q+r))
        
    plt.scatter(incenter_x, incenter_y)
    xy= (incenter_x, incenter_y)
    ax.annotate(f'{"C"} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))

    return incenter_x, incenter_y, p, q, r

def get_incenter_graph_coordinates(incenter_x, incenter_y):
    global incenter_graph_x_values_list, incenter_graph_y_values_list
    for i in range(0,3):
        incenter_graph_x_values= triangle_x_coordinates_list[i] 
        incenter_graph_x_values_list.append(incenter_graph_x_values)
        incenter_graph_x_values=incenter_x
        incenter_graph_x_values_list.append(incenter_graph_x_values)
        incenter_graph_y_values= triangle_y_coordinates_list[i] 
        incenter_graph_y_values_list.append(incenter_graph_y_values)
        incenter_graph_y_values=incenter_y
        incenter_graph_y_values_list.append(incenter_graph_y_values)

def circle(incenter_x, incenter_y, p, q, r):
    degree_P = math.acos((r**2+q**2-p**2)/(2*r*q))
    degree_p_sin_value = math.sin(degree_P)
    radius=(r*q*degree_p_sin_value)/(p+q+r)
    circle=plt.Circle((incenter_x, incenter_y),radius, fill=False)
    ax.add_patch(circle)

def plot_Graph():
    triangle()
  
    incenter_x, incenter_y, p, q, r = incenter()

    get_incenter_graph_coordinates(incenter_x, incenter_y)
    ax.fill(incenter_graph_x_values_list, incenter_graph_y_values_list, color = 'none', edgecolor='black')

    circle(incenter_x, incenter_y, p, q, r)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle='--')

    plt.gca().set_aspect('equal', adjustable='box')
    min_x = -10
    max_x = 11
    min_y = -10
    max_y = 11
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x, step=step))
    ax.set_yticks(np.arange(min_y, max_y, step=step))
    plt.show()

triangle_x_coordinates_list = []
triangle_y_coordinates_list = []
incenter_graph_x_values_list = []
incenter_graph_y_values_list = []

plot_Graph()
