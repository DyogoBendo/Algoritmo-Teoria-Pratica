import math


def find_max_crossing_subarray(A, low, mid, high):
    soma_left = - math.inf
    soma = 0
    
    for i in range(mid, low - 1, -1):
        soma += A[i]
        if soma > soma_left:
            soma_left = soma
            max_left = i
            
    soma_right = - math.inf
    soma = 0
    
    for i in range(mid + 1, high + 1):
        soma +=  A[i]
        if soma >= soma_right:
            soma_right = soma
            max_right = i
    
    return (max_left, max_right, soma_left + soma_right)


def maximum_subarray(A, low, high):
    if low == high:
        return (low, high, A[low])
    else:
        mid = (low + high ) // 2
        left_low, left_high, left_sum = maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        
        if cross_sum <= left_sum >= right_sum:
            return (left_low, left_high, left_sum)
        elif cross_sum <= right_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
 
def maximum_subarray_fused(A, low, high):
    if high - low <= 50:
        tamanho_vetor = len(A)
        best_soma = - math.inf
        for i in range(tamanho_vetor):
            soma = 0
            for j in range(i, tamanho_vetor):
                soma += A[j]
                if soma > best_soma:
                    best_soma = soma
                    begin = i
                    end = j

        return begin, end, best_soma
    else:
        mid = (low + high ) // 2
        left_low, left_high, left_sum = maximum_subarray(A, low, mid)
        right_low, right_high, right_sum = maximum_subarray(A, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)
        
        if cross_sum <= left_sum >= right_sum:
            return (left_low, left_high, left_sum)
        elif cross_sum <= right_sum:
            return (right_low, right_high, right_sum)
        else:
            return (cross_low, cross_high, cross_sum)
    
            
if __name__ == "__main__":
    a = list(map(int, input().split(", ")))
    print(maximum_subarray(a, 0, len(a) - 1))