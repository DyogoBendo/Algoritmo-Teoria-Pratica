from math import inf

inversoes = 0
def merge(A, p, q, r):
    """
    :param A: Arranjo qualquer passado, A[p...q...r]
    :param p: indice inicial
    :param q: indice intermediario
    :param r: indice final
    :return: retorna um array ordenado
    """
    n1 = q - p + 1  # numero de posicoes ate o meio do array
    n2 = r - q  # numero de posicoes depois da metade do array
    L = []  # array esquerdo (elementos da primeira metade)
    R = []  # array direito (elementos da segunda metade)
    for i in range(n1):
        L.append(A[p + i])  # inserimos cada elemento da primeiro metade
    for j in range(n2):
        R.append(A[q+j + 1])  # inserimos cada elemento da segunda metade

    L.append(inf)
    R.append(inf)
    # colocamos dois elementos None no final

    i = 0
    j = 0
    global inversoes

    for k in range(p, r + 1):
        if L[i] < R[j]:
            # analisamos para caso chegamos no ultimo elemento
            # e analisamos quem é o menor
            A[k] = L[i]  # substituimos o valor do array original
            i += 1  # atribuimos mais um valor a i, avancamos uma posicao no array L
        else:
            inversoes += (n1 - i)
            A[k] = R[j]
            j += 1  # atribuimos mais um valor a j, avancamos uma posicao no array R


def merge_sort(A, p, r):
    if p < r:  # caso possua mais de um elemento
        q = (p + r) // 2  # dividimos o array na metade
        merge_sort(A, p, q)  # conquistamos metade de um array
        merge_sort(A, q + 1, r)  # conquistamos a outra metade
        merge(A, p, q, r)  # juntamos esses dois arrays


if __name__ == '__main__':
    teste2 = list(map(int, input('Insira uma lista\n').split(', ')))
    merge_sort(teste2, 0, len(teste2) - 1)

    print(inversoes)