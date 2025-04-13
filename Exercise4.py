# Calculating the maximum error (absolute value) where y(x) = sin(pi*x) = cos(pi*x) is the 
# exact solution of a differential equation

import numpy as np
import math

def F_otimizado(x, k, a, b, m):
  coef = []
  
  for j in range(1, k+1):
     coef.append((((2 * j) - 1) / 2) * trapezios(a, b, m, j - 1))
  resposta = []
  # Calculating F(x) using a list of x
  for i in range(len(x)):
    somatorio = 0
    for j in range(1, k+1):
      somatorio += integral2_fj(x[i], j - 1) * coef[j-1]
    resposta.append(somatorio)
  return resposta

# Solution of the equation
def y(x):
  return math.sin(math.pi*x) + math.cos(math.pi*x)
h=2 / 10117
# List of x with variations according to its range
x = [-1 + i*h for i in range(0, 10118)]
w = []
for i in range(len(x)):
  w.append(y(x[i]))


def Gk_otimizado(x, k, a, b, m):
  alpha = -1
  beta = -1
  # A list with the values of x
  v1 = F_otimizado(x, k, a, b, m)
  # Invariable expressions
  expression = (alpha - F(-1, k, a, b, m))
  expression2 = (beta - F(1, k, a, b, m))
  resultado = []
  for i in range(len(x)):
    resultado.append(v1[i] + expression * ((1 - x[i]) / 2) + expression2 * ((x[i] + 1) / 2))
  return resultado

h = 2 / 10117
m = 10**4
a = -1
b = 1
x = [-1 + i*h for i in range(0, 10118)]


def Em(g,w):
  errorMax = 0
  for i in range(len(w)):
    error = abs(w[i] - g[i])
    if error > errorMax:
      errorMax = error
  return errorMax
for k in range(2, 31):
  print(Em(Gk_otimizado(x, k + 1, a, b, m), w))


