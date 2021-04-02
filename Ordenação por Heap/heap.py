from math import ceil, inf
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

def max_heapfy_loop(A, i, end = -1):
    if end == -1:
        end = len(A)
    B = A[:end]                        
    while True: 
        l = 2 * i + 1 if 2 * i + 1 < len(B) else None
        r = 2 * i + 2 if 2 * i  + 2 < len(B) else None
                
        if not l and not r:
            maior = None
        
        elif not l and r:
            maior = r
        
        elif not r and l:
            maior = l
        
        else:
            maior = l if B[l] > B[r] else r
    
        if not (maior and B[maior] > B[i]):
            break
        B[i], B[maior] = B[maior], B[i]        
        i = maior                         

    A[:end] = B

def build_max_heap(A):
    for i in range(len(A) // 2, -1, -1):
        max_heapfy(A, i)    

def build_min_heap(A):
    for i in range(len(A) // 2, -1, -1):
        min_heapfy(A, i)    

def heapsort(A):
    build_max_heap(A)
    diminui = 0          
    for i in range(len(A) - 1, 0, -1):
        diminui -= 1             
        A[i], A[0] = A[0], A[i]             
        max_heapfy_loop(A, 0, len(A) + diminui)        


def heap_maximum(A):  # retorna o maior elemento de um heap maximo
    return A[0]

def heap_minimun(A):
    return A[0]

def heap_extract_max(A):
    if len(A) < 1:
        raise Exception(IndexError)
    max, A[0] = A[0], A[- 1]            
    A.pop(-1)
    
    max_heapfy_loop(A, 0)
    
    return max        


def heap_extract_minimun(A):
    if len(A) < 1:
        pass
    else:
        min, A[0] = A[0], A[-1]
        A.pop(-1)
        
        min_heapfy(A, 0)
        
        return min

def heap_increse_key(A, i, chave):
    if chave < A[i]:
        pass
    else:        
        while i > 0 and A[i // 2] < chave:
            A[i] = A[i//2]
            i = i // 2
        A[i] = chave

def heap_descrese_key(A, i, chave):
    if chave > A[i]:
        pass
    else:
        A[i] = chave
        while i > 0 and A[i // 2] > A [i]:
            A[i], A[i // 2] = A[i // 2], A[i]
            i = i // 2
            
def max_heap_insert(A, chave):
    A.append(-inf)
    heap_increse_key(A, len(A) - 1, chave)

def max_heap_delete(A, i):
    if len(A) < i:
        pass
    chave, A[i] = A[i], A[- 1]            
    A.pop(-1)
    
    max_heapfy_loop(A, i)
    
    return chave        

def min_heap_insert(A, chave):
    A.append(inf)
    heap_descrese_key(A, len(A) - 1, chave)
    

def build_max_heap_2(A):      
    B = []  
    for i in range(0, len(A)):
        max_heap_insert(B, A[i])
    return B
    
if __name__ == "__main__":        
    heap = [5, 0, 3, 1, 2]    
    random_heap = [randint(0, 100) for i in range(5)]    
    
    # print(heap)
    print(random_heap)
    print("-" * 30)
    
    
    nice = build_max_heap_2(random_heap)
    print(nice)    
    
    print("-" * 30)
        
    build_max_heap(random_heap)
    print(random_heap)                
    
    # max_heapfy_loop(heap, 1)
    # print(heap)
        
    # max_heapfy(heap, 1) 
    # print(heap)
    
    # min_heapfy(heap, 1)
    # print(heap)
    
    
    # print(heap_extract_max(random_heap))
    # print(random_heap)
    
    # heap_increse_key(random_heap, 3, 50)
    # print(random_heap)
    
    # max_heap_insert(random_heap, 72)
    # print(random_heap)
    
    # print(max_heap_delete(random_heap, 1))
    # print(random_heap)
    
    # ------------------------------------
    
    # build_min_heap(random_heap)
    # print(random_heap)
    
    # print(heap_extract_minimun(random_heap))
    # print(random_heap)
    
    # heap_descrese_key(random_heap, 2, 17)
    # print(random_heap)
    
    # min_heap_insert(random_heap, 43)
    # print(random_heap)
    
    # build_min_heap(random_heap)
    # print(random_heap)
    
    # heapsort(random_heap)
    # print(random_heap)
    
    
    