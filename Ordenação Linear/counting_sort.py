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


if __name__ == "__main__":
    a = [randint(0, 20) for _ in range(20)]
    b = [0 for _ in range(20)]
    k = max(a)  # ideal é k ser <= que len(a)

    print("Vetor incial: ", a)
    counting_sort(a, b, k)
    print("Vetor ordenado: ", b)

