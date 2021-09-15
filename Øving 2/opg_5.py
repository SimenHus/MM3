import numpy as np
from sympy import *

s, t, tau = symbols('s t tau', positive = True, real = True)


#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
#sin(t) skrives sin(t)
#pi skrives pi


#ENDRE DINE VERDIER HER
#r(t) = [x, y, z]
rt = np.array([tau**3, 9*tau**2, 9*tau**2])
#t>a
a = 0


#--------------------------------
#Beregninger
v = np.array([diff(x, tau) for x in rt])
vlen = simplify(sqrt(v[0]**2 + v[1]**2 + v[2]**2))
st = powsimp(integrate(vlen, (tau, a, t)))
ts = solve(st - s, t, rational = False, force = True)

ts_ans = sqrt(factor(ts[0]**2))

print("s(t) = {}".format(st))
print("t(s) = {}".format(ts_ans))
print("""Det kan være at t(s) ikke gir riktig svar.
Dette kan sannsynligvis løses ved bruk av første kvadratsetning på uttrykket inne i parantesen.
For eksempel sqrt((s**2 + 864*sqrt(2)*s + 373248)**(1/3) - 72) ga meg feil svar,
men jeg fikk riktig ved å bruke første kvadratsetning på (s**2 + 864*sqrt(2)*s + 373248).
Da ble svaret sqrt((s+373248^(1/2))^(2/3)-72) som var riktig""")

print("Press enter to exit...")
input()