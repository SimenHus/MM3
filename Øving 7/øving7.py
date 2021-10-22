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
#a)
fxyz = x**2+y**2+z**2 #Integranden i a)
xlimsA = [-4, 3] #Grenser for x i oppgave a) OBS: Innerste integral
ylimsA = [-3, 3] #Grenser for y i oppgave a)
zlimsA = [-4, 3] #Grenser for z i oppgave a)

#c)
zlimsC = [0, x**2] #Grenser for z i oppgave c) OBS: Innerste integral
ylimsC = [0, x**2] #Grenser for y i oppgave c)
xlimsC = [0, 2] #Grenser for x i oppgave c)

arr1 = [(fxyz, xlimsA, ylimsA, zlimsA), (zlimsC, ylimsC, xlimsC)]

#Oppgave 2
#b)
integrandB = r+r**2*cos(theta) #Integranden i oppgave b)
zlim = [-2, 2] #Grensene til z
rlim = [0, 3] #Grensene til r
thetalimB = [0, 2*pi] #Grensene til theta

#c)
integrandC = rho**2*sin(theta) #Integranden i oppgave c)
rholim = [0, 1] #Grensene til rho
philim = [0, pi] #Grensene til phi
thetalimC = [0, pi] #Grensene til theta

arr2 = [(integrandB, zlim, rlim, thetalimB), (integrandC, rholim, philim, thetalimC)]

#Oppgave 3
#a)
zlim = [-r, r] #Grensene til z
rlim = [0, 1] #Grensene til r
thetalimA = [0, 2*pi] #Grensene til theta i a)
#b)
rholim = [0, 1/sin(phi)] #Grensene til rho
philim = [pi/4, 3*pi/4] #Grensene til phi
thetalimB = [0, pi/4] #Grensene til theta i b)

arr3 = [(r, zlim, rlim, thetalimA), (rho**2*sin(phi), rholim, philim, thetalimB)]

#Oppgave 4
#b)
rholim = [1, 3] #Grenser for rho
philim = [0, 2*pi] #Grenser for phi
thetalim = [0, pi] #Grenser for theta

arr4 = [(), (1, rholim, philim, thetalim)]

#Oppgave 5

ulik1 = [5, cos(phi)] #Ulikhet med cosinus. [Over brøkstrek, under brøkstrek]
ulik2 = [2, sin(phi)] #Ulikhet med sinus. [Over brøkstrek, under brøkstrek]
tetthet = 1 #Tetthet oppgitt i oppgaven

arr5 = [ulik1, ulik2, tetthet]

#Oppgave 6

G = [9, 9, 0] #Grunnflate med [+-x, +-y, z]
topp = [0, 0, 2] #Toppen av pyramiden

arr6 = [G, topp]

#Oppgave 7

ulik1 = [x**2 + y**2 + z**2, 4] #Første ulikhet. [Venstre side, høyre side]
ulik2 = [z, sqrt(x**2 + y**2)] #Andre ulikhet. [Venstre side, høyre side]
tetthet = 1 #Tetthet oppgitt i oppgaven

arr7 = [ulik1, ulik2, tetthet]

#-------------------------------------

#Oppgave 1


def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    a, b = myArr
    
    a1 = integrate(a[0], (x, a[1][0], a[1][1]), (y, a[2][0], a[2][1]), (z, a[3][0], a[3][1]))
    a2 = integrate(1, (x, a[1][0], a[1][1]), (y, a[2][0], a[2][1]), (z, a[3][0], a[3][1])) - a1
    a3 = integrate(1, (z, b[0][0], b[0][1]), (y, b[1][0], b[1][1]), (x, b[2][0], b[2][1]))

    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(a2))
    print("c) {}".format(a3))

#Oppgave 2
def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    b, c = myArr

    a1 = integrate(b[0], (z, b[1][0], b[1][1]), (r, b[2][0], b[2][1]), (theta, b[3][0], b[3][1]))
    a2 = integrate(c[0], (rho, c[1][0], c[1][1]), (phi, c[2][0], c[2][1]), (theta, c[3][0], c[3][1]))

    print("Resultater:")
    print("a) Svar: 0")
    print("b) Svar: {}".format(a1))
    print("c) Svar: {}".format(a2))

#Oppgave 3

def opg3(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    b, c = myArr

    a1 = integrate(b[0], (z, b[1][0], b[1][1]), (r, b[2][0], b[2][1]), (theta, b[3][0], b[3][1]))
    a2 = integrate(c[0], (rho, c[1][0], c[1][1]), (phi, c[2][0], c[2][1]), (theta, c[3][0], c[3][1]))

    print("Resultater:")
    print("a) Svar: {}".format(a1))
    print("b) Svar: {}".format(a2))

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    b, c = myArr
    a = symbols("a", real = True, positive = True)

    a1 = integrate(r, (r, 0, a), (theta, 0, pi/2), (z, -a, a))
    a2 = integrate(c[0], (rho, c[1][0], c[1][1]), (theta, c[2][0], c[2][1]), (phi, c[3][0], c[3][1]))
    a3 = integrate(rho**2*sin(phi), (rho, c[1][0], c[1][1]), (theta, c[2][0], c[2][1]), (phi, c[3][0], c[3][1]))

    print("Resultater:")
    print("a) Svar: {}".format(a1))
    print("b) Svar: {}".format(a2))
    print("c) Svar: {}".format(a3))

#Oppgave 5

def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    a, b, c = myArr

    grenser = [((r, 0, b[0])), ((theta, 0, 2*pi)), ((z, 0, [a[0]]))]
    a1 = integrate(c*r, grenser[0], grenser[1], grenser[2])
    a2 = integrate(c*r**2*cos(theta), grenser[0], grenser[1], grenser[2])/a1
    a3 = integrate(c*r**2*sin(theta), grenser[0], grenser[1], grenser[2])/a1
    a4 = integrate(c*r*z, grenser[0], grenser[1], grenser[2])/a1

    print("Resultater:")
    print("m = {}".format(a1))
    print("x-koordinat = {}".format(a2))
    print("y-koordinat = {}".format(a3))
    print("z-koordinat = {}".format(a4))

#Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    a, b = myArr

    punktFlateOvre = [a, [-a[0], a[1], a[2]], b]
    punktFlateNedre = [[a[0], -a[1], a[2]], [-a[0], -a[1], a[2]], b]
    vecsOvre = [np.subtract(punktFlateOvre[2], punktFlateOvre[i]) for i in range(2)]
    vecsNedre = [np.subtract(punktFlateNedre[2], punktFlateNedre[i]) for i in range(2)]
    normalOvre = np.cross(vecsOvre[0], vecsOvre[1])
    normalNedre = np.cross(vecsNedre[0], vecsNedre[1])
    flateOvre = solve(np.dot(np.subtract((x, y, z), punktFlateOvre[2]), normalOvre), y)
    flateNedre = solve(np.dot(np.subtract((x, y, z), punktFlateNedre[2]), normalNedre), y)

    a1 = flateOvre[0]
    b1 = flateNedre[0]

    a2 = nsimplify(Topunktsformel((-a[0], a[2]), (b[0], b[2]), x)).subs(y, z)
    b2 = nsimplify(Topunktsformel((a[0], a[2]), (b[0], b[2]), x)).subs(y, z)

    a3 = a[2]
    b3 = b[2]

    print("Resultater:")
    print("a1(x, z) = {}".format(a1))
    print("b1(x, z) = {}".format(b1))
    print("a2(z) = {}".format(a2))
    print("b2(z) = {}".format(b2))
    print("a3 = {}".format(a3))
    print("b3 = {}".format(b3))

#Oppgave 7

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    a, b, c = myArr

    grenser = [((rho, 0, sqrt(a[1]))), ((phi, 0, pi/4)), ((theta, 0, 2*pi))]
    a1 = integrate(c*rho**2*sin(phi), grenser[0], grenser[1], grenser[2])
    a2 = integrate(rho*sin(phi)*cos(theta)*c*rho**2*sin(phi), grenser[0], grenser[1], grenser[2])/a1
    a3 = integrate(rho*sin(phi)*sin(theta)*c*rho**2*sin(phi), grenser[0], grenser[1], grenser[2])/a1
    a4 = integrate(rho*cos(phi)*c*rho**2*sin(phi), grenser[0], grenser[1], grenser[2])/a1

    print("Resultater:")
    print("m = {}".format(a1))
    print("x-koordinat = {}".format(a2))
    print("y-koordinat = {}".format(a3))
    print("z-koordinat = {}".format(a4))

#-----------------------------------

#Funksjoner

def Topunktsformel(p1, p2, var = y):
    x1, y1 = p1
    x2, y2 = p2
    return solve(y-y1 - (y2-y1)/(x2-x1)*(x-x1), var)[0]

if __name__ == '__main__':
    opg1(arr1)
    opg2(arr2)
    opg3(arr3)
    opg4(arr4)
    opg5(arr5)
    opg6(arr6)
    opg7(arr7)

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

