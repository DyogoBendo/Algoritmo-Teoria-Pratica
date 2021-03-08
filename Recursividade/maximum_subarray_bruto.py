import math

def maximum_subarray(A):
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

    return best_soma, begin, end

# Função de tempo O(n^2)


if __name__ == '__main__':
    entrada = list(map(int, input().split(', ')))
    print(maximum_subarray(entrada))