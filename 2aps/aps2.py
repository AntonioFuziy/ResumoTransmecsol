import numpy as np
import matplotlib.pyplot as plt
import math

k = 1
alpha = 1
T = 3
Q = 100
t_final = 10*T
delta_x = 0.5
delta_y = delta_x
delta_t = (delta_x**2)/(4*k) - 0.0025
tempo = np.arange(0, t_final, delta_t)
c = np.zeros((61,41))
c_futuro = np.zeros((61,41))

for t in tempo:
  for x in range(0, 60):
    for y in range(0, 40):
      dcdx = (alpha*(c[x+1][y] - c[x-1][y])/(delta_x*2))
      dcdy = ((alpha*math.sin(x*(math.pi/5)))*(c[x][y+1] - c[x][y-1])/(2*delta_y))
      d2cdx2 = k*((c[x+1][y] - 2*c[x][y] + c[x-1][y])/(delta_x**2))
      d2cdy2 = k*((c[x][y+1] - 2*c[x][y] + c[x][y-1])/(delta_y**2))
      if(t < 12 and x == 30 and y == 20):
        q = Q/(delta_x*delta_y)
      else:
        q = 0
      c_futuro[x][y] = c[x][y] + delta_t*(-dcdx - dcdy + d2cdx2 + d2cdy2 + q)
      if(c_futuro[x][y] < 0):
        c_futuro[x][y] = 0
      if(x == 0):
        c_futuro[0][y] = c_futuro[1][y]
      elif(x == 60):
        c_futuro[60][y] = c_futuro[59][y]
      elif(y == 0):
        c_futuro[x][0] = c_futuro[x][1]
      elif(y == 40):
        c_futuro[x][40] = c_futuro[x][39]
  c = np.copy(c_futuro)
plt.imshow(c_futuro, vmin=0, vmax=1)
# print(c_futuro[40][40])
# plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
plt.colorbar()
plt.show()
print(c_futuro)