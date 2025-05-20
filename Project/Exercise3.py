# Implementing the Gaussian elimination

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
  for j in range(0,len(A)):
    l = j
    while(A[l, j] == 0):
      l += 1
    if(l > len(A)):
      print('ERROR: singular matrix')
    
    if(A[j, j] == 0):
      A[j], A[l] = A[l], A[j]
    else:
      for i in range(j + 1,len(A)):
        m = -A[i, j] / A[j, j]
        for k in range(j, len(A)):
          A[i, k] += m * A[j, k] 
    
  return A


escalonamento(matrix(5, -8, 0))
