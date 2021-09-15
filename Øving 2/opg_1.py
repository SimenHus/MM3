import numpy as np
import sympy as sp

t = sp.symbols('t')

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

v = np.array([sp.diff(xt, t), sp.diff(yt, t)])
vlen = sp.sqrt(v[0]**2 + v[1]**2)
L = sp.integrate(vlen, (t, a, b))

print("L: {}".format(L))