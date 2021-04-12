from random import randint

def counting_sort(A, B, k):  # ordenação utilizando contagem    
    C = [0 for _ in range(k + 1)]    
    for j in range(len(A)):                
        C[A[j]] += 1    # contamos quantos de cada elemento j aparecem   
    # C[i] possui o número de elementos igual a i        
    for i in range(1, k + 1): 
        C[i] += C[i - 1]
    # C[i] agora contém o número de elementos menores ou iguais a i    
    for j in range(len(A) - 1, -1, -1):                   
        B[C[A[j]] -1] = A[j]
        C[A[j]] -= 1

def count_min(A, k):
    C = [0 for _ in range(k + 1)]    
    for j in range(len(A)):                
        C[A[j]] += 1    # contamos quantos de cada elemento j aparecem   
    # C[i] possui o número de elementos igual a i        
    for i in range(1, k + 1): 
        C[i] += C[i - 1]
    return C        

def count_subarray(C, a, b):  # conta quantos elementos estão entre os valores a e b no array que foi processado em count_min
    if a == 0:
        return C[b]
    else:
        s = C[b] - C[a - 1]
        return s


if __name__ == "__main__":
    a = [randint(0, 20) for _ in range(20)]
    b = [0 for _ in range(20)]
    k = max(a)  # ideal é k ser <= que len(a)

    print("Vetor incial: ", a)
    counting_sort(a, b, k)
    print("Vetor ordenado: ", b)

    c = count_min(a, k)
    print(count_subarray(c, 10, 15))

