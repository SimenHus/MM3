import numpy as np
from sympy import *

s_value = 12
t, s = symbols('t s')

#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)

#ENDRE TIL DINE VERDIER HER
#rt =np.array([x, y, z])
rt = np.array([t**2/2, 1/3*(sqrt(2*t+1))**3, 0])
#s(t) = ...
st = t**2/2 + t
#t(s) = ...
ts = sqrt(2*s+1) - 1

#------------------------------------------------------------------
#Funksjoner

def subValue(myArr, symVar, symValue, divFactor = 1):
    returnArr = []
    for x in myArr:
        if type(x) == int:
            returnArr.append(x/divFactor)
            continue
        returnArr.append(x.subs(symVar, symValue)/divFactor)
    returnArr = [nsimplify(y) for y in returnArr]
    return returnArr


#------------------------------------------------------------------
#Beregninger
ts_value = ts.subs(s, s_value)
v = np.array([diff(x, t) for x in rt])
vsubArr = subValue(v, t, ts_value)
a = np.array([diff(x, t) for x in v])
asubArr = subValue(a, t, ts_value)
aXv = np.cross(a, v)
aXvsubArr = subValue(aXv, t, ts_value)

vlen = sqrt(vsubArr[0]**2 + vsubArr[1]**2 + vsubArr[2]**2)
aXvlen = sqrt(aXvsubArr[0]**2 + aXvsubArr[1]**2 + aXvsubArr[2]**2)
punkt = subValue(rt, t, ts_value)
T = np.array([x/vlen for x in vsubArr])

K = aXvlen/vlen**3

#KRUMNINGSRADIUS TBC

#Printer verdier
print("Punkt på kurven: {}".format(punkt))
print("T: {}".format(T))
print("K: {}".format(K))


print("Press enter to exit...")
input()