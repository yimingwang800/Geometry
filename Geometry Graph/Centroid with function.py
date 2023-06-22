import matplotlib.pyplot as plt
import numpy as np
import math
fig, ax = plt.subplots()

def Triangle():
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

def Centroid():
    x_sum = 0
    y_sum = 0
    for i in range(0,3):
        x_sum+=triangle_x_coordinates_list[i]
        y_sum+=triangle_y_coordinates_list[i]
    centroid_x = round(x_sum/3,2)
    centroid_y = round(y_sum/3,2) 
        
    plt.scatter(centroid_x, centroid_y)
    xy= (centroid_x, centroid_y)
    ax.annotate(f'{"C"} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))

    #return centroid_x, centroid_y

def get_centers():  
    global median_x_values_list, median_y_values_list
    for i in range(0,3):
        if(i==0):
            median_x_values= triangle_x_coordinates_list[i] 
            median_x_values_list.append(median_x_values)
            median_x_values=(triangle_x_coordinates_list[i+1]+triangle_x_coordinates_list[i+2])/2
            median_x_values_list.append(median_x_values)
            median_y_values= triangle_y_coordinates_list[i] 
            median_y_values_list.append(median_y_values)
            median_y_values=(triangle_y_coordinates_list[i+1]+triangle_y_coordinates_list[i+2])/2
            median_y_values_list.append(median_y_values)
        if(i==1):
            median_x_values= triangle_x_coordinates_list[i] 
            median_x_values_list.append(median_x_values)
            median_x_values=(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i+1])/2
            median_x_values_list.append(median_x_values)
            median_y_values= triangle_y_coordinates_list[i] 
            median_y_values_list.append(median_y_values)
            median_y_values=(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i+1])/2
            median_y_values_list.append(median_y_values) 
        else:   
            median_x_values= triangle_x_coordinates_list[i] 
            median_x_values_list.append(median_x_values)
            median_x_values=(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i-2])/2
            median_x_values_list.append(median_x_values)
            median_y_values= triangle_y_coordinates_list[i] 
            median_y_values_list.append(median_y_values)
            median_y_values=(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i-2])/2
            median_y_values_list.append(median_y_values)      

def plot_Graph():
    Triangle()
  
    Centroid()

    get_centers()
    ax.fill(median_x_values_list, median_y_values_list, color = 'none', edgecolor='black')

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
median_x_values_list = []
median_y_values_list = []

plot_Graph()