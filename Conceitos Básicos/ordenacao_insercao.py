"""
    Método eficiente para a ordenação de poucos elementos
    Funciona de forma semelhante a ordenação de cartas de baralho, em que colocamos a carta menor da esquerda para a direita.
    Comparamos carta por carta, até encontrar o lugar adequado de uma carta.
"""


def insertion_sort(arranjo):
    for j in range(1, len(arranjo)):
        chave = arranjo[j]  # Pegamos a posição do próximo valor (a primeira carta do monte)
        i = j - 1  # pegamos a posição da ultima carta que está na nossa mão
        while i > -1 and arranjo[i] > chave:
            # se a carta que escolhemos pertence a nossa mão, ou seja, não seja -1
            # e que a carta que pegamos do monte seja menor que a que estamos comparando
            # Se essas duas condições são atendidas, entramos no loop
            arranjo[i + 1] = arranjo[i]
            # como existe uma carta menor que a que estamos comparando, a que temos 'pula' para a próxima posição

            i -= 1
            # Passamos a analisar agora a que compramos do monte com uma carta que é anterior a última

        arranjo[i + 1] = chave
        # adicionamos a carta comprada na frente da posição em que encontramos uma carta menor do que ela
    return arranjo


def insertion_sort_desc(arranjo):
    for j in range(1, len(arranjo)):
        chave = arranjo[j]
        i = j - 1
        while i > -1 and arranjo[i] < chave:
            arranjo[i + 1] = arranjo[i]
            i -= 1
        arranjo[i + 1] = chave
    return arranjo


if __name__ == '__main__':
    teste1 = [1, 2, 3, 4, 6, 5]
    teste2 = [1, 4, 2, 3, 9, 3]
    teste3 = [7, 5, 3, 1, 10]

    print(f'Exemplo 1: \n{teste1}')
    print(f'crescente: {insertion_sort(teste1)}\ndecrescente:{insertion_sort_desc(teste1)} ')
    print()

    print(f'Exemplo 2: \n{teste2}')
    print(f'crescente: {insertion_sort(teste2)}\ndecrescente:{insertion_sort_desc(teste2)} ')
    print()

    print(f'Exemplo 3: \n{teste3}')
    print(f'crescente: {insertion_sort(teste3)}\ndecrescente:{insertion_sort_desc(teste3)} ')
    print()

    entrada = list(input('Faça você mesmo um teste!(Separe os elementos por virgula)\n').split(', '))
    print(f'Ordenado: \ncrescente: {insertion_sort(entrada)}\ndecrescente: {insertion_sort_desc(entrada)}')