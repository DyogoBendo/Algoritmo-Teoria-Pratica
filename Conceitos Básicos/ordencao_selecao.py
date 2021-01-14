def ordenacao_selecao(arranjo):
    for i in range(len(arranjo) - 1):
        posicao = arranjo[i]
        menor = posicao
        posicao_menor = i
        for j in range(i + 1, len(arranjo)):
            if arranjo[j] < menor:
                menor = arranjo[j]
                posicao_menor = j
        arranjo[i] = menor
        arranjo[posicao_menor] = posicao
    return arranjo


if __name__ == '__main__':
    teste1 = [1, 5, 3, 7, 4]
    teste2 = [2, 1, 9, 3, 0]

    print(ordenacao_selecao(teste1))
    print(ordenacao_selecao(teste2))

    teste = list(map(int, input('Insira a sua lista\n').split(', ')))
    print(ordenacao_selecao(teste))
