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


gaussSeidel(A, vh, len(A), w_0, 7, x)

# Calculating the error

def E(n:int):
    a, b, p, q = 0, 1, 0, math.pi ** 2
    h = (b - a) /n 

    proj_y = []
    x = [(a + (i - 1) * h) for i in range(1, n + 2)]

    for j in range(1, n):
        y = math.sin(math.pi * x[j])    
        proj_y.append(y)

    A = np.zeros(shape=(n - 1, n - 1))
    for i in range(n - 1):
        A[i, i] = 2 + (h ** 2) * q
    for k in range(n - 2):
        A[k + 1, k] = -1 - (h / 2) * p
        A[k, k + 1] = -1 + (h / 2) * p

    vh = []
    alpha = 0
    beta = 0
    for i in range(n-1):
        r = -(2 * (math.pi ** 2)) * math.sin(math.pi * x[i+1])
        vh.append((h**2)*(-r))

    for j in range(0, n-1):
        l = j
        while A[l, j] == 0:
            l += 1
        if l > n:
            print("Singular system")
        if A[j, j] == 0:
            A[j], A[l] = A[l], A[j]
        else:
            T = vh[j]
            vh[j] = vh[l]
            vh[l] = T
            for i in range(j + 1, n - 1):
                m = - A[i, j] / A[j, j]
                for k in range(j, n - 1):
                    A[i, k] += m * A[j, k]
                vh[i] += m * vh[j]
    x = [0 for i in range(n - 1)]
    for k in reversed(range(n - 1)):
        x[k] = vh[k]
        for j in range(k + 1, n - 1):
            x[k] = x[k] - A[k, j] * x[j]
        x[k] = x[k] / A[k, k]

    erro = []
    for i in range(n - 1):
        erro.append(abs(proj_y[i] - x[i]))

    return max(erro)

# Running time: 11 minutes e 52 seconds

results_32 = [E(n) for n in range(100, 1100, 100)]
print(results_32)
