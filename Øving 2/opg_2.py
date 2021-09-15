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
xt = 4*t**2 + 2
#y(t) = ...
yt = 3*t**3 + 5
#a < t < b
a = 0
b = 3

#---------------------------------
#Beregninger
#Integrand = vlen
v = np.array([diff(xt, t), diff(yt, t)])
vlen = sqrt(v[0]**2 + v[1]**2)
L = integrate(vlen, (t, a, b))

print("Integrand f(t): {}".format(vlen))
print("L: {}".format(L))

print("Press enter to exit...")
input()