import numpy as np
import matplotlib.pyplot as plt

alpha = 0.25
a = np.zeros((6,6))

a[0][0:6] = 100
delta_x = 0.1
delta_t = 0.01
a_futuro = np.zeros((6,6))
a_futuro[0][0:6] = 100
tempo = np.arange(0, 10, delta_t)

for t in tempo:
  for i in range(0,4):
    for j in range(1,5):
      Fo = (alpha*delta_t/(delta_x**2))
      a_futuro[i][j] = Fo*(a[i+1][j] - 2*a[i-1][j] + a[i][j+1] + a[i][j-1])+(1-4*Fo)*a[i][j]
    a = np.copy(a_futuro)

print(a_futuro)
