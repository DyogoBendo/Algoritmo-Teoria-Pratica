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

    # Consideramos nesse caso, em que temos apenas números negativos, que a melhor soma é um array vazio, que vale 0. 
    if soma < 0:
        begin = -1
        end = -1
        best_soma = 0
    return begin, end, best_soma

# Função de tempo O(n^2)


if __name__ == '__main__':
    entrada = list(map(int, input().split(', ')))
    print(maximum_subarray(entrada))