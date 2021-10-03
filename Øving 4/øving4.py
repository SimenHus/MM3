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


#Skriv dine verdier her

#Oppgave 1
#a)
fxy = x**2*y**2 - 10*x*y + 25 #Funksjon f(x, y)
dxdt = -3 #Hastighet i x
dydt = -1 #Hastighet i y
pos = (3, 2) #Posisjon i tidspunkt t

#b)
dzdx = 18*x
dzdy = 1
arr1 = [(fxy, dxdt, dydt, pos), (dzdx, dzdy)]


#Oppgave 2

punkt = [5, -5, 300] #Punkt = [(x, y), h]
stigning = [-1/5, 1/5] #stigning = [stigning x, stigning y]

arr2 = [(punkt), (stigning)]

#Oppgave 3

T1 = [(5, -2, -5), 12] #T(x, y, z) = [(x, y, z), verdi]
T2 = [(10, -2, -5), 11] #Endring i x
T3 = [(5, 3, -5), 13] #Endring i y
T4 = [(5, -2, 0), 11] #Endring i z
retningsvektor = [3, 4, 5] #Retningsvektor hvor vi skal finne stigningstall
wPunkt = [10, -7, 5] #Punkt vi skal finne ved bruk av tilnærming

arr3 = [(T1, T2, T3, T4), retningsvektor, wPunkt]

#Oppgave 4

Txyz = 10*E**(-x**2-y**2-z**2) #T(x, y, z)
punkt = (4, -5, -3) #Oppgitt punkt

arr4 = [Txyz, punkt]

#Oppgave 5
fxy = (ln(sqrt(x/y)), sqrt(x*y)) #f(x, y) = (u(x, y), v(x, y)) = ...

arr5 = fxy

#Oppgave 6
xy = (1, 2) #(x, y) = (..., ...)
Df = [ #Oppgitt matrise for xy
            [4, 3], #Rad 1
            [1, 8]  #Rad 2
        ]
Dh = [ #Den oppgitte matrisen til h (jacobimatrisen)
            [-3, -4], #Rad 1
            [1, -3]   #Rad 2
        ]
arr6 = [xy, Df, Dh]

#Oppgave 7
likning = z**4 + y**4 + x**3 - 18*x**2 + 108*x - 216 #Oppgitt likning. Ikke ta med = 0
arr7 = likning

#--------------------------------------------------

#Oppgave 1

def opg1(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 1:")
    a, b = myArr

    fxy, dxdt, dydt, pos = a
    dzdt = diff(fxy, x) * dxdt + diff(fxy, y) * dydt
    a1 = dzdt.subs({x: pos[0], y: pos[1]})

    #b) 
    xfunc = r*cos(theta)
    yfunc = r*sin(theta)
    dzdx, dzdy = b
    dzdx = sympify(dzdx)
    dzdy = sympify(dzdy)
    dzdr = dzdx.subs(x, xfunc)*diff(xfunc, r) + dzdy.subs(y, yfunc)*diff(yfunc, r)
    dzdtheta = dzdx.subs(x, xfunc)*diff(xfunc, theta) + dzdy.subs(y, yfunc)*diff(yfunc, theta)
    a2 = [dzdr, dzdtheta]

    print("Resultater:")
    print("a) {}".format(a1))
    print("b)\ndzdtheta = {}\ndzdr = {}".format(a2[1], a2[0]))

#Oppgave 2

def opg2(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 2:")
    a, b = myArr
    pos = a

    #a)
    a1 = [nsimplify(v/absV(b)) for v in b]

    #b)
    a2 = [-i for i in a1]

    #c)
    vsorost = [1/sqrt(2), -1/sqrt(2)]
    vnordvest = [-1/sqrt(2), 1/sqrt(2)]

    stigSorost = nsimplify(sum([b[i]*vsorost[i] for i in range(len(b))]))
    stigNordvest = nsimplify(sum([b[i]*vnordvest[i] for i in range(len(b))]))
    a3 = [stigSorost, stigNordvest]

    #d)
    koords = [x, y, z]
    grad = [-b[0], -b[1], 1]
    tangentplan = nsimplify(sum([grad[i]*koords[i]-grad[i]*pos[i] for i in range(len(grad))]))
    tangCoeffs = [tangentplan.coeff(k) for k in koords]
    for k in tangCoeffs:
        if k >= 1 or k <= -1: tangentplan *= k
        if k < 1 and k > -1: tangentplan /= k

    koords = [x, y]
    grad = [b[0], b[1]]
    tangentlinje = nsimplify(sum([grad[i]*koords[i] - grad[i]*pos[i] for i in range(len(grad))]))
    tangCoeffs = [tangentlinje.coeff(k) for k in koords]
    for k in tangCoeffs:
        if k >= 1 or k <= -1: tangentlinje *= k
        if k < 1 and k > -1: tangentlinje /= k

    
    a4 = [simplify(tangentplan), simplify(tangentlinje), 0]

    print("Resultater:")
    print("a) (x = {}, y = {}".format(a1[0], a1[1]))
    print("b) (x = {}, y = {}".format(a2[0], a2[1]))
    print("c)\nSørøst = {}\nNordvest = {}".format(a3[0], a3[1]))
    print("d)\nTangentplan: {} = 0\nTangentlinje: {} = 0\nStigning: {}".format(a4[0], a4[1], a4[2]))


#Oppgave 3
def opg3(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 3:")
    T, T0, dx = symbols('T T0 dx')
    Tvars, retning, wpunkt = myArr

    linearisering = (T - T0)/dx
    a1 = []
    for i in range(len(Tvars[0][0])): 
        a1.append(nsimplify(simplify(
        linearisering.subs({
            T: Tvars[i+1][1],
            T0: Tvars[0][1],
            dx: Tvars[i+1][0][i] - Tvars[0][0][i]
        }))))
    
    a2 = [nsimplify(simplify(k/absV(a1))) for k in a1]

    retning = [simplify(k/absV(retning)) for k in retning]
    a3 = sum([nsimplify(simplify(a1[i]*retning[i])) for i in range(len(retning))])

    koords = [x, y, z]
    a4 = nsimplify(Tvars[0][1] + sum([a1[i]*(koords[i] - Tvars[0][0][i]) for i in range(len(koords))]))
    a5 = nsimplify(a4.subs({
        x: wpunkt[0],
        y: wpunkt[1],
        z: wpunkt[2]}))

    print("Resultater:")
    print("dTdx = {}".format(a1[0]))
    print("dTdy = {}".format(a1[1]))
    print("dTdz = {}".format(a1[2]))
    print("Max stigning x: {}".format(a2[0]))
    print("Max stigning y: {}".format(a2[1]))
    print("Max stigning z: {}".format(a2[2]))
    print("Stigningstall i oppgitt vektorretning: {}".format(a3))
    print("Linearisert likning w = {} (P.S: Kopier hele likningen w=...)".format(a4))
    print("Tilnærmet verdi for T({}, {}, {}) = {}".format(wpunkt[0], wpunkt[1], wpunkt[2], a5))

#Oppgave 4

def opg4(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 4:")
    T, pos = myArr
    koords = [x, y, z]
    gradient = [diff(T, koords[i]).subs({
        x: pos[0],
        y: pos[1],
        z: pos[2]}) for i in range(len(koords))]

    a1 = [k/absV(gradient) for k in gradient]
    a2 = absV(gradient)
    a3 = nsimplify(simplify(sum([gradient[i]*(koords[i] - pos[i]) for i in range(len(koords))])))

    print("Resultater:")
    for i in range(len(koords)): print("{}-koordinat: {}".format(koords[i], a1[i]))
    print("Stigninstall: {}".format(a2))
    print("Likning for tangentplan: {} = 0 (P.S: Kopier hele likningen, inkludert = 0)".format(a3))

#Oppgave 5

def opg5(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 5:")
    u, v = symbols('u v')
    fxy = myArr
    koords = [x, y]
    koordsUV = [u, v]
    Df = []

    for i in range(len(fxy)):
        gradient = []
        for j in range(len(koords)):
            gradient.append(nsimplify(simplify(diff(fxy[i], koords[j]))))
        Df.append(gradient)
    
    x1 = solve(u - fxy[0], x)[0]
    x2 = solve(v - fxy[1], x)[0]
    y1 = solve(u - fxy[0], y)[0]
    y2 = solve(v - fxy[1], y)[0]
    a2 = [solve(x - x1.subs(y, y2), x)[1], solve(y - y1.subs(x, x2), y)[1]]

    Dg = []
    for i in range(len(a2)):
        gradient = []
        for j in range(len(koordsUV)):
            gradient.append(nsimplify(simplify(diff(a2[i], koordsUV[j]))))
        Dg.append(gradient)
    
    print("Resultater:")
    for i in range(len(koordsUV)):
        for j in range(len(koords)):
            print("d{}d{} = {}".format(koordsUV[i], koords[j], Df[i][j]))
    print("x(u, v) = {}".format(a2[0]))
    print("y(u, v) = {}".format(a2[1]))
    print("OBS: Hvis svaret ble feil, prøv å bytt fortegn")
    for i in range(len(koords)):
        for j in range(len(koordsUV)):
            print("d{}d{} = {}".format(koords[i], koordsUV[j], Dg[i][j]))


#Oppgave 6

def opg6(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 6:")
    xy, Df, Dh = myArr
    u, v, s, t = symbols('u v s t')
    koords = [x, y]
    koordsUV = [u, v]
    koordsST = [s, t]

    a1 = np.linalg.inv(Df)
    a2 = np.matmul(Dh, Df)
    print("Resultater:")
    for i in range(len(koords)):
        for j in range(len(koordsUV)):
            print("d{}d{} = {}".format(koords[i], koordsUV[j], nsimplify(a1[i][j])))
    print("")
    for i in range(len(koords)):
        for j in range(len(koordsST)):
            print("d{}d{} = {}".format(koordsST[i], koords[j], nsimplify(a2[i][j])))
    
    

#Oppgave 7

def opg7(myArr):
    print("\n\n\n\n\n\n\n\nOppgave 7:")
    likn = myArr
    dzdx, dzdy = symbols('dzdx dzdy')
    zx = Function('zx')(x)
    zy = Function('zy')(y)
    liknx = diff(likn.subs(z, zx), x).subs({zx: z, Derivative(z, x): dzdx})
    likny = diff(likn.subs(z, zy), y).subs({zy: z, Derivative(z, y): dzdy})
    a1 = solve(liknx, dzdx)[0]
    a2 = solve(likny, dzdy)[0]
    print("Resultater:")
    print("dzdx = {}".format(a1))
    print("dzdy = {}".format(a2))

#Funksjoner

#Returnerer lengden av en vektor, gitt vector vec
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

