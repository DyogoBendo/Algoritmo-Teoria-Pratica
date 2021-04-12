from random import randint

def min(A):
    min = A[0]
    for i in A:         
        if i < min:
            min = i
            
    return min


if __name__ == "__main__":
    A = [randint(0, 100) for _ in range(10)]

    print(A)
    print(min(A))