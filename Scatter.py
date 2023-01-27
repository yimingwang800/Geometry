import matplotlib.pyplot as plt
import numpy as np

def basic():
    # Define plot
    fig, ax = plt.subplots()     #Only one subplot
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [1, 2, 3, 4, 5, 6, 7]   # y = 2x +2
    plt.scatter(x, y)           # Plot the sine of each x point

    names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    # i = 0
    # for xy in zip(x, y):
    #     #ax.annotate(text=names[i], xy = xy)     #xy = (1, 1) | (2, 2) | etc.
    #     #ax.annotate(text=f'{names[i]} {xy}', xy = xy)
    #     ax.annotate(text=f'{names[i]} {xy}', xy = xy,
    #                 textcoords='offset points', xytext=(10, 2))
    #     i = i + 1

    for i, xy in enumerate(zip(x,y)):
        ax.annotate(text=f'{names[i]} {xy}', xy = xy, textcoords='offset points', xytext=(10, 2))
    
    # Format plot, add label for axes
    plt.title('Scatter')
    plt.xlabel('x')
    plt.ylabel('y')

    #Format plot, add grid
    #plt.grid(linestyle='-')    #Solide line
    plt.grid(linestyle='--')    # Dash line

    #Format plot, set aspect ration
    plt.gca().set_aspect('equal')

    # Define canvas and ticks
    min_x = 0
    max_x = 8
    min_y = 0
    max_y = 8
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x+step, step=step))
    ax.set_yticks(np.arange(min_y, max_y+step, step=step))

    plt.show()

basic()