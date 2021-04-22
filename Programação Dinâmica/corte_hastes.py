from math import inf

# Resolução não dinâmica

def cut_rod(p, n):  # p é a tabela de preços, e n o tamanho do corte máximo
    if n == 0:
        return 0
    q = - inf
    for i in range(n):        
        q = max(q, p[i] + cut_rod(p, n - (i + 1)))
    return q

# Essa solução é ineficiente, pois chamamos os mesmos parâmetros diversas vezes


# Programação dinâmica de cima para baixo
def memoized_cut_rod(p, n):
    r = [- inf for _ in range(n)]    
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = 0 if n == 0 else - inf
    for i in range(n):
        q = max(q, p[i] + memoized_cut_rod_aux(p, n - i, r))
    r[n] = q  # salvamos a solução encontrada para não ser necessário recálculo

    return q


if __name__ == "__main__":
    precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]    
    for i in range(1, 11):
        print(f"Com tamanho {i} a receita total é: R$ {cut_rod(precos, i):.2f}")
