import matplotlib.pyplot as plt
import numpy as np
import string

def basic():
    # Define plot
    fig, ax = plt.subplots()     #Only one subplot
    start_num = 0
    end_num = 25
    step = 0.5
    name = []
    x = (np.arange(start_num, end_num+step, step=step))
    y = 2*x+2
    plt.scatter(x, y)

    # names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k'] 

    
    for i in range(end_num+1):
        alphabet = string.ascii_uppercase[i]
        for j in range (end_num+1):
            alphabet += string.ascii_uppercase[j]
            name.append(alphabet)
            alphabet = alphabet[:-1]
        alphabet = ''
        
    for i, xy in enumerate(zip(np.round(x,2), np.round(y,2))):
        ax.annotate(text=f'{name[i]} {xy}', xy = xy, textcoords='offset points', xytext=(10, 2))

    # Format plot, add label for axes
    plt.title('Scatter')
    plt.xlabel('x')
    plt.ylabel('y')

    #Format plot, add grid
    plt.grid(linestyle='--')    # Dash line

    #Format plot, set aspect ration
    plt.gca().set_aspect('equal')

    # Define canvas and ticks
    min_x = start_num
    max_x = end_num
    min_y = 0
    max_y = 2*max_x+2
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x+step, step=step))
    ax.set_yticks(np.arange(min_y, max_y+step, step=step))

    plt.show()

basic()