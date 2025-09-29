import numpy as np

a = 6
L = np.zeros(a)
q = np.floor(len(L/2))
list = []

for i in range(0,a):
    list.append(0)

print(list)
#print(q)
#print(L)
#print(len(L[0:2]))

print(np.floor(9/2)) # should equal 4

def merge(A, p, q, r):
    L=[]
    R=[]

    for i in range(p, q+1):
        L.append(A[i])
    for j in range(q+1,r+1):
        R.append(A[j])

    i=0
    j=0
    k=p

    while i <q-p+1 and j<r-q:
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = A[j]
            j = j+1
        k = k+1

    while i < q-p+1:
        A[k] = L[i]
        i = i + 1
        k = k + 1
    while j < r-q:
        A[k] = R[j]
        j = j + 1
        k = k + 1