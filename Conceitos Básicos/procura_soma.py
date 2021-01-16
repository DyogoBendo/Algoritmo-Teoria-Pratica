def procura_soma(vetor, soma):
    for i in range(len(vetor)):
        encontrado = encontra_soma(i, vetor, soma, i + 1, len(vetor) - 1)
        if encontrado == 1:
            return 'Encontrado!'
    return 'Não foi encontrado :('


def encontra_soma(i, vetor, soma, inicio, fim):
    if inicio > fim:
        return -1
    else:
        meio = (inicio + fim) // 2
        if soma == vetor[i] + vetor[meio]:
            return 1
        if soma > vetor[i] + vetor[meio]:
            return encontra_soma(i, vetor, soma, meio + 1, fim)
        else:
            return encontra_soma(i, vetor, soma, inicio, meio - 1)


if __name__ == '__main__':
    entrada = list(map(int, input('Insira um vetor: ').split(', ')))
    soma = int(input('Insira uma soma: '))
    print(procura_soma(entrada, soma))