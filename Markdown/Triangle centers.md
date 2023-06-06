Triangle $A(x_1,y_1)$, $B(x_2,y_2)$, $C(x_3,y_3)$

$\star$ Centroid $G(x,y) = G(\frac{x_1+x_2+x_3}{3},\frac{y_1+y_2+y_3}{3})$

$\star$ Circumcenter $C(x,y)$
1. find the slop of AC, which is: 
$\frac{y_3-y_1}{x_3-x_1}$
2. find the slop of the perpendicular bisectors of the line AC, which is:
$-\frac{x_3-x_1}{y_3-y_1}$
3. find the middle point of A and C, which is: $(\frac{x_3+x_1}{2},\frac{y_3+y_1}{2})$
4. find the line equation of the perpendicular bisectors of the line AC:
$y=-\frac{x_3-x_1}{y_3-y_1}x+b$
$\Rightarrow \frac{y_3+y_1}{2} = -\frac{x_3-x_1}{y_3-y_1}\frac{x_3+x_1}{2} +b$
$\Rightarrow b = \frac{(y_3-y_1)(y_3+y_1)+(x_3-x_1)(x_3+x_1)}{2(y_3-y_1)}$
so the line equation of the perpendicular bisectors of the line AC is:
$y=-\frac{x_3-x_1}{y_3-y_1}x+\frac{(y_3-y_1)(y_3+y_1)+(x_3-x_1)(x_3+x_1)}{2(y_3-y_1)}$   ---------(1)
5. similarly, the line equation of the perpendicular bisectors of the line BC is:
$y=-\frac{x_3-x_2}{y_3-y_2}x+\frac{(y_3-y_2)(y_3+y_2)+(x_3-x_2)(x_3+x_2)}{2(y_3-y_2)}$   ---------(2)
6. solve equations (1) and (2) to find the coordinates of the Circumcenter $C(x,y)$, which is: $ C = (\frac{(y_3-y_1)(y_3-y_2)(y_3+y_2)+(y_3-y_1)(x_3-x_2)(x_3+x_2)-(y_3-y_1)(y_3-y_2)(y_3+y_1)+(y_3-y_2)(x_3-x_1)(x_3+x_1)}{(y_3-y_1)(x_3-x_2)-(y_3-y_2)(x_3-x_1)},\frac{(y_3-y_1)^2(x_3-x_2)(y_3+y_1)+(y_3-y_1)(x_3-x_2)(x_3+x_1)(x_3-x_1)-(y_3-y_1)(y_3-y_2)(y_3+y_1)(x_3-x_1)-(x_3-x_1)^2(x_3+x_1)(y_3-y_2)}{2(y_3-y_1)[(x_3-x_2)(y_3-y_1)-(y_3-y_2)(x_3-x_1)]})$