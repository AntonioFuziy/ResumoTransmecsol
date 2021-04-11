import numpy as np
import matplotlib.pyplot as plt

alpha = 1*1e-4
a = np.zeros((1,11))

a[0][1:10] = 20
delta_x = 0.05
delta_t = 5
a_futuro = np.zeros((1,11))

eixo_x = np.arange(0, 55, 5)
tempo = np.arange(0, 500, delta_t)
  # a_futuro[0][i] = a[0][i] + (alpha*delta_t/(delta_x**2)) * (a[0][i+1] - 2*a[0][i] + a[0][i-1])
for t in tempo:
  for i in range(1,10):
    a_futuro[0][i] = (alpha*delta_t/(delta_x**2))*(a[0][i+1] - 2*a[0][i] + a[0][i-1]) + a[0][i]
  a = np.copy(a_futuro)
print(a_futuro)

plt.plot(eixo_x, a_futuro[0])
plt.show()