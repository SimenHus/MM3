import numpy as np
from sympy import *

t, s = symbols('t s')
opgAntall = 7

#---------------------------------
#ENDRE DINE VERDIER HER

#Oppgave 1
#x(t) = ...
xt = 2*t + 0.5
#y(t) = ...
yt = 4*t - 2
#a < t < b
a = 0
b = 1

opg1Info = [xt, yt, a, b]

#Oppgave 2
#x(t) = ...
xt = 4*t**2 + 2
#y(t) = ...
yt = 3*t**3 + 5
#a < t < b
a = 0
b = 3

opg2Info = [xt, yt, a, b]

#Opggave 3
#x(t) = ...
xt = 3*sin(t)
#y(t) = ...
yt = 3*cos(t)
#z(t) = ...
zt = 2*t
#a < t < b
a = 0
b = 4
opg3Info = [xt, yt, zt, a, b]

#Oppgave 4
#x(t) = ...
xt = 3*cos(t)
#y(t) = ...
yt = 3*sin(t)
#a < t < b
a = 0
b = pi
#delta (massetetthet) = ...
d = 1

opg4Info = [xt, yt, a, b, d]

#Oppgave 5 er litt spesiell, så måtte endre noe
t = symbols('t', positive = True, real = True)
#Opggave 5
#r(t) = [x, y, z]
rt = np.array([t**3, 9*t**2, 9*t**2])
#t>a
a = 0

opg5Info = [rt, a]

#Endrer tilbake
t = symbols('t')
#Oppgave 6
v = np.array([2, -3, 0]) #Hastighetsvektor
a = np.array([0, 3, 3]) #Akselerasjonsvektor
r = np.array([1, 0, 1]) #Rykk vektor
opg6Info = [v, a, r]

#Oppgave 7
#rt =np.array([x, y, z])
rt = np.array([t**2/2, 1/3*(sqrt(2*t+1))**3, 0])
#s(t) = ...
st = t**2/2 + t
#t(s) = ...
ts = sqrt(2*s+1) - 1
opg7Info = [rt, st, ts]



#----------------------- Funksjoner ---------------------


#Returnerer enhetstangentvektor, gitt hastighetsvektor v
def TVec(v):
    vlen = absV(v)
    T = np.array([x/vlen for x in v])
    return T

#Returnerer enhetsnormalvektor, gitt hastighetsvektor v og akselerasjonsvektor a
def NVec(v, a):
    aXv = np.cross(a, v)
    aXvlen = absV(aXv)
    vlen = absV(v)
    return (np.cross(v, aXv))/(vlen*aXvlen)

#Returnerer den deriverte av en vektor, gitt vektor vec parameter d
def diffV(vec, d):
    return np.array([diff(x, d) for x in vec])

#Returnerer lengden av en vektor, gitt vector vec
def absV(vec):
    value = 0
    for x in vec: value += (x**2)
    return simplify(sqrt(value))

#Returnerer krumningen, gitt hastighetsvektor v og akselerasjonsvektor a
def Krumning(v, a):
    vlen = absV(v)
    aXv = np.cross(a, v)
    aXvlen = absV(aXv)
    return aXvlen/vlen**3

#Returnerer torsjonen, gitt hastighetsvektor v, akselerasjonsvektor a og rykkvektor r
def Torsjon(v, a, r):
    vXa = np.cross(v, a)
    vXalen = absV(vXa)
    return np.dot(vXa, r)/vXalen**2



#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
#sin(t) skrives sin(t)
#pi skrives pi

#----------------------- Oppgave 1 ---------------------
def opg1(myArr):
    print("Oppgave 1:")
    t = symbols('t')
    xt, yt, a, b = myArr
    #---------------------------------
    #Beregninger
    r = [xt, yt]
    v = diffV(r, t)
    vlen = sqrt(v[0]**2 + v[1]**2)
    L = integrate(vlen, (t, a, b))

    print("L: {}".format(L))



#----------------------- Oppgave 2 ---------------------


def opg2(myArr):
    print("\n\nOppgave 2:")
    t = symbols('t')

    xt, yt, a, b = myArr

    #---------------------------------
    #Beregninger
    #Integrand = vlen
    r = [xt, yt]
    v = diffV(r, t)
    vlen = absV(v)
    L = integrate(vlen, (t, a, b))

    print("Integrand f(t): {}".format(vlen))
    print("L: {}".format(L))


#----------------------- Oppgave 3 ---------------------

def opg3(myArr):
    print("\n\nOppgave 3:")
    t = symbols('t')

    xt, yt, zt, a, b = myArr

    #---------------------------------
    #Beregninger
    #Integrand = vlen
    r = [xt, yt, zt]
    v = diffV(r, t)
    vlen = absV(v)
    L = integrate(vlen, (t, a, b))

    print("Integrand f(t): {}".format(vlen))
    print("L: {}".format(L))
#----------------------- Oppgave 4 ---------------------

def opg4(myArr):
    print("\n\nOppgave 4:")
    t = symbols('t')

    xt, yt, a, b, d = myArr

    #--------------------------------
    #Beregninger
    f = d * sqrt((diff(xt, t))**2 + (diff(yt, t))**2)
    m = integrate(f, (t, a, b))
    x = 1/m*integrate(f*xt, (t, a, b))
    y = 1/m*integrate(yt*f, (t, a, b))

    print("m: {}".format(m))
    print("x: {}".format(x))
    print("y: {}".format(y))

#----------------------- Oppgave 5 ---------------------
def opg5(myArr):
    print("\n\nOppgave 5:")
    s, t, tau = symbols('s t tau', positive = True, real = True)
    rt, a = myArr

    #--------------------------------
    #Beregninger
    v = diffV(rt, t)
    vlen = absV(v)
    st = powsimp(integrate(vlen, (t, a, tau)))
    ts = solve(st - s, tau, rational = False, force = True)

    ts_ans = sqrt(factor(ts[0]**2))

    print("s(t) = {}".format(st))
    print("t(s) = {}".format(ts_ans))
    print("""Det kan være at t(s) ikke gir riktig svar.
    Dette kan sannsynligvis løses ved bruk av første kvadratsetning på uttrykket inne i parantesen.
    For eksempel sqrt((s**2 + 864*sqrt(2)*s + 373248)**(1/3) - 72) ga meg feil svar,
    men jeg fikk riktig ved å bruke første kvadratsetning på (s**2 + 864*sqrt(2)*s + 373248).
    Da ble svaret sqrt((s+373248^(1/2))^(2/3)-72) som var riktig""")
#----------------------- Oppgave 6 ---------------------

def opg6(myArr):
    print("\n\nOppgave 6:")

    v, a, r = myArr
    #------------------------------------------------------------------
    #Mellomregninger
    vlen = absV(v)
    aXv = np.cross(a, v)
    vXa = np.cross(v, a)
    aXvlen = absV(aXv)


    #Ønskede verdier
    T = TVec(v)
    N = NVec(v, a)
    K = Krumning(v, a)
    t = Torsjon(v, a, r)

    #Printer dem fint :)
    print("T: {}".format(T))
    print("N: {}".format(N))
    print("K: {}".format(K))
    print("t: {}".format(t))
#----------------------- Oppgave 7 ---------------------

def opg7(myArr):
    print("\n\nOppgave 7:")
    s_value = 12
    t, s = symbols('t s')

    rt, st, ts = myArr

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

    vlen = absV(vsubArr)
    aXvlen = absV(aXvsubArr)
    punkt = subValue(rt, t, ts_value)
    T = TVec(vsubArr)

    K = aXvlen/vlen**3
    Kr = 1/K

    #KRUMNINGSRADIUS TBC

    #Printer verdier
    print("Punkt på kurven: {}".format(punkt))
    print("T: {}".format(T))
    print("K: {}".format(K))
    print("Kr: {}".format(Kr))

opg1(opg1Info)
opg2(opg2Info)
opg3(opg3Info)
opg4(opg4Info)
opg5(opg5Info)
opg6(opg6Info)
opg7(opg7Info)


print("\n\nPress enter to exit...")
input()