import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

arr_3d = [
    [[0, 1, 2], [3, 4, 5], [6, 7, 8]],
    [[9, 10, 11], [12, 13, 14], [15, 16, 17]],
    [[18, 19, 20], [21, 22, 23], [24, 25, 26]]
]

xs = []
ys = []
zs = []


for i in range(3):
    for j in range (3):
        for k in range (3):
            xs.append(i)
            ys.append(j)
            zs.append(k)
            #ax.text(i, j, k, arr_3d[i][j][k])
            ax.text(i, j, k, f'{arr_3d[i][j][k]} ({i}, {j}, {k})')

print(xs)
print(ys)
print(zs)

#Plot scatter
ax.scatter(xs, ys, zs)

# Add label for axes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#for xyz in enumerate(zip(xs,ys,zs)):
    #ax.annotate(text=f'{xyz}', xyz = xyz, textcoords='offset points', xytext=(10, 2))

#Display the plot
plt.show()
