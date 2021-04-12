from random import randint

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


def randomized_select(A, p, r, i):
    if p ==r:
        return A[p]
    q = randomized_partition(A, p, r)
    k = q - p + 1
    if i == k:
        return A[q]
    elif i < k:
        return randomized_select(A, p, q - 1, i)
    else:
        return randomized_select(A, q + 1, r, i - k)


def min(A):
    min = A[0]
    for i in A:         
        if i < min:
            min = i
            
    return min


def min_max_simultaneos(A):
    if len(A) % 2 != 0:
        min = max = A[0]
        for i in range(1, len(A) - 1):
            a = A[i]
            b = A[i + 1]

            if a > b: 
                if a > max:
                    max = a
                if b < min:
                    min = b
            else:
                if b > max:
                    max = b
                if a < min:
                    min = a
    else:
        min = A[0]
        max = A[1]

        for i in range(2, len(A) - 1):
            a = A[i]
            b = A[i + 1]

            if a > b: 
                if a > max:
                    max = a
                if b < min:
                    min = b
            else:
                if b > max:
                    max = b
                if a < min:
                    min = a
    return (min, max)


if __name__ == "__main__":
    A = [randint(0, 100) for _ in range(10)]
    B = [randint(0, 100) for _ in range(11)]

    print(A)
    print(min(A))
    print(min_max_simultaneos(A))
    print(randomized_select(A, 0, len(A) - 1, 5))

    print()

    print(B)
    print(min_max_simultaneos(B))
    