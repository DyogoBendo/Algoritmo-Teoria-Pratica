import math
from random import random

def bucket_sort(A):    
    n = len(A)
    B = [[] for _ in range(n)]

    for i in range(n):        
        B[math.floor(n * A[i])].append(A[i])
    
    # temos os baldes criados agora, e depois precisamos apenas ordenar cada balde individualmente, e concatená-los
    print(B)
    result = []
    for i in range(n):
        B[i].sort()
        result += B[i]
    return result

if __name__ == "__main__":
    a = [round(random(), 2) for _  in range(50)]
    print(a)

    print()
    print('\n', bucket_sort(a))