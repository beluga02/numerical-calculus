# Gauss Seidel method

# y''(x)= q(x)*y(x)+r(x)
# sin'(pi*x)= pi*-cos(pi*x)
# sin''(pi*x) = pi^2*-sin(pi*x)= pi^2*sin(pi*x) -2*(pi^2)*sin(pi*x)

import numpy as np
import math

n = 10
a, b, p, q = 0, 1, 0, math.pi ** 2
h = (b - a) / n
x = [(a + (i - 1) * h) for i in range(1, n + 2)]

vh = []
alpha = 0
beta = 0
for i in range(n - 1):
    r = - (2 * (math.pi ** 2)) * math.sin(math.pi * x[i + 1])
    vh.append((h ** 2) * (-r))

w_0 = np.zeros(n - 1)

A = np.zeros(shape=(n - 1, n - 1))
for i in range(n - 1):
    A[i, i] = 2 + (h ** 2) * q
for k in range(n - 2):
    A[k + 1, k] = -1 - (h / 2) * p
    A[k, k + 1] = -1 + (h / 2) * p
  

def q(x):
  return math.pi ** 2
def r(x):
  return -2 * math.pi ** 2 * math.sin(math.pi * x)


def sol(x):
  return math.sin(math.pi * x)

a = 0
b = 1

alph = sol(a)
bet = sol(b)

def gaussSeidel(A, y, m, x_0, nmax, x):
  k, x_old, x_new = 0, x_0, x_0
  while(k < nmax):
    x_new[0] = (1 / (2 + h ** 2 * q(x[0]))) * (y[0] + x_old[1] * (1))
    for i in range(1, m-1):
      x_new[i] = (1 / (2 + h ** 2 * q(x[i]))) * (y[i] + x_new[i - 1] * (1) + x_old[i + 1] * (1))
    x_new[m - 1] = (1 / (2 + h ** 2 * q(x[m - 1]))) * (y[m - 1] + x_new[m - 2] * (1))
    print('Interaction result', k + 1)
    print(x_new)
    x_old = x_new
    k += 1

