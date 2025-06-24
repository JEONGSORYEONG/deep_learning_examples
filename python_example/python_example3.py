import numpy as np
n = int(input())
A = np.zeros((n,n), dtype=int)

for i in range(n):
    for j in range(n):
        A[i,j] = i*n+j

print(A)
B = A.reshape(-1,) 
print(B)

