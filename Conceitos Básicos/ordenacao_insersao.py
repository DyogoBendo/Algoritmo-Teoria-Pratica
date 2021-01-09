"""
    Método eficiente para a ordenação de poucos elementos
    Funciona de forma semelhante a ordenação de cartas de baralho, em que colocamos a carta menor da esquerda para a direita.
    Comparamos carta por carta, até encontrar o lugar adequado de uma carta.
"""


def insertion_sort(arranjo):
    for j in range(1, len(arranjo)):
        chave = arranjo[j]
        i = j - 1
        while i > 0 and arranjo[i] > chave:
            arranjo[i + 1] = arranjo[i]
            i -= 1
        arranjo[i + 1] = chave
    return arranjo


if __name__ == '__main__':
    teste1 = [1, 2, 3, 4, 6, 5]
    teste2 = [1, 4, 2, 3, 9, 3]
    teste3 = [1, 5, 3, 1, 10]

    print(f'Exemplo 1: \n{teste1}')
    print(insertion_sort(teste1))
    print()

    print(f'Exemplo 2: \n{teste2}')
    print(insertion_sort(teste2))
    print()

    print(f'Exemplo 3: \n{teste3}')
    print(insertion_sort(teste3))
    print()

    entrada = list(map(int, input('Faça você mesmo um teste!(Separe os elementos por virgula)\n').split(', ')))
    print(f'Ordenado: {insertion_sort(entrada)}')