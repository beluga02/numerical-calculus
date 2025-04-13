# Calculate the function Gk defined as 
# Gk(x) := F(x) + [alpha - F(-1)] * (1 - x) / 2 + [beta - F(1)] * (x + 1) / 2

import math
def integral2_fj(x,k):
  j = k
  soma = 0
  for i in range(0, j+1, 1):
    soma += ((math.factorial(j)/(math.factorial(i)*(math.factorial(j-i))))*(math.factorial(j+i)/(math.factorial(i)*math.factorial(j)))*((4*(((x-1)/2)**(i+2)))/((i+1)*(i+2))))
  return soma

def F(x, k, a, b, m):
  somatorio = 0
  for j in range(1, k+1, 1):
    somatorio += integral2_fj(x, j-1)*(((2*j) - 1) / 2) * trapezios(a, b, m, j-1)
  return somatorio


x = [-1, -0.7, 0, 0.3, 1]
k = 7
# y(-1) = y(1) = -1
m = 10**4
a = -1
b = 1

def Gk(x, k, a, b, m):
  alpha = -1
  beta = -1
  return F(x, k, a, b, m) + (alpha - F(-1, k, a, b, m)) * ((1 - x) / 2) + (beta - F(1, k, a, b, m)) * ((x + 1) / 2)

for i in range(len(x)):
  print(Gk(x[i], k, a, b, m))
