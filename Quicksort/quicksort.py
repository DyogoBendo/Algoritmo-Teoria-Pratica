from random import randint

def quicksort(A, p, r):
    if p < r:
        q = randomized_partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    
    if A[p] == A[r - 1]:  # condição para quando todos os elementos são iguais
        i = (p + r) // 2
    
    return i + 1

def randomized_partition(A, p, r):
    i = randint(p, r)
    A[r], A[i] = A[i], A[r]  # trocamos a ultima posicao por um elemento aleatorio
    return partition(A, p, r)
    
def hoare_partition(A, p, r):
    print("hey ey")
    x = A[p]
    i = p - 1
    j = r + 1
    
    while True:        
        while True:
            j -= 1
            if A[j] <= x:
                break
        print("j:", A[j])
        print(A)
        print()
        
        while True:
            i += 1
            if A[i] >= x:
                break
        print("i: ", A[i])        
        print(A)
        print()
        
        if i < j:
            A[i], A[j] = A[j], A[i]
            print("troca: ", A)
            print()
        else:
            print(A)
            print()
            return j
    
    

def quicksort_decreasing(A, p, r):
    if p < r:
        q = partition_decreasing(A, p, r)
        quicksort_decreasing(A, p, q - 1)
        quicksort_decreasing(A, q + 1, r)


def partition_decreasing(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    
    if A[p] == A[r - 1]:  # condição para quando todos os elementos são iguais
        i = (p + r) // 2
    
    return i + 1

def tail_recursive_quicksort(A, p, r):
    while p < r:
        q = partition(A, p, r)  
        tail_recursive_quicksort(A, p, q - 1)
        p = q + 1

                
if __name__ == "__main__":
    A = list({randint(0, 100)  for _ in range(11)})
    
    print(A)
    
    quicksort(A, 0, len(A) - 1)    
    print(A)
    
    quicksort_decreasing(A, 0, len(A) - 1)    
    print(A)
    
    print(hoare_partition([13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21], 0, 11))
    print()
    
    print(partition_2([13, 19, 9, 5, 12, 8, 7, 4, 11, 2, 6, 21], 0, 11))
    