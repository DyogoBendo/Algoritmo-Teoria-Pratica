from random import randint

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

    print()

    print(B)
    print(min_max_simultaneos(B))