from operator import indexOf
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
#e skrives E eller exp()
#log = ln

#Sett inn dine tall under her:

#Oppgave 1
fxy = 3*sin(8*pi*y + 5*pi*x) #z = f(x, y) = ...
punkt = (1/30, 1/48) #Punkt = (x, y)

arr1 = [fxy, punkt]

#Oppgave 2
A = [ #Den oppgitte matrisen i oppgaveteksten
    [-13/3, -14/3], #a, b
    [14/3, 22/3] #c, d
    ]
areal = 100 #Arealet oppgitt i oppgaveteksten
B = [ #Oppgitt matrise B i oppgavetekst
    [-3, -5, -5], 
    [3, 5, 5],
    [-3, -3, -3]
    ]
volum = 10 #Volumet som blir oppgitt i oppgaven
detD = 11 #Determinanten til matrise D
arr2 = [(A, areal), (B), (volum, detD)]

#Oppgave 3
#Her kan du gjette eller se teoribiten

#Oppgave 4
#a)
fxy = -(y-3)**4+(x-6)**4+6 #z = f(x, y) = ...
#b)
gxy = sin(y**2 + x**2) #z = g(x, y) = ...
xgrenserB = [-1.5, 1.5] #a < x < b
ygrenserB = [-1.5, 1.5] #a < y < b
#c)
hxy = E**(-sqrt(1-y**2))+E**(-sqrt(1-x**2)) #z = h(x, y) = ...
xgrenserC = [0, 1] #a < x < b
ygrenserC = [0, 1] #a < x < b
arr4 = [fxy, (gxy, xgrenserB, ygrenserB), (hxy, xgrenserC, ygrenserC)]

#Oppgave 5
fxy = 2*y**2+4*y+2*x**2-16*x+38 #z = f(x, y)
gxyz = -z**2-8*z+2*y**2+2*y+2*x**2+14*x+7 #w = g(x, y, z)
arr5 = [fxy, gxyz]

#Oppgave 6
fxy = x**2 - 2*x*y + y**2 #z = f(x, y)
radius = 2 #Radius til sirkelen

arr6 = [fxy, radius]

#Oppgave 7
fxy = 4*y + 2*x #f(x, y)
radius = 8 #Oppgitt radius

arr7 = [fxy, radius]

#-------------------------------------

#Oppgave 1

def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    fxy, pos = myArr
    variabler = [x, y]

    gradientExp = [diff(fxy, k) for k in variabler]
    gradient = [nsimplify(k.subs({x: pos[0], y: pos[1]})) for k in gradientExp]
    linearisering = nsimplify(fxy.subs({x: pos[0], y: pos[1]}) + sum(
        [gradient[i]*(variabler[i] - pos[i]) for i in range(len(pos))]))
    a2 = nsimplify(simplify(linearisering))

    H = []
    for a in variabler:
        innerMatrix = []
        for b in variabler: innerMatrix.append(diff(diff(fxy, a), b))
        H.append(innerMatrix)

    mat1 = [(x-pos[0])/2, (y-pos[1])/2]
    mat2 = []
    mat3 = [[x - pos[0]], [y - pos[1]]]
    for a in H:
        newMat = []
        for b in a: newMat.append(b.subs({x: pos[0], y: pos[1]}))
        mat2.append(newMat)
    a4Matrix = np.matmul(np.matmul(mat1, mat2), mat3)
    a4 = nsimplify(simplify(factor(a4Matrix)))[0]
    print("Resultater:")
    print("a)\ndfdx = {}\ndfdy = {}".format(gradientExp[0], gradientExp[1]))
    print("b) z = {}".format(a2))
    print("c)")
    for i in range(len(H)):
        for j in range(len(H[0])): print("f{}{} = {}".format(i+1, j+1, H[i][j]))
    print("d) z = {}".format(a4))


def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    a, b, c = myArr

    #a)
    a1 = [nsimplify(k) for k in list(np.linalg.eig(a[0])[0])]
    a2 = nsimplify(np.linalg.det(a[0]))
    a3 = []
    for i in np.linalg.inv(a[0]):
        tempMat = []
        for j in i: tempMat.append(nsimplify(j))
        a3.append(tempMat)
    a4 = nsimplify(abs(a2)*a[1])

    #b)
    a5 = [round(k) for k in list(np.linalg.eig(b)[0])]
    a6 = nsimplify(np.linalg.det(b))

    #c)
    a7 = nsimplify(c[0]*abs(c[1]))
    print("Resultater:")
    print("a)\nEgenverdier: {}".format(a1))
    print("detA = {}".format(a2))
    print("A**-1 = matrix({}, {})".format(a3[0], a3[1]))
    print("Nytt areal: {}".format(a4))
    print("b)\nEgenverider: {}".format(a5))
    print("detB = {}".format(a6))
    print("Nytt Volum: {}".format(a7))

#Oppgave 3

def opg3():
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    print("Her må du bare gjette eller lese teoribiten :)")

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    a, b, c = myArr
    koords = (x, y)

    #a)
    gradient = Grad(a)
    kritisk = solve(gradient, koords)
    a1 = [kritisk[x], kritisk[y], a.subs(kritisk)]

    #c)

    hxy, limx, limy = c
    minmax = [hxy.subs({x: limx[i], y: limy[i]}) for i in range(len(limx))]
    a2 = [limx[minmax.index(max(minmax))], limy[minmax.index(max(minmax))], max(minmax)]


    print("Resultater:")
    print("a)\nKritisk punkt: [{}, {}, {}]".format(a1[0], a1[1], a1[2]))
    print("Se teoribiten for hvordan å finne hva slags type punkt det er snakk om (eller bare gjett :))")
    print("b)")
    print("Likning: x**2 + y**2 = pi/2 (Tok en kjapp løsning her, hvis det ikke funker se teoribiten)")
    print("c)")
    print("Kritisk punkt: [x, y, z] = [{}, {}, {}]".format(a2[0], a2[1], a2[2]))

#Oppgave 5
def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    a, b = myArr
    varsf = (x, y)
    varsg = (x, y, z)


    #a)
    gradf = Grad(a)
    Hf = [Grad(k) for k in gradf]
    HfInts = [[int(k) for k in Hf[i]] for i in range(len(Hf))]
    kritiskf = solve(gradf, varsf)
    a1 = [kritiskf[x], kritiskf[y]]
    a2 = CriticalPointClass(np.matrix(HfInts))

    #b)
    gradg = Grad(b, varsg)
    Hg = [Grad(k, varsg) for k in gradg]
    HgInts = [[int(k) for k in Hg[i]] for i in range(len(Hg))]
    kritiskg = solve(gradg, varsg)
    a3 = [kritiskg[x], kritiskg[y], kritiskg[z]]
    a4 = CriticalPointClass(np.matrix(HgInts))

    print("Resultater:")
    print("a)\nKritisk punkt til f i [x, y] = [{}, {}]".format(a1[0], a1[1]))
    print("Klassifisering: {}".format(a2))
    print("b)\nKritisk punkt til g i [x, y, z] = [{}, {}, {}]".format(a3[0], a3[1], a3[2]))
    print("Klassifisering: {}".format(a4))


#Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    fxy, rad = myArr
    sub = [rad*cos(theta), rad*sin(theta)]
    fsub = fxy.subs({x: sub[0], y: sub[1]})
    grad = Grad(fsub, vars = [theta])[0]
    ekstremal = solve(grad, theta)
    verdier = [fsub.subs(theta, ekstremal[i]) for i in range(len(ekstremal))]
    topp = max(verdier)
    bunn = min(verdier)
    ekstremal.sort()
    if fsub.subs(theta, ekstremal[0]) == bunn: ekstremal.sort(reverse=True)
    a1 = [k.subs(theta, ekstremal[0]) for k in sub]
    a2 = [-k for k in a1]
    if a1[0] > a2[0]:
        tempA = [a1[0], a1[1]]
        a1 = [a2[0], a2[1]]
        a2 = tempA
    a3 = [k.subs(theta, ekstremal[1]) for k in sub]
    a4 = [-k for k in a3]
    if a3[0] > a4[0]:
        tempA = [a3[0], a3[1]]
        a3 = [a4[0], a4[1]]
        a4 = tempA

    print("Resultater:")
    print("a)\nFørste toppunkt: [x, y] = [{}, {}]".format(a1[0], a1[1]))
    print("Andre toppunkt: [x, y] = [{}, {}]".format(a2[0], a2[1]))
    print("Funksjonsverdi: z = {}".format(topp))
    print("b)\nFørste bunnpunkt: [x, y] = [{}, {}]".format(a3[0], a3[1]))
    print("Andre bunnpunkt: [x, y] = [{}, {}]".format(a4[0], a4[1]))
    print("Funksjonsverdi: z = {}".format(bunn))

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    fxy, rad = myArr
    lam = symbols('lambda')

    gxy = x**2 + y**2 -rad**2
    Lxy = fxy -lam*gxy
    gradL = Grad(Lxy, (x, y, lam))
    D = gradL[1].subs(lam, solve(gradL[0], lam)[0])
    solTemp = solve(D, y)[0]
    solx = solve(gradL[2].subs(y, solTemp), x)
    soly = [solTemp.subs(x, solx[i]) for i in range(len(solx))]
    maxmin = [0, 1]
    if fxy.subs({x: solx[0], y: soly[0]}) < fxy.subs({x: solx[1], y: soly[1]}): maxmin.reverse()

    print(solx)
    print(fxy.subs({x: solx[0], y: soly[0]}))
    print(fxy.subs({x: solx[1], y: soly[1]}))

    print("Resultater:")
    print("Del 1:")
    print("g(x, y) = {}".format(gxy))
    print("L(x, y, lambda) = {}".format(Lxy))
    print("Del 2:")
    print("dLdx = {}".format(gradL[0]))
    print("dLdy = {}".format(gradL[1]))
    print("dLdz = {}".format(gradL[2]))
    print("Del 3:")
    print("Likningssett D: {} = 0".format(D))
    print("Toppunkt i [x, y] = [{}, {}]".format(solx[maxmin[0]], soly[maxmin[0]]))
    print("Bunnpunkt i [x, y] = [{}, {}]".format(solx[maxmin[1]], soly[maxmin[1]]))

#-----------------------------------

#Funksjoner

def Grad(func, vars = (x, y)):
    gradient = [diff(func, k) for k in vars]
    return gradient

def CriticalPointClass(H):
    eig = np.linalg.eigvals(H)
    positiveEig = False
    negativeEig = False
    zeroEig = False
    for x in eig:
        if x > 0: positiveEig = True
        if x < 0: negativeEig = True
        if x == 0: zeroEig = True
    classification = "Ikke konklusivt"
    if positiveEig and not negativeEig and not zeroEig: classification = "Bunnpunkt"
    if not positiveEig and negativeEig and not zeroEig: classification = "Toppunkt"
    if positiveEig and negativeEig: classification = "Sadelpunkt"
    return classification

if __name__ == '__main__':
    opg1(arr1)
    opg2(arr2)
    opg3()
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

