import matplotlib.pyplot as plt
import numpy as np
import string

fig, ax = plt.subplots()     #Only one subplot
start_num = -25
end_num = 0
step = 0.5
name = []
x = (np.arange(start_num, end_num+step, step=step))
y_1 = 3*x+12
y_2 = 5*x+36

for i, xy in enumerate(zip(x, y_1)):
    if y_1[i] == y_2[i]:
        ax.annotate(text = f'{"P"} {xy}', xy = xy, textcoords='offset points', xytext=(10, 2))

plt.plot(x, y_1)
plt.plot(x, y_2)


plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle='--')
plt.plot(x,y_1)

plt.gca().set_aspect('equal')
min_x = start_num - 20
max_x = end_num + 20
min_y = 5*start_num+36
max_y = 5*end_num+36
step = 5    #0.5
ax.set_xticks(np.arange(min_x, max_x+step, step=step))
ax.set_yticks(np.arange(min_y, max_y+step, step=step))

plt.show()