import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagons(x_center,y_center):
    half_r = r/2
    x_value = math.sqrt(r**2 - half_r**2)
    x_coordinates = []
    y_coordinates = []
    x_centers_list = [x_center,x_center+2*x_value,x_center-x_value,x_center+x_value]
    y_centers_list = [y_center,y_center,y_center+(3*r)/2,y_center+(3*r)/2]
    num_of_hexagons =len(x_centers_list)
    i=0
    while i < num_of_hexagons:
        x = [x_centers_list[i]+x_value, x_centers_list[i], x_centers_list[i]-x_value, x_centers_list[i]-x_value, x_centers_list[i], x_centers_list[i]+x_value]
        y= [y_centers_list[i]+half_r, y_centers_list[i]+r, y_centers_list[i]+half_r, y_centers_list[i]-half_r, y_centers_list[i]-r, y_centers_list[i]-half_r]
        x_coordinates.append(x)
        y_coordinates.append(y) 
        i+=1

    #for i in range(num_of_hexagons):
    #    fig = plt.figure()
    #    ax = fig.add_subplot()
    #    ax.fill(x_coordinates[i], y_coordinates[i], color='r')
    #    plt.gca().set_aspect('equal') 
    

    fig = plt.figure()
    ax = fig.add_subplot()            
    ax.fill(x_coordinates[0], y_coordinates[0], color='r') 
    ax.fill(x_coordinates[1], y_coordinates[1], color='y') 
    ax.fill(x_coordinates[2], y_coordinates[2], color='b') 
    ax.fill(x_coordinates[3], y_coordinates[3], color='g') 
    plt.gca().set_aspect('equal') 
    plt.show()

r=int(input())
x_center=int(input())
y_center=int(input())

Hexagons(x_center,y_center)   



