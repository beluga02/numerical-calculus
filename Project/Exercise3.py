# Implementing the Gaussian elimination

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
