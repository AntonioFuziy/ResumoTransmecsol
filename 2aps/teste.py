import numpy as np

matrix = np.zeros((3,3))
cont = 0

for i in range(0,3):
  for j in range(0,3):
    cont+=1
    matrix[i][j] = cont

print(matrix)