from numpy import array, cross, dot
from sympy import \
    symbols, solve, simplify, nsimplify, diff, integrate, powsimp, sqrt, factor, sin, cos, pi

"""
Dette er matteprogrammet til simen h :)

# Nyttig info
    Kvadratrot skrives på formen: sqrt(...)
    Vanlig deling skrives på formen: x/y
    Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
    sin(t) skrives sin(t)
    pi skrives pi

"""

def oppg_1():
    t = symbols('t')

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
    v = array([diff(xt, t), diff(yt, t)])
    vlen = sqrt(v[0]**2 + v[1]**2)
    L = integrate(vlen, (t, a, b))

    print("L: {}".format(L))

    print("Press enter to exit...")
    input()

def oppg_2():
    t = symbols('t')

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
    v = array([diff(xt, t), diff(yt, t)])
    vlen = sqrt(v[0]**2 + v[1]**2)
    L = integrate(vlen, (t, a, b))

    print("Integrand f(t): {}".format(vlen))
    print("L: {}".format(L))

    print("Press enter to exit...")
    input()

def oppg_3():
    t = symbols('t')

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
    v = array([diff(xt, t), diff(yt, t), diff(zt, t)])
    vlen = sqrt(simplify(v[0]**2 + v[1]**2 + v[2]**2))
    L = integrate(vlen, (t, a, b))

    print("Integrand f(t): {}".format(vlen))
    print("L: {}".format(L))

    print("Press enter to exit...")
    input()

def oppg_4():
    t = symbols('t')

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

def oppg_5():
    s, t, tau = symbols('s t tau', positive = True, real = True)

    #ENDRE DINE VERDIER HER
    #r(t) = [x, y, z]
    rt = array([tau**3, 9*tau**2, 9*tau**2])
    #t>a
    a = 0

    #--------------------------------
    #Beregninger
    v = array([diff(x, tau) for x in rt])
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

def oppg_6():

    #ENDRE DINE VERDIER HER
    v = array([2, -3, 0]) #Hastighetsvektor
    a = array([0, 3, 3]) #Akselerasjonsvektor
    r = array([1, 0, 1]) #Rykk vektor


    #------------------------------------------------------------------
    #Mellomregninger
    vlen = sqrt(v[0]**2 + v[1]**2 + v[2]**2)
    aXv = cross(a, v)
    vXa = cross(v, a)
    aXvlen = sqrt(aXv[0]**2 + aXv[1]**2 + aXv[2]**2)


    #Ønskede verdier
    T = v/vlen
    N = (cross(v, aXv))/(vlen*aXvlen)
    K = aXvlen/(vlen**3)
    t = (dot(vXa, r))/(aXvlen**2)

    #Printer dem fint :)
    print("T: {}".format(T))
    print("N: {}".format(N))
    print("K: {}".format(K))
    print("t: {}".format(t))

    print("Press enter to exit...")
    input()

def oppg_7():
    s_value = 12
    t, s = symbols('t s')

    #ENDRE TIL DINE VERDIER HER
    #rt =array([x, y, z])
    rt = array([t**2/2, 1/3*(sqrt(2*t+1))**3, 0])
    #s(t) = ...
    st = t**2/2 + t # denne variabelen brukes ikke...
    #t(s) = ...
    ts = sqrt(2*s+1) - 1

    #------------------------------------------------------------------
    #Funksjoner
    def subValue(myArr, symVar, symValue, divFactor = 1):
        returnArr = []
        for x in myArr:
            if isinstance(x, int):
                returnArr.append(x/divFactor)
                continue
            returnArr.append(x.subs(symVar, symValue)/divFactor)
        returnArr = [nsimplify(y) for y in returnArr]
        return returnArr

    #------------------------------------------------------------------
    #Beregninger
    ts_value = ts.subs(s, s_value)
    v = array([diff(x, t) for x in rt])
    vsubArr = subValue(v, t, ts_value)
    a = array([diff(x, t) for x in v])
    asubArr = subValue(a, t, ts_value) # denne variabelen brukes ikke
    aXv = cross(a, v)
    aXvsubArr = subValue(aXv, t, ts_value)

    vlen = sqrt(vsubArr[0]**2 + vsubArr[1]**2 + vsubArr[2]**2)
    aXvlen = sqrt(aXvsubArr[0]**2 + aXvsubArr[1]**2 + aXvsubArr[2]**2)
    punkt = subValue(rt, t, ts_value)
    T = array([x/vlen for x in vsubArr])

    K = aXvlen/vlen**3
    Kr = 1/K

    #KRUMNINGSRADIUS TBC

    #Printer verdier
    print("Punkt på kurven: {}".format(punkt))
    print("T: {}".format(T))
    print("K: {}".format(K))
    print("Kr: {}".format(Kr))

    print("Press enter to exit...")
    input()

if __name__ == '__main__':
    # Kjør alle oppgavene
    oppgaver = ( oppg_1
               , oppg_2
               , oppg_3
               , oppg_4
               , oppg_5
               , oppg_6
               , oppg_7 )
    for oppgave in oppgaver:
        oppgave()
