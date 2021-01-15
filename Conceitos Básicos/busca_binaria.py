def pesquisa_binaria(vetor_ordenado, valor_procurado, inicio, fim):
    if inicio > fim:
        return -1
    else:
        meio = (inicio + fim) // 2
        if valor_procurado == vetor_ordenado[meio]:
            return meio
        if valor_procurado < vetor_ordenado[meio]:
            return pesquisa_binaria(vetor_ordenado, valor_procurado, inicio, meio - 1)
        else:
            return pesquisa_binaria(vetor_ordenado, valor_procurado, meio + 1, fim)


if __name__ == '__main__':
    entrada = list(map(int, input('Insira um vetor\n').split(', ')))
    entrada.sort()
    fim = len(entrada) - 1

    while True:
        sim_nao = input('Deseja procurar um valor? (s/n)  ')
        if sim_nao == 's':
            valor_procurado = int(input('Qual valor procura?\n'))
            print(f'Posição dele: {pesquisa_binaria(entrada, valor_procurado, 0, fim)}')
        else:
            break
