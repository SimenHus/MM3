import numpy as np
from sympy import *
from sympy.geometry import Circle

x, y, z = symbols('x y z')
theta, phi = symbols('theta phi')
r, rho = symbols('r rho', real = True, positive = True)
print("MERK: Hvis svaret er zoo, oo eller lignende betyr det uendelig")
print("Du kan kopiere svarene direkte fra Python inn til øvingen :)")

#Nyttig info
#Kvadratrot skrives på formen: sqrt(...)
#Vanlig deling skrives på formen: x/y
#Eksponenter skrives på formen: x**y (2**2 = 2^2 = 4)
#sin(t) skrives sin(t)
#pi skrives pi
#e skrives E
#log = ln

#Legg til dine verdier her

#Oppgave 1
#Du får gjette :)

#Oppgave 2
koord1 = [15/4, 5*sqrt(3)/4, 5/2]
koord2 = [3**(3/2)/2, 3/2, 4]

arr2 = [(koord1), (koord2)]

#Oppgave 3
koord1 = [2, pi/6, pi/4]
koord2 = [7, pi/4, -3]

arr3 = [(koord1), (koord2)]

#Oppgave 4
#Sylinderkoordinater
a = cos(theta) + r
#Kulekoordinater
b = 1/rho**2
#Kartesiske koordinater
c = -z**2 + y + x

arr4 = [(a), (b), (c)]

#Oppgave 5
#Lenke for visualisering av objektene: https://www.geogebra.org/m/DRfuvhxR
#likning = (venstre side, høyre side)
l1 = (z**2 - 6*z + y**2 - 8*y + x**2 - 4*x + 29, 9)
l2 = (z**2 - 6*z + y**2 - 8*y + x**2 + 25, 9)

arr5 = [(l1, l2), ()]

#Oppgave 6

#a)
#f(x, y) = ...
fxy = (E**x + 1)/(E**y + 1)
#lim -> (x, y) = (..., ...)
limf = (0, 0)

#b)
#g(x, y) = ...
gTeller = x*y - y - 2*x + 2
gNevner = x**2 - 3*x +2
#lim -> (x, y) = (..., ...) 
limg = (1, 1)

#c)
#h(x, y) = ...
hTeller = x**2 - y**6
hNevner = x*y**3
#lim -> (x, y) = (..., ...)
limh = (0, 0)
#Substitusjon 1: (venstre side, høyre side)
sub1 = (x, y**3)
#Substitusjon 2: (venstre side, høyre side)
sub2 = (x, y)

arr6 = [(fxy, limf), (gTeller, gNevner, limg), (hTeller, hNevner, limh, sub1, sub2)]

#Oppgave 7

#a)
#f(x, y) = ...
fxy = sin(y**2 + y + x**2)

#b)
#punkt p = (x, y)
p = (1, 2)

#c)
#g(x, y) = ...
gxy = y**2 - 6*y + x**2 - 6*x + 21
arr7 = [(fxy), (p), (gxy)]


#Oppgave 8

#c)
#g(x, y) = ...
gxy = y*ln(y**2 + x**2)
arr8 = [(), (), (gxy)]

#---------------------------------------------------

#Oppgave 1
def opg1():
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    print("Generelt uttrykk for kule:")
    print("(z-z0)**2 + (y-y0)**2 + (x-x0)**2 = r**2")
        
    

#Oppgave 2

def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    r, theta, phi = symbols('r theta phi')
    a, b = myArr
    a = [nsimplify(x) for x in a]
    b = [nsimplify(x) for x in b]

    #a)

    a1 = list(cart2sphere(a[0], a[1], a[2]))
    lfa = "r**2 = x**2 + y**2 + z**2\nphi = arccos(z/sqrt(x**2 + y**2 + z**2))\ntan(theta) = y/x"

    #b)

    a2 = list(cart2syl(b[0], b[1], b[2]))
    
    lfb = "r**2 = x**2 + y**2\ntan(theta) = y/x\nz = z"

    print("Resultater:")
    print("a)\nr = {}\nphi = {}\ntheta = {}".format(a1[0], a1[1], a1[2]))
    print("b)\nr = {}\ntheta = {}\nz = {}".format(a2[0], a2[1], a2[2]))

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))

#Oppgave 3

def opg3(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    r, theta, phi = symbols('r theta phi')
    a, b = myArr
    a = [nsimplify(x) for x in a]
    b = [nsimplify(x) for x in b]

    #a)

    a1 = list(sphere2cart(a[0], a[1], a[2]))
    lfa = "x = rsin(phi)cos(theta)\ny = rsin(phi)sin(theta)\nz = rcos(phi)"

    #b)

    a2 = list(syl2cart(b[0], b[1], b[2]))
    
    lfb = "x = rcos(theta)\ny = rsin(theta)\nz = z"

    print("Resultater:")
    print("a)\nx = {}\ny = {}\nz = {}".format(a1[0], a1[1], a1[2]))
    print("b)\nx = {}\ny = {}\nz = {}".format(a2[0], a2[1], a2[2]))

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    a, b, c = myArr

    #a)
    
    a1cart = syl2cartExp(a)
    a1 = cart2sphereExp(a1cart)

    #b)

    a1cart = sphere2cartExp(b)
    a2 = cart2sylExp(a1cart)

    #c)

    a3 = cart2sylExp(c)


    lfa = "Gjør uttrykket om til et rent kartesisk uttrykk, deretter om til kulekoordinater"
    lfb = "Gjør uttrykket om til et rent kartesisk uttrykk, deretter om til sylinderkoordinater"
    lfc = "Gjør fra kartesisk til sylinderkoordinater"

    print("Resultater:")
    print("Hvis noen resultater ikke blir godkjent, kan det være at du kun trenger å faktorisere potensyttrykk")
    print("Hvis resultatet er helt på jordet kan du sende meg en melding så skal jeg se om jeg kan hjelpe :)")
    print("a) {}".format(a1))
    print("b) {}".format(a2))
    print("c) {}".format(a3))

    print("\nHvordan løse:")
    print("Alle oppgavene her løses ved bruk av en algoritme (algoritmene ligger på bunnen av scriptet) som bytter ut verdier (f.eks x = r*cos(theta) helt til uttrykket er på riktig form")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))
    print("c)\n{}".format(lfc))

#Oppgave 5

def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    a, b = myArr
    l1, l2 = a

    likn = l1[0] - l1[1] - (l2[0] - l2[1])
    freeSym = likn.free_symbols
    if x in freeSym: freeSym = x
    elif y in freeSym: freeSym = y
    elif z in freeSym: freeSym = z
    freeSymVal = solve(likn, freeSym)
    newEq = [l1[0].subs(freeSym, freeSymVal[0]), l1[1]]
    eqSyms = newEq[0].free_symbols
    if z in eqSyms and x not in eqSyms: newEq[0] = newEq[0].subs(z, x)
    if z in eqSyms and y not in eqSyms: newEq[0] = newEq[0].subs(z, y)
    r = Circle(newEq[0] - newEq[1]).radius

    lfa = """Finn kryssningen mellom planene ved å ta plan1 - plan2. Deretter får du en løsning for x/y/z.
Sett inn løsningen du får tilbake i et av planene ({} = {} inn i {} = {}). Da får du uttrykket for en sirkel.
Radiusen er kvadratroten av det konstante tallet.""".format(freeSym, freeSymVal[0], l1[0], l1[1])

    print("Resultater:")
    print("a) r = {}".format(r))

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))

#Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    a, b, c = myArr

    #a
    fxy, limf = a
    a1 = fxy.subs({x: limf[0], y: limf[1]})

    lfa = "Sett inn {} for x og {} for y".format(limf[0], limf[1])

    #b
    gT, gN, limg = b
    gxy = simplify(factor(gT)/factor(gN))
    b1 = gxy.subs({x: limg[0], y: limg[1]})

    lfb = "Faktoriserer {} til {}".format(gT/gN, gxy)

    #c
    hT, hN, limh, sub1, sub2 = c
    limUsed = limh[0] if sub1[0] == x else limh[1]
    exp1 = (hT/hN).subs(sub1[0], sub1[1])
    exp2 = (hT/hN).subs(sub2[0], sub2[1])
    c1 = limit(exp1, sub1[1], limUsed)
    c2 = limit(exp2, sub2[1], limUsed)

    lfc = "1: Sett inn {} for {}, og deretter {} for {} i {}\n2: Sett inn {} for {}, og deretter {} for {} i {}".format(
        sub1[1], sub1[0], limUsed, sub1[1], exp1,
        sub2[1], sub2[0], limUsed, sub2[1], exp2)
    
    #Skriv svar
    print("Resultat:")
    print("a) {}".format(a1))
    print("b) {}".format(b1))
    print("c)\nSubstitusjon 1: {}\nSubstitusjon 2: {}".format(c1, c2))

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))
    print("c)\n{}".format(lfc))


#Oppgave 7

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    a, b, c = myArr
    #a)
    fxy = a
    a1 = diff(fxy, x)
    a2 = diff(fxy, y)
    lfa = "1: Deriver {} mhp x. Bruk kjerneregel og betrakt y som en konstant\n2: Deriver {} mhp x. Bruk kjerneregel og betrakt y som en konstant".format(
        fxy, fxy)

    #b)
    p = b

    b1 = a1.subs({x: p[0], y: p[1]})
    b2 = a2.subs({x: p[0], y: p[1]})
    b3 = fxy.subs({x: p[0], y: p[1]})

    lfb = """a: Partiell deriver f(x, y) mhp på x, deretter sett inn {0} for x og {1} for y
b: Partiell deriver f(x, y) mhp på y, deretter sett inn {0} for x og {1} for y
c: c = z = f(x0, y0). Finner z ved å regne ut f({0}, {1})""".format(p[0], p[1])

    #c)
    gxy = c
    dgdx = diff(gxy, x)
    dgdy = diff(gxy, y)
    bxy = list(solveset(dgdx)) + list(solveset(dgdy))
    c1 = [bxy[0], bxy[1], gxy.subs({x: bxy[0], y: bxy[1]})]

    lfc = """Først vet vi at funksjonen har et globalt minimum, derfor trenger vi ikke undersøke om dette stemmer.
a: Partiell deriver g mhp x og sett lik null (dgdx = 0)
b: Partiell dervier g mhp y og sett lik null (dgdy = 0)
c: c = z = g(x, y) = g(a, b)"""

    #Skriv svar
    print("Resultater:")
    print("a)\ndfdx = {}\ndfdy = {}".format(a1, a2))
    print("b)\na = {}\nb = {}\nc = {}".format(b1, b2, b3))
    print("c) {}".format(c1))

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))
    print("c)\n{}".format(lfc))

def opg8(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 8:")
    a, b, c = myArr
    print("a) og b) kan dere bare gjette på :)")
    #c)
    g = c
    gxx = diff(diff(g, x), x)
    gxxyy = diff(diff(gxx, y), y)
    c1 = gxxyy

    lfc = "Partiell dervier g mhp x 2 ganger, deretter deriver resultatet mhp y to ganger. Bingo"

    print("Resultater:")
    print("c) {}".format(c1))

    print("\nHvordan løse:")
    print("c)\n{}".format(lfc))

#-------------------------
#Functions

def cart2sphere(x, y, z):
    r = sqrt(x**2 + y**2 + z**2)
    theta = atan2(y, x)
    phi = acos(z/sqrt(x**2 + y**2 + z**2))
    return r, phi, theta

def cart2syl(x, y, z):
    r = sqrt(x**2 + y**2)
    theta = atan2(y, x)
    z = z
    return r, theta, z 

def sphere2cart(rho, phi, theta):
    x = rho*sin(phi)*cos(theta)
    y = rho*sin(phi)*sin(theta)
    z = rho*cos(phi)
    return x, y, z

def syl2cart(r, theta, z):
    x = r*cos(theta)
    y = r*sin(theta)
    return x, y, z

def syl2sphere(r, theta, z):
    rho = sqrt(r**2 + z**2)
    phi = acos(z/sqrt(r**2 + z**2))
    return rho, phi, theta

def sphere2syl(rho, phi, theta):
    r = rho*sin(phi)
    z = rho*cos(phi)
    return r, theta, z

def cart2sylExp(myEq):
    cart2syl = [[x**2 + y**2, r**2],
                [x, r*cos(theta)],
                [y, r*sin(theta)],
                [y/x, tan(theta)]]
    newEq = myEq
    counter = 0
    stuckCounter = 0
    while checkType(newEq) != "syl":
        newEq = simplify(newEq.subs(cart2syl[counter][0], cart2syl[counter][1]))
        if counter +1 == len(cart2syl):
            counter = 0
        else:
            counter += 1
        stuckCounter += 1
        if stuckCounter == 30:
            print("Fant ikke sylinderkoordinater for det kartesiske uttrykket :(")
            break
    return newEq

def cart2sphereExp(myEq):
    cart2sphere = [[x**2 + y**2 + z**2, rho**2],
                [x, rho*sin(phi)*cos(theta)],
                [y, rho*sin(phi)*sin(theta)],
                [z, rho*cos(phi)],
                [y/x, tan(theta)]]
    newEq = myEq
    counter = 0
    stuckCounter = 0
    while checkType(newEq) != "sphere":
        newEq = simplify(newEq.subs(cart2sphere[counter][0], cart2sphere[counter][1]))
        if counter +1 == len(cart2sphere):
            counter = 0
        else:
            counter += 1
        stuckCounter += 1
        if stuckCounter == 30:
            print("Fant ikke kulekoordinater for det kartesiske uttrykket :(")
            break
    return newEq

def sphere2cartExp(myEq):
    sphere2cart = [[rho**2, x**2 + y**2 + z**2],
                [rho, sqrt(x**2 + y**2 + z**2)],
                [rho*cos(phi), z],
                [rho*cos(theta), x/sin(phi)],
                [rho*sin(theta), y/sin(phi)],
                [tan(theta), y/x]]
    newEq = myEq
    counter = 0
    stuckCounter = 0
    while checkType(newEq) != "cart":
        newEq = simplify(newEq.subs(sphere2cart[counter][0], sphere2cart[counter][1]))
        if counter +1 == len(sphere2cart):
            counter = 0
        else:
            counter += 1
        stuckCounter += 1
        if stuckCounter == 30:
            print("Fant ikke kartesisk uttrykk for kulekoordinatene :(")
            break
    return newEq

def syl2cartExp(myEq):
    syl2cart = [[r**2, x**2 + y**2],
                [r*cos(theta), x],
                [r*sin(theta), y],
                [tan(theta), x/y],
                [r, sqrt(x**2 + y**2)],
                [cos(theta), x/r],
                [sin(theta), y/r]]
    newEq = myEq
    counter = 0
    stuckCounter = 0
    while checkType(newEq) != "cart":
        newEq = simplify(newEq.subs(syl2cart[counter][0], syl2cart[counter][1]))
        if counter +1 == len(syl2cart):
            counter = 0
        else:
            counter += 1
        stuckCounter += 1
        if stuckCounter == 30:
            print("Fant ikke kartesisk uttrykk for sylinderkoordinatene :(")
            break
    return newEq

def checkType(myEq):
    syms = myEq.free_symbols
    if r not in syms and theta not in syms and rho not in syms and phi not in syms: return "cart"
    if x not in syms and y not in syms and rho not in syms and phi not in syms: return "syl"
    if x not in syms and y not in syms and z not in syms and r not in syms: return "sphere"


if __name__ == '__main__':
    opg1()
    opg2(arr2)
    opg3(arr3)
    opg4(arr4)
    opg5(arr5)
    opg6(arr6)
    opg7(arr7)
    opg8(arr8)

    print("Press enter to exit...")
    input()


#Funksjonsformat

def opgx(myArr):
    print("\n\n\n\n\n\n\n\nOppgave x:")
    a, b, c = myArr

    lfa = "løsning oppgave a"
    lfb = "løsning oppgave b"
    lfc = "løsning oppgave c"

    print("Resultater:")
    print("a)")
    print("b)")
    print("c)")

    print("\nHvordan løse:")
    print("a)\n{}".format(lfa))
    print("b)\n{}".format(lfb))
    print("c)\n{}".format(lfc))