def pesquisar_valor(conjunto, v):
    valor_encontrado = None
    for i in range(len(conjunto)):
        if conjunto[i] == v:
            valor_encontrado = i + 1
            return valor_encontrado
    return valor_encontrado


if __name__ == '__main__':
    teste1 = [1, 2, 3, 4, 8]

    print(f'Vetor: {teste1}')

    print(f'Onde está o número 1? {pesquisar_valor(teste1, 1)}')
    print(f'Onde está o número 2? {pesquisar_valor(teste1, 2)}')
    print(f'Onde está o número 8? {pesquisar_valor(teste1, 8)}')
    print(f'Onde está o número 7? {pesquisar_valor(teste1, 7)}')

    teste2 = list(input('Insira um conjunto de numeros').split(', '))

    while True:
        valor = input('Insira um número (Digite S para sair)')
        if valor == 'S':
            break
        print(f'Index: {pesquisar_valor(teste2, valor)}')