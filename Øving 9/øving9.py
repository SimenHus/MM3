from sympy import *
import numpy as np


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

#Sett inn dine tall under her:

#Oppgave 1

likn = [2*x + 4*y + 2*z, 4] #Likning for plan [Venstre side, høyre side]
vektorfelt = [24*y - 16*x, #Vektorfelt F
              8*x - 12*y,
              20]

arr1 = [likn, vektorfelt]

#Oppgave 2

radius = 2 #Radius r
hoyde = 6 #Høyden h. Er også maksimal verdi for z
vektorfelt = [x + 7, #Vektorfelt F
              y + 7,
              z]

arr2 = [radius, hoyde, vektorfelt]

#Oppgave 3

radius = 2 #Radius til kulen

arr3 = radius

#Oppgave 4

abc = [5, 3, 7] #Planene x = a, y = b og z = c

arr4 = abc

#Oppgave 5
#Alle svar her er det samme :)

#Oppgave 6
vektorfelt = [2*x, -2*y] #Vektorfeltet F. Merk at du ikke trenger å skrive 1/sqrt(x**2 + y**2)

arr6 = vektorfelt

#Oppgave 7

vektorfelt = [x**3*y**4, #Vektorfelt F
              x**3*z**4,
              x**3*(z**4 + y**4)]

arr7 = vektorfelt
#-------------------------------------

#Oppgave 1

def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    plan, F = myArr
    fxy = solve(plan[0] - plan[1], z)[0]
    N = [-k for k in Grad(fxy)] + [1]
    xakse = solve(fxy - z, x)[0].subs({y: 0, z: 0})
    yakse = solve(fxy - z, y)[0].subs({x: 0, z: 0})
    areal = xakse*yakse/2
    fluks = F[2]*areal
    fluks2 = integrate(np.dot(F, N), (x, 0, 2), (y, 0, 1))
    print(fluks2)
    print("Resultater:")
    print("z = f(x, y) = {}".format(fxy))
    print("dS = {}".format(N))
    print("Planet skjærer x-aksen i x = {}".format(xakse))
    print("Planet skjærer y-aksen i y = {}".format(yakse))
    print("Areal til trekant A = {}".format(areal))
    print("Fluks = {}".format(fluks))

#Oppgave 2

def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    u, v = symbols("u v")
    rad, h, F = myArr
    side = (rad*cos(theta), rad*sin(theta))
    Nside = [simplify(k/absV(side)) for k in side] + [0]
    fluksTopp = pi*rad**2*+F[2].subs(z, h)
    fluksBunn = pi*rad**2*-F[2].subs(z, 0)
    integrand = np.dot(F, Nside).subs({x: rad*cos(theta), y: rad*sin(theta)})
    fluksSide = integrate(integrand*rad, (z, 0, h), (theta, 0, 2*pi))

    print("Resultater:")
    print("N1 = [0, 0, 1]")
    print("N2 = [0, 0, -1]")
    print("N3 = {}".format(Nside))
    print("Fluks topp = {}".format(fluksTopp))
    print("Fluks bunn = {}".format(fluksBunn))
    print("Fluks side = {}".format(fluksSide))

#Oppgave 3

def opg3(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    rad = myArr
    koords = (x, y, z)
    N = [k/rad for k in koords]

    print("Resultater:")
    print("Enhetsnormalvektor N = {}".format(N))
    print("Fluks = 0")

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    abc = myArr

    fluksTot = np.prod(abc)*3

    print("Resultater:")
    print("Fluks = {}".format(fluksTot))


#Oppgave 5

def opg5():
    print("\n\n\n\n\n\n\n\nOppgave 5:")

    print("Resultater:")
    print("N = -[cos(t), sin(t)]")
    print("Fluks = 0")

#Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    F = np.array(myArr)/(sqrt(x**2 + y**2))

    div = simplify(diff(F[0], x) + diff(F[1], y))
    curl = simplify(diff(F[1], x) - diff(F[0], y))
    print("Resultater:")
    print("Divergens = {}".format(div))
    print("Curl = {}".format(curl))

#Oppgave 7

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    F = myArr
    vars = (x, y, z)
    div = simplify(sum([diff(F[i], vars[i]) for i in range(len(F))]))
    curl = Curl(F)
    print("Resultater:")
    print("Divergens = {}".format(div))
    print("Curl = {}".format(curl))


#-----------------------------------

#Funksjoner

def Curl(F):
    F1 = simplify(diff(F[2], y) - diff(F[1], z))
    F2 = simplify(diff(F[0], z) - diff(F[2], x))
    F3 = simplify(diff(F[1], x) - diff(F[0], y))
    return [F1, F2, F3]

def Grad(func, vars = (x, y)):
    gradient = [diff(func, k) for k in vars]
    return gradient

def absV(vec):
    value = 0
    for x in vec: value += (x**2)
    return sqrt(value)

if __name__ == '__main__':
    opg1(arr1)
    opg2(arr2)
    opg3(arr3)
    opg4(arr4)
    opg5()
    opg6(arr6)
    opg7(arr7)

    print("Press enter to exit...")
    #input()


#Funksjonsformat

def opgx(myArr):
    print("\n\n\n\n\n\n\n\nOppgave x:")
    a, b, c = myArr

    print("Resultater:")
    print("a)")
    print("b)")
    print("c)")

