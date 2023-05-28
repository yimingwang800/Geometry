import matplotlib.pyplot as plt
import numpy as np
import math

def Hexagon(x_center,y_center,r):
    half_r = r/2
    x = [x_center+x_value, x_center, x_center-x_value, x_center-x_value, x_center, x_center+x_value]
    y= [y_center+half_r, y_center+r, y_center+half_r, y_center-half_r, y_center-r, y_center-half_r]
    
    return x,y

print("Please enter the radius:")
r=int(input())
x_centers_list = []
y_centers_list = []
print("Please enter the x-coordinate of the initial hexagon center:")
int_x_center =int(input())
print("Please enter the y-coordinate of the initial hexagon center:")
int_y_center =int(input())
print("Please enter the number of rows:")
rows = int(input())
print("Please enter the number of colums:")
columns = int(input())
x_value = math.sqrt(r**2 - (r/2)**2) 
for i in range(0,rows):
        if i%2 ==0:
            for j in range(0, columns):
                x_centers_value = int_x_center + 2*j*x_value
                x_centers_list.append(x_centers_value)
                y_centers_value = int_y_center - (3/2)*r*i
                y_centers_list.append(y_centers_value)
        if i%2 ==1:
            for j in range(0, columns):
                x_centers_value = int_x_center + x_value + 2*j*x_value
                x_centers_list.append(x_centers_value)
                y_centers_value = int_y_center - (3/2)*r*i
                y_centers_list.append(y_centers_value)

 
color=[]
fig = plt.figure()
ax = fig.add_subplot()
i=0
while i < len(x_centers_list):
    x, y = Hexagon(x_centers_list[i],y_centers_list[i],r) 
    color.append(tuple(np.random.choice(range(0,2),size=3)))
    ax.fill(x, y, color = 'none', edgecolor='black')
    # ax.fill(x, y, color=color[i])
    # ax.fill(x, y, color='g')
    i+=1

plt.gca().set_aspect('equal') 
plt.show()