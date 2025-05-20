# Secant method

def Sec(x_0, x_1, n_max, prec):  

  i = 1
  x_k = x_0
  x_k_next = x_1
  
  while(minDiag(x_k_next-prec) * minDiag(x_k_next + prec)> 0 and i < n_max):
    tmp = x_k - minDiag(x_k) * (x_k_next - x_k) / (minDiag(x_k_next - prec)-minDiag(x_k))

    print(i, x_k, x_k_next, minDiag(x_k_next), minDiag(x_k_next - prec) * minDiag(x_k_next + prec))
    x_k = x_k_next
    x_k_next = tmp
    i += 1

# Maximum number of interactions
n_max=20
# Interval
x_0=-10
x_1=-9.9
# Precision
prec= 10 ** -8

Sec(x_0, x_1, n_max, prec)
      
     

