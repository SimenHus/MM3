from sympy import *
import numpy as np


x, y, z, t = symbols('x y z t')
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

#Sett inn dine tall under her:

#Oppgave 1

limV = [1, 2] #Grensene til v
limU = [ln(3), ln(7)] #Grensene til u

arr1 = [limV, limU]

#Oppgave 2

fxyz = 1/(x**2+y**2+z**2)

arr2 = fxyz

#Oppgave 3

F = [6*x**2*y**3 + 4*x,
    6*x**3*y**2 + 2*y] #Vektorfelt F

arr3 = F

#Oppgave 4

F = [15*x, 8*x+y**2] #Vektorfelt F
radius = 3 #Radius til sirkel

arr4 = [F, radius]

#Oppgave 5

f = cos(4*y**2) + sin(4*x**2) #Potensialfunksjon
radius = 1 #Radius til sirkel C
arr5 = [f, radius]

#Oppgave 6
#Se teori for hjelp

#Oppgave 7

sphere = [x**2 + y**2 + z**2, 4] #Område S. [Venstre side, høyre side]

arr7 = sphere

#Oppgave 8

limz = [0, 2] #Grensene til z

arr8 = limz

#-------------------------------------

#Oppgave 1

def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    limV, limU = myArr
    u, v = symbols("u v")
    koords = [u, v]
    Guv = [v*E**u, v*E**(-u)]
    DG = []
    for j in Guv:
        tempMat = []
        for k in koords: tempMat.append(diff(j, k))
        DG.append(tempMat)
    a1 = DG[0][0]*DG[1][1]-DG[0][1]*DG[1][0]

    a2 = integrate(a1, (u, limU[0], limU[1]), (v, limV[0], limV[1]))
    print("Resultater:")
    print("Integrand g(u, v) = {}".format(a1))
    print("A = {}".format(a2))

#Oppgave 2

def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    f = myArr

    fx = simplify(diff(f, x))
    fy = simplify(diff(f, y))
    fz = simplify(diff(f, z))

    print("Resultater:")
    print("fx = {}".format(fx))
    print("fy = {}".format(fy))
    print("fz = {}".format(fz))

#Oppgave 3

def opg3(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    F = myArr

    rt = {x: t*x, y: t*y}

    f = integrate(np.dot([k.subs(rt) for k in F], (x, y)), (t, 0, 1))
    

    print("Resultater:")
    print("phi(x, y) = {}".format(f))

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    F, rad = myArr
    koords = (x, y)
    rt = {x: rad*cos(t), y: rad*sin(t)}
    vt = [diff(rt[k], t) for k in koords]
    f = integrate(np.dot([k.subs(rt) for k in F], vt), (t, 0, 2*pi))
    print("Resultater:")
    print("Sirkulasjon = {}".format(f))

#Oppgave 5

def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    f, rad = myArr
    
    a1 = f.subs({x: rad*cos(2*pi), y: rad*sin(2*pi)}) - f.subs({x: rad*cos(0), y: rad*sin(0)})
    a2 = f.subs({x: rad*cos(pi/2), y: rad*sin(pi/2)}) - f.subs({x: rad*cos(0), y: rad*sin(0)})

    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(-a2))

#Oppgave 6

def opg6():
    print("\n\n\n\n\n\n\n\nOppgave 6:")

    print("Resultater:")
    print("Står litt tips i teori, men du kan alltids bare gjette :)")

#Oppgave 7

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    S = myArr
    vars = (phi, theta)
    radius = nsimplify(sqrt(S[1]))
    rx = radius*sin(phi)*cos(theta)
    ry = radius*sin(phi)*sin(theta)
    rz = (solve(S[0]-S[1], z)[1])
    ruv = (rx, ry, rz.subs({x: rx, y: ry}))
    vu = [simplify(diff(k, vars[0])) for k in ruv]
    vv = [simplify(diff(k, vars[1])) for k in ruv]
    ruxrv = np.cross(vu, vv)
    dS = sqrt(simplify(absV(ruxrv)**2))
    limU = [0, pi/2]
    limV = [0, pi/2]
    a1 = integrate(rx*dS, (vars[0], limU[0], limU[1]), (vars[1], limV[0], limV[1]))
    a2 = integrate(ry*dS, (vars[0], limU[0], limU[1]), (vars[1], limV[0], limV[1]))


    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(a2))

#Oppgave 8

def opg8(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 8:")
    limZ = myArr
    vars = (r, theta)
    radius = nsimplify(limZ[1])
    rx = r*cos(theta)
    ry = r*sin(theta)
    rz = sqrt(x**2 + y**2).subs({x: rx, y: ry})
    ruv = (rx, ry, rz)
    vu = [simplify(diff(k, vars[0])) for k in ruv]
    vv = [simplify(diff(k, vars[1])) for k in ruv]
    ruxrv = np.cross(vu, vv)
    dS = sqrt(simplify(absV(ruxrv)**2))
    limU = [0, radius]
    limV = [0, 2*pi]
    a1 = integrate(rz**2*dS, (vars[0], limU[0], limU[1]), (vars[1], limV[0], limV[1]))
    print("Resultater:")
    print("Svar: {}".format(simplify(a1)))

#-----------------------------------

#Funksjoner

def absV(vec):
    value = 0
    for x in vec: value += (x**2)
    return sqrt(value)

if __name__ == '__main__':
    opg1(arr1)
    opg2(arr2)
    opg3(arr3)
    opg4(arr4)
    opg5(arr5)
    opg6()
    opg7(arr7)
    opg8(arr8)

    print("Press enter to exit...")
    input()


#Funksjonsformat

def opgx(myArr):
    print("\n\n\n\n\n\n\n\nOppgave x:")
    a, b, c = myArr

    print("Resultater:")
    print("a)")
    print("b)")
    print("c)")

