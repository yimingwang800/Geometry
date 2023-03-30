import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon_coordinates(x_center_list,y_center_list,num_of_hexagons):
    half_r = r/2
    x_value = math.sqrt(r**2 - half_r**2)
    x_coordinates = []
    y_coordinates = []
    i=0
    while i < num_of_hexagons:
        x = [x_center_list[i]+x_value, x_center_list[i], x_center_list[i]-x_value, x_center_list[i]-x_value, x_center_list[i], x_center_list[i]+x_value]
        y= [y_center_list[i]+half_r, y_center_list[i]+r, y_center_list[i]+half_r, y_center_list[i]-half_r, y_center_list[i]-r, y_center_list[i]-half_r]
        x_coordinates.append(x)
        y_coordinates.append(y) 
        i+=1

    for i in range(num_of_hexagons):
       fig = plt.figure()
       ax = fig.add_subplot()
       ax.fill(x_coordinates[i], y_coordinates[i], color='r')
       plt.gca().set_aspect('equal') 
    
    # fig = plt.figure()
    # ax = fig.add_subplot()
    # #ax.fill(x[0], y[0],x[1], y[1], x[2], y[2],x[3], y[3], color='r') 
    # ax.fill(x_coordinates[0], y_coordinates[0], color='r') 
    # ax.fill(x_coordinates[1], y_coordinates[1], color='y') 
    # ax.fill(x_coordinates[2], y_coordinates[2], color='b') 
    # ax.fill(x_coordinates[3], y_coordinates[3], color='g') 
    # plt.gca().set_aspect('equal') 
    plt.show()

num_of_hexagons = int(input())
r=int(input())
x_center_list = []
y_center_list = []
for i in range(num_of_hexagons):
    x=int(input())
    x_center_list.append(x)
    y=int(input())
    y_center_list.append(y)
#num_of_hexagons =len(x_center_list)


Hexagon_coordinates(x_center_list,y_center_list,num_of_hexagons)   



