from random import randint

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
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
    

if __name__ == "__main__":
    A = list({randint(0, 100)  for _ in range(11)})
    
    print(A)
    
    quicksort(A, 0, len(A) - 1)    
    print(A)
    
    quicksort_decreasing(A, 0, len(A) - 1)    
    print(A)