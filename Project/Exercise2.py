# Creating a matrix of vectors equal to zero and alternating the values of the diagonal and indexes less and bigger than 1

import numpy as np


def matrix(n:int, q:float, p:float):
  b = 1
  a = 0
  h = (b - a) / n
  matriz = np.zeros(shape=(n - 1, n - 1))
  for i in range(n - 1):
      matriz[i, i] = 2 + (h ** 2) * q
  for k in range(n - 2):
      matriz[k + 1, k] = -1 - (h / 2) * p
      matriz[k, k + 1] = -1 + (h / 2) * p
        

  return matriz


print(matrix(8, -8, 0))
