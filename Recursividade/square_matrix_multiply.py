import random
import pprint
from math import log2, ceil

def multiply_square_matrix(A, B):
    n = len(A[0])
    c = [ [0 for _ in range(n)] for __ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += A[i][k] * B[k][j]
                            
    return c

def subtract_matrix(A, B, n):
    c = [[0 for __ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            c[i][j] = A[i][j] - B[i][j]
    
    return c

def add_matrix(A, B, n):
    c = [[0 for __ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            c[i][j] = A[i][j] + B[i][j]
    
    return c
    
def regularizate(A, B, n):
    next_2 = ceil(log2(n))
    
    Az = [[0 for _ in range(2 ** next_2)] for _ in range(2 ** next_2)]
    Bz = [[0 for _ in range(2 ** next_2)] for _ in range(2 ** next_2)]
    
    for i in range(n):
        for j in range(n):
            Az[i][j] = A[i][j]
            Bz[i][j] = B[i][j]    
    nz = next_2 * 2

    return Az, Bz, nz


def straussen_matrix(A, B, n):
    if n == 1:
        c = [[0]]
        c[0][0] = A[0][0] * B[0][0]
        return c
    
    if log2(n) < ceil(log2(n)):
        A, B, n = regularizate(A, B, n)
    
    c = [[0 for _ in range(n)] for __ in range(n)]
    k = n // 2
    
    a11 = [[0 for _ in range(k)] for __ in range(k)] 
    a12 = [[0 for _ in range(k)] for __ in range(k)] 
    a21 = [[0 for _ in range(k)] for __ in range(k)] 
    a22 = [[0 for _ in range(k)] for __ in range(k)] 
    b11 = [[0 for _ in range(k)] for __ in range(k)] 
    b12 = [[0 for _ in range(k)] for __ in range(k)] 
    b21 = [[0 for _ in range(k)] for __ in range(k)] 
    b22 = [[0 for _ in range(k)] for __ in range(k)]

    for i in range(k):
        for j in range(k):
            
            a11[i][j] = A[i][j]
            a12[i][j] = A[i][k + j]
            a21[i][j] = A[k + i][j]
            a22[i][j] = A[k + i][k + j]
            
            b11[i][j] = B[i][j]
            b12[i][j] = B[i][k + j]
            b21[i][j] = B[k + i][j]
            b22[i][j] = B[k + i][k + j]
            
    
    p1 = straussen_matrix(add_matrix(a11, a22, k), add_matrix(b11, b22, k), k)
    p2 = straussen_matrix(add_matrix(a21, a22, k), b11, k)
    p3 = straussen_matrix(a11, subtract_matrix(b12, b22, k), k)
    p4 = straussen_matrix(a22, subtract_matrix(b21, b11, k), k)
    p5 = straussen_matrix(add_matrix(a11, a12, k), b22, k)
    p6 = straussen_matrix(subtract_matrix(a21, a11, k), add_matrix(b11, b12, k), k)
    p7 = straussen_matrix(subtract_matrix(a12, a22, k), add_matrix(b21, b22, k), k)
    
    
    c11 = add_matrix (subtract_matrix(add_matrix(p1, p4, k), p5, k), p7, k)
    c12 = add_matrix(p3, p5, k)
    c21 = add_matrix(p2, p4, k)
    c22 = add_matrix (subtract_matrix(p1, p2, k), add_matrix(p3, p6, k), k)
    
    for i in range(k):
        for j in range(k):
            c[i][j] = c11[i][j]
            c[i][j + k] = c12[i][j]
            c[i + k][j] = c21[i][j]
            c[i + k][j + k] = c22[i][j]
    
    return c

if __name__ == "__main__":
    a = [[random.randint(-10, 10) for _ in range(20)] for _ in range(20)]
    b = [[random.randint(-10, 10) for _ in range(20)] for _ in range(20)]
    t1 = multiply_square_matrix(a, b)
    t2 = straussen_matrix(a, b, 20)
    
    if t1 == t2:
        print("Worked!")
    pprint.pprint(t1)
    print()
    pprint.pprint(t2)
    
    
    # Funciona até o 6
    