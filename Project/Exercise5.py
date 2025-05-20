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
  

# Maximum number of interactions
n_max=20
# Interval
x_0=-10
x_1=-9.9
# Precision
prec= 10 ** -8

Sec(x_0, x_1, n_max, prec)
      
     

