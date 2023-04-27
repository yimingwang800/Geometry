import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon(x_center,y_center,r):
    half_r = r/2
    x_value = math.sqrt(r**2 - half_r**2)
    x = [x_center+x_value, x_center, x_center-x_value, x_center-x_value, x_center, x_center+x_value]
    y= [y_center+half_r, y_center+r, y_center+half_r, y_center-half_r, y_center-r, y_center-half_r]
    return x,y

    # for i in range(num_of_hexagons):
    #    fig = plt.figure()
    #    ax = fig.add_subplot()
    #    ax.fill(x_coordinates[i], y_coordinates[i], color='r')
    #    plt.gca().set_aspect('equal') 

num_of_hexagons = int(input())
r=int(input())
x_center = []
y_center = []
for i in range(num_of_hexagons):
    x=int(input())
    x_center.append(x)
    y=int(input())
    y_center.append(y)
#num_of_hexagons =len(x_center_list)

fig = plt.figure()
ax = fig.add_subplot()
i=0
while i < num_of_hexagons:
    x, y = Hexagon(x_center[i],y_center[i],r)  
    ax.fill(x, y, color='r')
    i+=1

plt.gca().set_aspect('equal') 
plt.show()

