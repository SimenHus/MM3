import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


def OppgaveB():
    xpoints = np.linspace(-10, 10, 20)
    ypoints = np.linspace(-10, 10, 20)
    xp, yp = np.meshgrid(xpoints, ypoints)

    L = 3
    M = 1
    r = np.array([xp, yp])  # r = (x, y)
    r1 = [r[0] + 1, r[1]]  # r1 = r + (1, 0) = (x + 1, y)
    r2 = [r[0] - 1, r[1]]  # r2 = r - (1, 0) = (x - 1, y)
    r1Len = np.sqrt(r1[0]**2 + r1[1]**2)  # |r1|
    r2Len = np.sqrt(r2[0]**2 + r2[1]**2)  # |r2|
    r1Hatt = r1/r1Len  # r1Hatt = r1/|r1|
    r2Hatt = r2/r2Len  # r2Hatt = r2/|r1|
    F = L/r1Len*r1Hatt - M/r2Len*r2Hatt  # Setter inn i v
    u = F[0]  # Første koordinat til vektorfeltet
    v = F[1]  # Andre koordinat til vektorfeltet

    fig, ax = plt.subplots()  # Lager figur element
    ax.quiver(xp, yp, u, v)  # Lager vektorpiler
    ax.grid()  # Skrur på et grid i figuren
    plt.show()  # Viser figuren vi lagde


def f(pos, t):
    x = pos[0]
    y = pos[1]
    L = 3
    M = 1
    r = np.array([x, y])  # r = (x, y)
    r1 = [r[0] + 1, r[1]]  # r1 = r + (1, 0) = (x + 1, y)
    r2 = [r[0] - 1, r[1]]  # r2 = r - (1, 0) = (x - 1, y)
    r1Len = np.sqrt(r1[0]**2 + r1[1]**2)  # |r1|
    r2Len = np.sqrt(r2[0]**2 + r2[1]**2)  # |r2|
    r1Hatt = r1/r1Len  # r1Hatt = r1/|r1|
    r2Hatt = r2/r2Len  # r2Hatt = r2/|r1|
    F = L/r1Len*r1Hatt - M/r2Len*r2Hatt  # Setter inn i v
    u = F[0]  # Første koordinat til vektorfeltet
    v = F[1]  # Andre koordinat til vektorfeltet
    return u, v

def OppgaveC():
    #Integralkurver [start posisjon, interval]
    kurve1 = [[-1, 0.5], [0, 10]]
    kurve2 = [[-1, -0.5], [0, 6]]
    kurve3 = [[-1.5, -0.5], [0, 3]]

    # Setter intervalet til integralet
    t1 = np.linspace(kurve1[1][0], kurve1[1][1], 100)
    t2 = np.linspace(kurve2[1][0], kurve2[1][1], 100)
    t3 = np.linspace(kurve3[1][0], kurve3[1][1], 100)
    sol1 = odeint(f, kurve1[0], t1)  # Finner punktene langs integralkurve 1
    sol2 = odeint(f, kurve2[0], t2)  # Finner punktene langs integralkurve 2
    sol3 = odeint(f, kurve3[0], t3)  # Finner punktene langs integralkurve 3

    # Legger resultatet til figuren
    fig, ax = plt.subplots()  # Lager figur element
    ax.plot(sol1[:, 0], sol1[:, 1], color="red")
    ax.plot(sol2[:, 0], sol2[:, 1], color="green")
    ax.plot(sol3[:, 0], sol3[:, 1], color="blue")
    ax.grid()  # Skrur på et grid i figuren
    plt.show()
    

    xpoints = np.linspace(-10, 10, 20)
    ypoints = np.linspace(-10, 10, 20)
    xp, yp = np.meshgrid(xpoints, ypoints)
    u, v = f([xp, yp], 0)
    ax.quiver(xp, yp, u, v)  # Lager vektorpiler
    #plt.show()  # Viser figuren vi lagde
    
    

def OppgaveD():
    x, y, L, M, t = sp.symbols("x y L M t") #Definerer x, y, L, M  og t som symboler uten verdier

    r = np.array([t*x, t*y])  # r = (x, y)
    r1 = [r[0] + 1, r[1]]  # r1 = r + (1, 0) = (x + 1, y)
    r2 = [r[0] - 1, r[1]]  # r2 = r - (1, 0) = (x - 1, y)
    r1Len = sp.sqrt(r1[0]**2 + r1[1]**2)  # |r1|
    r2Len = sp.sqrt(r2[0]**2 + r2[1]**2)  # |r2|
    r1Hatt = [k/r1Len for k in r1]  # r1Hatt = r1/|r1|
    r2Hatt = [k/r2Len for k in r2]  # r2Hatt = r2/|r1|
    F = [L/r1Len*r1Hatt[i] - M/r2Len*r2Hatt[i] for i in range(2) ] # Setter inn i v

    integrand = sum([F[i]*sp.diff(r[i], t) for i in range(2)])
    phi = sp.simplify(sp.integrate(integrand, (t, 0, 1)))
    print(phi)
