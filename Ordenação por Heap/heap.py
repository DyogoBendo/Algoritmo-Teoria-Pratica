from typing import Mapping


def max_heapfy(A, i):
    l = 2 * i
    r = 2*i + 1
    
    if l < len(A):
        if A[l] > A[i]:
            maior = l
        else:
            maior = i
    else:
        maior = i

    if r < len(A):
        if A[r] > A[i]:
            maior = r
        else:
            maior = i
    else:
        maior = i
    
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapfy(A, maior)        


if __name__ == "__main__":        
    heap = [5, 0, 3, 1, 2]
    print(heap)
        
    max_heapfy(heap, 1)
    