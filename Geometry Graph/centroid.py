import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

def centroid(P_x, P_y, Q_x, Q_y,R_x, R_y):
    point_P =[P_x, P_y]
    point_Q =[Q_x, Q_y]
    point_R =[R_x, R_y]

    centroid_x = round((P_x+Q_x+R_x)/3,2)
    centroid_y = round((P_y+Q_y+R_y)/3,2)

    mid_PQ= [(P_x+Q_x)/2,(P_y+Q_y)/2]
    mid_QR= [(Q_x+R_x)/2,(Q_y+R_y)/2]
    mid_RP= [(R_x+P_x)/2,(R_y+P_y)/2]
    
    Triangle_x_values =[point_P[0],point_Q[0],point_R[0],point_P[0]]
    Triangle_y_values =[point_P[1],point_Q[1],point_R[1],point_P[1]]

    P_median_x_values =[point_P[0],mid_QR[0]]
    P_median_y_values =[point_P[1],mid_QR[1]]

    Q_median_x_values =[point_Q[0],mid_RP[0]]
    Q_median_y_values =[point_Q[1],mid_RP[1]]

    R_median_x_values =[point_R[0],mid_PQ[0]]
    R_median_y_values =[point_R[1],mid_PQ[1]]

    names = ['P', 'Q', 'R']
    for i, xy in enumerate(zip(Triangle_x_values, Triangle_y_values)):
        if i != len(Triangle_x_values)-1:
            ax.annotate(f'{names[i]} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))

    plt.scatter(centroid_x, centroid_y)
    xy= (centroid_x, centroid_y)
    ax.annotate(f'{"C"} {xy}', xy = xy, textcoords='offset points', xytext=(5, -5))
    
    plt.plot(Triangle_x_values,Triangle_y_values)
    plt.plot(P_median_x_values,P_median_y_values)
    plt.plot(Q_median_x_values,Q_median_y_values)
    plt.plot(R_median_x_values,R_median_y_values)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(linestyle='--')

    plt.gca().set_aspect('equal', adjustable='box')
    min_x = -10
    max_x = 11
    min_y = -10
    max_y = 11
    step = 1    #0.5
    ax.set_xticks(np.arange(min_x, max_x, step=step))
    ax.set_yticks(np.arange(min_y, max_y, step=step))
    plt.show()


P_x =float(input('x-coordinate of P: '))
P_y =float(input('y-coordinate of P: '))
Q_x =float(input('x-coordinate of Q: '))
Q_y =float(input('y-coordinate of Q: '))
R_x =float(input('x-coordinate of R: '))
R_y =float(input('y-coordinate of R: '))

centroid(P_x, P_y, Q_x, Q_y,R_x, R_y)
