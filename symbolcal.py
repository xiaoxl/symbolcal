from __future__ import division
from sympy import *

from sympy.plotting import plot

# from sympy.abc import x

x,y,z,t=symbols('x y z t')

expr=(1/(1-x))**3


m=10

f=fps(expr,x).truncate(m+1)
g=diff(expr,x,m)
numb=g.evalf(subs={x:0})/factorial(m)


print(f)
print(numb)

# x = symbols('x')
# plot(sqrt(x^2+x^3),x,0,2)
#
