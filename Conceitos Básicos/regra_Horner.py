def regra_horner(x, coeficientes):
    y = 0
    i = len(coeficientes) - 1

    while i >= 0:
        y = coeficientes[i] + (x * y)
        i -= 1

    return y


def algoritmo_ingenuo(x, coeficientes):
    y = 0
    for i in range(len(coeficientes) - 1, -1, -1):
        valor_exponente = 1
        for j in range(i):
            valor_exponente *= x
        y += coeficientes[i] * valor_exponente
    return y


if __name__ == '__main__':
    coeficientes = list(map(int, input('Insira os coeficientes de um polinomio: ').split(', ')))
    lista_coeficientes = ''
    for i in range(len(coeficientes)):
        if coeficientes[i] == 0:
            continue
        if i > 0:
            lista_coeficientes += ' + '
        if coeficientes[i] != 1:
            lista_coeficientes += f'{coeficientes[i]}'
        else:
            pass
        if len(coeficientes) - i - 1 > 1:
            lista_coeficientes += f'(x^{len(coeficientes) - i - 1})'
        elif len(coeficientes) - i - 1 == 1:
            lista_coeficientes += f'(x)'
        else:
            pass
    print(f'Polinomio: {lista_coeficientes}')
    coeficientes.reverse()
    x = int(input('Insira um valor de x: '))
    print(f'Resultado: {regra_horner(x, coeficientes)}')
    print(f'Resultado: {algoritmo_ingenuo(x, coeficientes)}')

