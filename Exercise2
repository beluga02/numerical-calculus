# Applying the Trapezoidal Rule
# Let's solve the exercise y''(x) = -pi^2(sin(pi*x) + cos(pi*x)), y(-1) = y(1) = -1,
# alpha and beta are equal to -1
# Solution y(x) = sin(pi*x) + cos(pi*x)

import math

# y''(x)
def r(x):
  return (-(math.pi**2)*(math.sin(math.pi*x) + math.cos(math.pi*x)))

def fj(x,k):
  j = k
  soma = 0
  for i in range(1,j+1,1):
    soma += ((math.factorial(j)/(math.factorial(i)*(math.factorial(j-i))))*(math.factorial(j+i)/(math.factorial(i)*math.factorial(j)))*((x-1)/2)**i)
  return soma


m = 10**4
a = -1
b = 1
k = 9


# Implementing the Trapezoidal Rule
def trapezios(a,b,n,k):
  resp = (1/2)*((fj(a,k)*r(a))+(fj(b,k)*r(b)))
  h = (b-a)/n
  for i in range(1,n):
    resp += (fj(a+(i*h),k))*(r(a+(i*h)))
  resp *= h
  return resp

alphas = []
# Iterating j from 1 to k
for j in range(1, k+1):
  exp_alpha = "{:e}".format((((2*j)-1)/2)*trapezios(a,b,m,j-1))
  print(f'alpha{j}={exp_alpha}')
  alphas.append((((2*j)-1)/2)*trapezios(a,b,m,j-1))

print(alphas)


