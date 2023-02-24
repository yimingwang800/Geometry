import matplotlib.pyplot as plt
import numpy as np
import string

fig, ax = plt.subplots()     #Only one subplot
start_num = -9
end_num = 7
step = 0.01
x = (np.arange(start_num, end_num+step, step=step))
y = x**2 + 2*x + 1 

plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle='--')
plt.plot(x,y)

plt.gca().set_aspect('equal')
min_x = start_num
max_x = end_num
min_y = 0
max_y = max_x**2 + 2*max_x + 1
step = 5    #0.5
ax.set_xticks(np.arange(min_x, max_x+step, step=step))
ax.set_yticks(np.arange(min_y, max_y+step, step=step))

plt.show()