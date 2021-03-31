from math import ceil
from random import randint


def max_heapfy(A, i):
    l = 2 * i + 1
    r = 2*i + 2
    
    if l < len(A):
        if A[l] > A[i]:
            maior = l
        else:
            maior = i
    else:
        maior = i

    if r < len(A):
        if A[r] > A[maior]:
            maior = r
    
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapfy(A, maior)        



def min_heapfy(A, i):
    l = 2 * i + 1
    r = 2*i + 2
    
    if l < len(A):
        if A[l] < A[i]:
            menor = l
        else:
            menor = i
    else:
        menor = i

    if r < len(A):
        if A[r] < A[menor]:
            menor = r        
    
    if menor != i:
        A[i], A[menor] = A[menor], A[i]
        min_heapfy(A, menor)        

# Ambos possuem o mesmo tempo de execução

def max_heapfy_loop(A, i):    
    while True: 
        l = 2 * i + 1 if 2 * i + 1 < len(A) else None
        r = 2 * i + 2 if 2 * i  + 2 < len(A) else None
                
        if not l and not r:
            maior = None
        
        elif not l and r:
            maior = r
        
        elif not r and l:
            maior = l
        
        else:
            maior = l if A[l] > A[r] else r
    
        if not (maior and A[maior] > A[i]):
            break
        A[i], A[maior] = A[maior], A[i]        
        i = maior                         


def build_max_heap(A):
    for i in range(ceil(len(A) / 2), -1, -1):
        max_heapfy(A, i)    

def build_min_heap(A):
    for i in range(ceil(len(A) / 2), -1, -1):
        min_heapfy(A, i)    
    
if __name__ == "__main__":        
    heap = [5, 0, 3, 1, 2]    
    random_heap = [randint(0, 100) for i in range(5)]
    
    print(heap)
    print(random_heap)
    
    max_heapfy_loop(heap, 1)
    print(heap)
        
    # max_heapfy(heap, 1) 
    # print(heap)
    
    min_heapfy(heap, 1)
    print(heap)
    
    build_max_heap(random_heap)
    print(random_heap)
    
    build_min_heap(random_heap)
    print(random_heap)
    