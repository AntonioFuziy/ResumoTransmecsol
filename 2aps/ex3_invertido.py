import numpy as np
import matplotlib.pyplot as plt
import math

k = 1
alpha = 1
T = 3
Q = 80
# n = 5
# a = n/1.4
# b = 60/(n+5)
t_final = 5
delta_x = 0.5
delta_y = delta_x
delta_t = 0.05#(delta_x**2)/(4*k) - 0.0125
tempo = np.arange(0, 50*delta_t, delta_t)
c = np.zeros((61,61))
c_futuro = np.zeros((61,61))

for t in tempo:
  for x in range(0, 60):
    for y in range(0, 60):
      dcdx = (alpha*(c[y+1][x] - c[y-1][x])/(delta_x*2))
      dcdy = 0#((alpha*math.sin(x*(math.pi/5)))*(c[x][y+1] - c[x][y-1])/(2*delta_y))
      d2cdx2 = k*((c[y+1][x] - 2*c[y][x] + c[y-1][x])/(delta_x**2))
      d2cdy2 = k*((c[y][x+1] - 2*c[y][x] + c[y][x-1])/(delta_y**2))
      if(t < 2 and x == 15 and y == 15):
        q = Q/(delta_x*delta_y)
      else:
        q = 0
      c_futuro[y][x] = c[y][x] + delta_t*(-dcdx - dcdy + d2cdx2 + d2cdy2 + q)
      if(c_futuro[y][x] < 0):
        c_futuro[y][x] = 0
      if(x == 1):
        c_futuro[0][x] = c_futuro[1][x]
      elif(x == 30):
        c_futuro[30][x] = c_futuro[29][x]
      elif(y == 0):
        c_futuro[y][0] = c_futuro[y][1]
      elif(y == 30):
        c_futuro[y][30] = c_futuro[y][29]
  c = np.copy(c_futuro)
plt.imshow(c_futuro)
# plt.gca().invert_xaxis()
# plt.gca().invert_yaxis()
print(c_futuro[40][40])
plt.xlim(0,30)
plt.ylim(0,30)
plt.clim(0, 1)
plt.colorbar()
plt.show()
print(c_futuro)