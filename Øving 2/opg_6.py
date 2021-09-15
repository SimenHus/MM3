import numpy as np
import sympy as sp

#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
#sin(t) skrives sin(t)
#pi skrives pi

#ENDRE DINE VERDIER HER
v = np.array([2, -3, 0]) #Hastighetsvektor
a = np.array([0, 3, 3]) #Akselerasjonsvektor
r = np.array([1, 0, 1]) #Rykk vektor


#------------------------------------------------------------------
#Mellomregninger
vlen = sp.sqrt(v[0]**2 + v[1]**2 + v[2]**2)
aXv = np.cross(a, v)
vXa = np.cross(v, a)
aXvlen = sp.sqrt(aXv[0]**2 + aXv[1]**2 + aXv[2]**2)


#Ønskede verdier
T = v/vlen
N = (np.cross(v, aXv))/(vlen*aXvlen)
K = aXvlen/(vlen**3)
t = (np.dot(vXa, r))/(aXvlen**2)

#Printer dem fint :)
print("T: {}".format(T))
print("N: {}".format(N))
print("K: {}".format(K))
print("t: {}".format(t))



print("Press enter to exit...")
input()