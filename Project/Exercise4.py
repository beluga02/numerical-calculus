# Calculating the shortest diagonal 

import numpy as np
def matrix(n:int, q:float, p:float):
  b = 1
  a = 0
  h=(b - a) / n
  matriz = np.zeros(shape=(n - 1, n - 1))
  for i in range(n - 1):
      matriz[i, i] = 2 + (h ** 2) * q
  for k in range(n - 2):
      matriz[k + 1, k] = -1 - (h / 2) * p
      matriz[k, k + 1] = -1 + (h / 2) * p
        

  return matriz


def escalonamento(A):
  for j in range(0, len(A)):
    l = j
    while(A[l, j] == 0):
      l += 1
    if(l > len(A)):
      print('ERROR: singular matrix')
    
    if(A[j, j] == 0):
      A[j], A[l] = A[l], A[j]
    else:
      for i in range(j+1,len(A)):
        m = - A[i, j] / A[j, j]
        for k in range(j, len(A)):
          A[i, k] += m * A[j, k] 
    
  return A


def menor_diagonal(A):
  menor_valor = A[0, 0]
  for i in range(0, len(A)):
    for j in range(0, len(A)):
      if(menor_valor > A[i, j] and i == j):
          menor_valor = A[i, j]

  return menor_valor


menor_diagonal(escalonamento(matrix(20, -8, 0)))

# Using q as a parameter

def minDiag(q:float):
  n, b, a,p = 20, 1, 0, 0
  h = (b - a) / n
  matriz = np.zeros(shape=(n - 1, n - 1))
  for i in range(n - 1):
      matriz[i, i] = 2 + (h ** 2) * q
  for k in range(n - 2):
      matriz[k + 1, k] = -1 - (h / 2) * p
      matriz[k, k + 1] = -1 + (h / 2) * p

  for j in range(0, len(matriz)):
    l = j
    while(matriz[l, j] == 0):
      l += 1
    if(l > len(matriz)):
      print('ERROR: singular matrix')
    
    if(matriz[j, j] == 0):
      matriz[j], matriz[l] = matriz[l], matriz[j]
    else:
      for i in range(j + 1, len(matriz)):
        m = - matriz[i, j] / matriz[j, j]
        for k in range(j, len(matriz)):
          matriz[i, k] += m * matriz[j, k] 

  menor_valor = matriz[0, 0]
  for i in range(0, len(matriz)):
    for j in range(0, len(matriz)):
      if(menor_valor > matriz[i,j] and i == j):
          menor_valor = matriz[i,j]
        

  return menor_valor


results_21 = []
for q in range(-10, 0, 1):
  results_21.append(minDiag(q))
print(results_21)


# Plotting the graph

import matplotlib.pyplot as plt

x = np.array([q for q in range(-10, 1, 1)])
y = np.array([minDiag(q) for q in range(-10, 1, 1)])

plt.plot(x, y,color="red")

plt.title("Function MinDiag on the interval [-10, 0]")
plt.xlabel("Interval")
plt.ylabel("Minimum value of the main diagonal")
plt.grid()

plt.show()

# Using 100 points to compare the curve of the previous graph

x = np.array([q for q in range(0, 101, 1)])
y = np.array([minDiag(q) for q in range(0, 101, 1)])

plt.plot(x, y,color="red")

plt.title("Function MinDiag on the interval [-10, 0] - More values included")
plt.xlabel("Interval")
plt.ylabel("Minimum value of the main diagonal")
plt.grid()

plt.show()
