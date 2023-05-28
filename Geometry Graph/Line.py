import matplotlib.pyplot as plt
import numpy as np

# Define plot, for only one subplot
fig, ax = plt.subplots()

#Draw basic line
x = [8, 8, 4, 4, 8]
y = [8, 4, 4, 8, 8] 
plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle='--')

names = ['A', 'B', 'C', 'D']
for i, xy in enumerate(zip(x, y)):
    if i != len(x)-1:
        ax.annotate(f'{names[i]} {xy}', xy = xy, textcoords='offset points', xytext=(10, 2))

min_x = -10
max_x = 10
min_y = 0
max_y = 23
step = 1    #0.5
ax.set_xticks(np.arange(min_x, max_x+step, step=step))
ax.set_yticks(np.arange(min_y, max_y+step, step=step))



plt.show()