from math import inf
from random import randint


def linear_maximum_subarray(A):
    max_subarry = actual_max_subarray = A[0]
    begin = end = b = 0    
    for j in range(1, len(A)):
        actual_max_subarray = max(A[j], actual_max_subarray + A[j])
            
        if actual_max_subarray > max_subarry:
            max_subarry = actual_max_subarray
            end = j
            begin = b
        
        if actual_max_subarray < 0:
            b = j + 1
        
    
    return begin, end, max_subarry
        

if __name__ == "__main__":
    lista =[randint(-10, 10) for i in range(10)]
    
    print(lista)
    print(linear_maximum_subarray(lista))