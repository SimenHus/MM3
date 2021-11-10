import numpy as np
import matplotlib.pyplot as plt

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

fig, ax = plt.subplots() #Lager figur element
ax.quiver(xp, yp, u, v) #Lager vektorpiler
ax.grid() #Skrur på et grid i figuren
plt.show() #Viser figuren vi lagde
