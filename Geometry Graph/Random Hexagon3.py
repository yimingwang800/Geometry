import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon(x_center,y_center,r):
    half_r = r/2
    x = [x_center+x_value, x_center, x_center-x_value, x_center-x_value, x_center, x_center+x_value]
    y= [y_center+half_r, y_center+r, y_center+half_r, y_center-half_r, y_center-r, y_center-half_r]
    
    return x,y


num_of_hexagons = int(input())
r=int(input())
x_centers_list = []
y_centers_list = []
x_center =int(input())
x_centers_list.append(x_center)
y_center =int(input())
y_centers_list.append(y_center)
x_value = math.sqrt(r**2 - (r/2)**2) 
for i in range(1,num_of_hexagons):
    if i%3 == 0:  
        x_centers_value = x_centers_list[i-3]+2*x_value
        x_centers_list.append(x_centers_value)
        y_centers_value = y_center
        y_centers_list.append(y_centers_value)
    if i%3 == 1:  
        x_centers_value = x_centers_list[i-1]+x_value
        x_centers_list.append(x_centers_value)
        y_centers_value = y_center+(3/2)*r
        y_centers_list.append(y_centers_value)
    if i%3 == 2:  
        x_centers_value = x_centers_list[i-2]+x_value
        x_centers_list.append(x_centers_value)
        y_centers_value = y_center-(3/2)*r
        y_centers_list.append(y_centers_value)
 
color=[]
fig = plt.figure()
ax = fig.add_subplot()
i=0
while i < num_of_hexagons:
    x, y = Hexagon(x_centers_list[i],y_centers_list[i],r) 
    color.append(tuple(np.random.choice(range(0,2),size=3)))
    ax.fill(x, y, color = 'none', edgecolor='black')
    # ax.fill(x, y, color=color[i])
    # ax.fill(x, y, color='g')
    i+=1

plt.gca().set_aspect('equal') 
plt.show()

