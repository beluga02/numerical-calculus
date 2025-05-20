# Finding elements of the main diagonal 
# The bigger the number of iterations, the nearer the value reaches 1.5
def diagprincipalexerc1(x:int) -> float:
  A11 = 2
  if x == 1:
    return A11
  else:
    return 2 - 3 / (4 * diagprincipalexerc1(x - 1))

# We need to calculate the first k term of the sequence
# that alpha_zero = 2 e alpha_i+1 = phi(alpha_i), for i from 0
# to k

def sequencia(k):
    h = 1 / 10
    q = 0
    p = 10
    alpha = 2
    for i in range(k):
        alpha = 2 + (h ** 2) * q - (1 - ((h ** 2) / 4) * p ** 2) / alpha
        print("Alpha", i + 1, "é: %.52f" % alpha)


k = 64
sequencia(k)
