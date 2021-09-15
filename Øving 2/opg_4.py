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
xt = 3*cos(t)
#y(t) = ...
yt = 3*sin(t)
#a < t < b
a = 0
b = pi
#delta (massetetthet) = ...
d = 1


#--------------------------------
#Beregninger
f = d * sqrt((diff(xt, t))**2 + (diff(yt, t))**2)
m = integrate(f, (t, a, b))
x = 1/m*integrate(f*xt, (t, a, b))
y = 1/m*integrate(yt*f, (t, a, b))

print("m: {}".format(m))
print("x: {}".format(x))
print("y: {}".format(y))

print("Press enter to exit...")
input()