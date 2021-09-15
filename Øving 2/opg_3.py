import numpy as np
from sympy import *

t = symbols('t')

#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
#sin(t) skrives sin(t)
#pi skrives pi

#ENDRE DINE VERDIER HER
#x(t) = ...
xt = 3*sin(t)
#y(t) = ...
yt = 3*cos(t)
#z(t) = ...
zt = 2*t
#a < t < b
a = 0
b = 4

#---------------------------------
#Beregninger
#Integrand = vlen
v = np.array([diff(xt, t), diff(yt, t), diff(zt, t)])
vlen = sqrt(simplify(v[0]**2 + v[1]**2 + v[2]**2))
L = integrate(vlen, (t, a, b))

print("Integrand f(t): {}".format(vlen))
print("L: {}".format(L))

print("Press enter to exit...")
input()