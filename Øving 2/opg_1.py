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
xt = 2*t + 0.5
#y(t) = ...
yt = 4*t - 2
#a < t < b
a = 0
b = 1

#---------------------------------
#Beregninger

v = np.array([diff(xt, t), diff(yt, t)])
vlen = sqrt(v[0]**2 + v[1]**2)
L = integrate(vlen, (t, a, b))

print("L: {}".format(L))

print("Press enter to exit...")
input()