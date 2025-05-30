# Exercise 1
# For k = 10, calculate the Legendre polynomials P0(x), P1(x), ... , Pk-1(x) for 
# x = 0.7688
# Calculating each Legendre polynomial
import math
def fj(x,k):
  j = k
  soma = 0
  # Implementing the sum of i from 0 to j until reaching k
  for i in range(0,j+1,1):
    soma += ((math.factorial(j)/(math.factorial(i)*(math.factorial(j-i))))*(math.factorial(j+i)/(math.factorial(i)*math.factorial(j)))*((x-1)/2)**i)
  return soma

x = 0.7688
k = 10
legendre = []
# Iterating according to the value of k
for n in range(k):
  legendre.append(fj(x, n))
  print(f'P{n}(x) = {fj(x, n)}')

print(legendre)



