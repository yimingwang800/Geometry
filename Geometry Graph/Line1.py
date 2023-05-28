import matplotlib.pyplot as plt
import numpy as np
import string

# Define plot, for only one subplot
fig, ax = plt.subplots()

#Draw basic line
x = [8, 8, 4, 4, 8]
y = [8, 4, 4, 8, 8] 
plt.plot(x,y)

plt.xlabel('x')
plt.ylabel('y')
plt.grid(linestyle='--')

start_num = 0
end_num = 25
step = 0.5
name = []

for i in range(end_num+1):
    alphabet = string.ascii_uppercase[i]
    name.append(alphabet)
    #alphabet = alphabet[:-1]
    #alphabet = ''

for i, xy in enumerate(zip(x, y)):
    if i != len(x)-1:
        ax.annotate(f'{name[i]} {xy}', xy = xy, textcoords='offset points', xytext=(5, 2))

min_x = -10
max_x = 10
min_y = 0
max_y = 23
step = 1    #0.5
ax.set_xticks(np.arange(min_x, max_x+step, step=step))
ax.set_yticks(np.arange(min_y, max_y+step, step=step))
# for xy in enumerate(zip(np.round(x,2), np.round(y,2))):
#    ax.annotate(text=f'{name[i]} {xy}', xy = xy, textcoords='offset points', xytext=(10, 2))



plt.show()