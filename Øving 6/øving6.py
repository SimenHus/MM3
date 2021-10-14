from sympy import *


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
fxy = x**2+y**2 #Funksjonen som skal integreres i a)
xlimA = [-3, 3] #Grensene x skal integreres mellom (integralet til høyre)
ylimA = [-2, 2] #Grensene y skal integreres mellom (integralet til venstre)
#b)
gxy = 1-(x**2+y**2) #Funksjonen som skal integreres i b)
xlimB = [-3, 0] #Grensene x skal integreres mellom (integralet til høyre)
ylimB = [0, 2] #Grensene y skal integreres mellom (integralet til venstre)


arr1 = [(fxy, xlimA, ylimA), (gxy, xlimB, ylimB)]

#Oppgave 2
#a)
fxy = 1 #Funksjonen som skal integreres i a)
xlimA = [0, y**2] #Grensene x skal integreres mellom (integralet til høyre)
ylimA = [0, 2] #Grensene y skal integreres mellom (integralet til venstre)
#b)
gxy = 1 #Funksjonen som skal integreres i b)
xlimB = [y**2, 2**2] #Grensene x skal integreres mellom (integralet til høyre)
ylimB = [0, 2] #Grensene y skal integreres mellom (integralet til venstre)
arr2 = [(fxy, xlimA, ylimA), (gxy, xlimB, ylimB)]

#Oppgave 3
#Antar samme oppgave for alle, slik at du ikke trenger å fylle inn noe :)

#Oppgave 4
fxy = sin(x*y)
xlim = [-1, 1] #Grensene x skal integreres mellom (integralet til høyre)
ylim = [-3, 3] #Grensene y skal integreres mellom (integralet til venstre)

arr4 = [(fxy, xlim, ylim), ()]

#Oppgave 5
#a)
fxy = r #Funksjonen som skal integreres i a)
xlimA = [0, theta] #Grensene r skal integreres mellom (integralet til høyre)
ylimA = [0, 2*pi] #Grensene theta skal integreres mellom (integralet til venstre)
#b)
gxy = r #Funksjonen som skal integreres i b)
xlimB = [theta, 2*pi] #Grensene r skal integreres mellom (integralet til høyre)
ylimB = [0, 2*pi] #Grensene theta skal integreres mellom (integralet til venstre)
arr5 = [(fxy, xlimA, ylimA), (gxy, xlimB, ylimB)]

#Oppgave 6
corners = [(4, 0), (0, 9)] #Hjørnene til trekanten. Pass på at leddet med +- står som første del av listen
arr6 = [corners]

#Oppgave 7
#Se teoribiten

#Oppgave 8
fxy = x**2+y**2+x #Integranden
ylim = [-x, x] #Grenser til y (innerste integral)
xlim = [0, 3] #Grenser til x (ytterste integral)
arr8 = [fxy, ylim, xlim]

#-------------------------------------

#Oppgave 1

def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    a, b = myArr

    a1 = integrate(a[0], (x, a[1][0], a[1][1]), (y, a[2][0], a[2][1]))
    a2 = integrate(b[0], (x, b[1][0], b[1][1]), (y, b[2][0], b[2][1]))

    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(a2))

#Oppgave 2

def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    a, b = myArr

    a1 = integrate(a[0], (x, a[1][0], a[1][1]), (y, a[2][0], a[2][1]))
    a2 = integrate(b[0], (x, b[1][0], b[1][1]), (y, b[2][0], b[2][1]))

    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(a2))

#Oppgave 3

def opg3():
    print("\n\n\n\n\n\n\n\nOppgave 3:")

    ansList = [0, 1, 0, x, 1/2-cos(1)/2]
    varList = ["a", "b", "c(x)", "d(x)", "Endelig svar"]
    print("Resultater:")
    for i in range(len(ansList)): print("{} = {}".format(varList[i], nsimplify(ansList[i])))
    
#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    a, b = myArr

    a1 = integrate(a[0], (x, a[1][0], a[1][1]), (y, a[2][0], a[2][1]))

    print("Resultater:")
    print("a) {}".format(a1))

#Oppgave 5

def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    a, b = myArr

    a1 = integrate(a[0], (r, a[1][0], a[1][1]), (theta, a[2][0], a[2][1]))
    a2 = integrate(b[0], (r, b[1][0], b[1][1]), (theta, b[2][0], b[2][1]))

    print("Resultater:")
    print("a) {}".format(a1))
    print("b) {}".format(a2))

    #Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    a = myArr[0]

    a1 = 1
    punkter = [(-a[0][0], a[0][1]), a[0], a[1]]
    nedreGrenseX = Topunktsformel(punkter[0], punkter[2], x)
    ovreGrenseX = Topunktsformel(punkter[1], punkter[2], x)
    a2 = [nsimplify(nedreGrenseX), nsimplify(ovreGrenseX)]
    a3 = [punkter[2][1], 0]

    print("Resultater:")
    print("f(x, y) = {}".format(a1))
    print("a1(y) = {}".format(a2[0]))
    print("b1(y) = {}".format(a2[1]))
    print("a2 = {}".format(a3[1]))
    print("b2 = {}".format(a3[0]))

#Oppgave 7
def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    print("Se teoribiten, sorry")


#Oppgave 8
def opg8(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 8:")
    fxy, ylim, xlim = myArr
    grt = cart2sylExp(fxy)*r
    print("Resultater:")
    print("g(r, theta) = {}".format(grt))
    print("a = -pi/4")
    print("b = pi/4")
    print("c(theta) = 0")
    print("d(theta) = {}".format(xlim[1]/cos(theta)))

#-----------------------------------

def Topunktsformel(p1, p2, var = y):
    x1, y1 = p1
    x2, y2 = p2
    return solve(y-y1 - (y2-y1)/(x2-x1)*(x-x1), var)[0]


def checkType(myEq):
    syms = myEq.free_symbols
    if r not in syms and theta not in syms and rho not in syms and phi not in syms: return "cart"
    if x not in syms and y not in syms and rho not in syms and phi not in syms: return "syl"
    if x not in syms and y not in syms and z not in syms and r not in syms: return "sphere"


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
#Funksjoner

if __name__ == '__main__':
    opg1(arr1)
    opg2(arr2)
    opg3()
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

    print("Resultater:")
    print("a)")
    print("b)")
    print("c)")

