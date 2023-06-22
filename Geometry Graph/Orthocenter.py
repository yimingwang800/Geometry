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
    return centroid_x, centroid_y

def Circumcenter():
    d=2*(triangle_x_coordinates_list[0]*(triangle_y_coordinates_list[1]-triangle_y_coordinates_list[2])+
         triangle_x_coordinates_list[1]*(triangle_y_coordinates_list[2]-triangle_y_coordinates_list[0])+
         triangle_x_coordinates_list[2]*(triangle_y_coordinates_list[0]-triangle_y_coordinates_list[1]))
    circumcenter_x_value=((triangle_x_coordinates_list[0]*triangle_x_coordinates_list[0]+triangle_y_coordinates_list[0]*triangle_y_coordinates_list[0])*(triangle_y_coordinates_list[1]-triangle_y_coordinates_list[2])+(triangle_x_coordinates_list[1]*triangle_x_coordinates_list[1] + triangle_y_coordinates_list[1]*triangle_y_coordinates_list[1])*(triangle_y_coordinates_list[2]-triangle_y_coordinates_list[0])+(triangle_x_coordinates_list[2]*triangle_x_coordinates_list[2] + triangle_y_coordinates_list[2]*triangle_y_coordinates_list[2])*(triangle_y_coordinates_list[0]-triangle_y_coordinates_list[1]))/d
    circumcenter_y_value=((triangle_x_coordinates_list[0]*triangle_x_coordinates_list[0]+triangle_y_coordinates_list[0]*triangle_y_coordinates_list[0])*(triangle_x_coordinates_list[2]-triangle_x_coordinates_list[1])+(triangle_x_coordinates_list[1]*triangle_x_coordinates_list[1] + triangle_y_coordinates_list[1]*triangle_y_coordinates_list[1])*(triangle_x_coordinates_list[0]-triangle_x_coordinates_list[2])+(triangle_x_coordinates_list[2]*triangle_x_coordinates_list[2] + triangle_y_coordinates_list[2]*triangle_y_coordinates_list[2])*(triangle_x_coordinates_list[1]-triangle_x_coordinates_list[0]))/d
    circumcenter_x=round(circumcenter_x_value,2)
    circumcenter_y=round(circumcenter_y_value,2)
    return circumcenter_x, circumcenter_y

def Orthocenter(centroid_x, centroid_y,circumcenter_x, circumcenter_y):
    
    Orthocenter_x=round((3*centroid_x-2*circumcenter_x),2)
    Orthocenter_y=round((3*centroid_y-2*circumcenter_y),2)

    plt.scatter(Orthocenter_x, Orthocenter_y)
    xy= (Orthocenter_x, Orthocenter_y)
    ax.annotate(f'{"O"} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))
    return Orthocenter_x, Orthocenter_y

def get_ortho_graph_coordinates(Orthocenter_x, Orthocenter_y):    
    global ortho_graph_x_values_list, ortho_graph_y_values_list
    for i in range(0,3):
        if(i==0):
            ortho_graph_x_values= triangle_x_coordinates_list[i] 
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_x_values=(((triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])**2)*Orthocenter_x+(triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])*(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])*Orthocenter_y-(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])*(triangle_y_coordinates_list[i+2]+triangle_y_coordinates_list[i+1])*triangle_x_coordinates_list[i+2]+(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])*(triangle_x_coordinates_list[i+2]+triangle_x_coordinates_list[i+1])*triangle_y_coordinates_list[i+2])/((triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])**2+(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])**2)
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_y_values= triangle_y_coordinates_list[i] 
            ortho_graph_y_values_list.append(ortho_graph_y_values)
            ortho_graph_y_values=(((triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])**2)*Orthocenter_y+(triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])*(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])*Orthocenter_x+(triangle_y_coordinates_list[i+2]+triangle_y_coordinates_list[i+1])*(triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])*triangle_x_coordinates_list[i+2]-(triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])*(triangle_x_coordinates_list[i+2]+triangle_x_coordinates_list[i+1])*triangle_y_coordinates_list[i+2])/((triangle_x_coordinates_list[i+2]-triangle_x_coordinates_list[i+1])**2+(triangle_y_coordinates_list[i+2]-triangle_y_coordinates_list[i+1])**2)
            ortho_graph_y_values_list.append(ortho_graph_y_values)
        if(i==1):
            ortho_graph_x_values= triangle_x_coordinates_list[i] 
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_x_values=(((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])**2)*Orthocenter_x+(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])*(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])*Orthocenter_y-(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])*(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i+1])*triangle_x_coordinates_list[i-1]+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])*(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i+1])*triangle_y_coordinates_list[i-1])/((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])**2+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])**2)
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_y_values= triangle_y_coordinates_list[i] 
            ortho_graph_y_values_list.append(ortho_graph_y_values)
            ortho_graph_y_values=(((triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])**2)*Orthocenter_y+(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])*(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])*Orthocenter_x+(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i+1])*(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])*triangle_x_coordinates_list[i-1]-(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])*(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i+1])*triangle_y_coordinates_list[i-1])/((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i+1])**2+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i+1])**2)
            ortho_graph_y_values_list.append(ortho_graph_y_values)
        if(i==2):
            ortho_graph_x_values= triangle_x_coordinates_list[i] 
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_x_values=(((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])**2)*Orthocenter_x+(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])*(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])*Orthocenter_y-(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])*(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i-2])*triangle_x_coordinates_list[i-1]+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])*(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i-2])*triangle_y_coordinates_list[i-1])/((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])**2+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])**2)
            ortho_graph_x_values_list.append(ortho_graph_x_values)
            ortho_graph_y_values= triangle_y_coordinates_list[i] 
            ortho_graph_y_values_list.append(ortho_graph_y_values)
            ortho_graph_y_values=(((triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])**2)*Orthocenter_y+(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])*(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])*Orthocenter_x+(triangle_y_coordinates_list[i-1]+triangle_y_coordinates_list[i-2])*(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])*triangle_x_coordinates_list[i-1]-(triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])*(triangle_x_coordinates_list[i-1]+triangle_x_coordinates_list[i-2])*triangle_y_coordinates_list[i-1])/((triangle_x_coordinates_list[i-1]-triangle_x_coordinates_list[i-2])**2+(triangle_y_coordinates_list[i-1]-triangle_y_coordinates_list[i-2])**2)
            ortho_graph_y_values_list.append(ortho_graph_y_values)

def plot_Graph():
    Triangle()
    
    centroid_x, centroid_y = Centroid()
   
    circumcenter_x, circumcenter_y =Circumcenter()

    Orthocenter_x, Orthocenter_y = Orthocenter(centroid_x, centroid_y,circumcenter_x, circumcenter_y)

    get_ortho_graph_coordinates(Orthocenter_x, Orthocenter_y)
    ax.fill(ortho_graph_x_values_list, ortho_graph_y_values_list, color = 'none', edgecolor='black')


    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle='--')

    plt.gca().set_aspect('equal', adjustable='box')
    min_x = -10
    max_x = 16
    min_y = -10
    max_y = 16
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x, step=step))
    ax.set_yticks(np.arange(min_y, max_y, step=step))
    plt.show()

triangle_x_coordinates_list = []
triangle_y_coordinates_list = []
ortho_graph_x_values_list = []
ortho_graph_y_values_list = []

plot_Graph()