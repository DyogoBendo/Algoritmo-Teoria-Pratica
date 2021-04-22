from math import inf
import time

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
    r = [- inf for _ in range(n + 1)]    
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n] >= 0:
        return r[n]
    q = 0 if n == 0 else - inf
    for i in range(n):
        q = max(q, p[i] + memoized_cut_rod_aux(p, n - (i + 1), r))
    r[n] = q  # salvamos a solução encontrada para não ser necessário recálculo

    return q


def bottom_up_cut_rod(p, n):
    r = [-inf for _ in range(n + 1)]
    r[0] = 0    

    for j in range(1, n + 1):
        q = -inf
        for i in range(0, j):            
            q = max(q, p[i] + r[j - (i + 1)])  # calculamos todos os subproblemas anteriores de n, antes de calcular o problema n
        r[j] = q    
    return r[n]


if __name__ == "__main__":
    precos = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 45, 50, 54, 60, 71, 80, 85, 87, 90, 99]
    start_time = time.time()
    print("Calculando de forma ingênua: ")    
    for i in range(0, 21):
        print(f"Com tamanho {i} a receita total é: R$ {cut_rod(precos, i):.2f}")
    print("--- %s seconds ---" % (time.time() - start_time))
        
    print("-" * 50)
    start_time = time.time()
    print("Calcula de cima para baixo: ")        
    for i in range(0, 21):
        print(f"Com tamanho {i} a receita total é: R$ {memoized_cut_rod(precos, i):.2f}")
    print("--- %s seconds ---" % (time.time() - start_time))

    print("-" * 50)        
    start_time = time.time()
    print("Calculando de baixo para cima: ")
    for i in range(0, 21):        
        print(f"Com tamanho {i} a receita total é: R$ {bottom_up_cut_rod(precos, i):.2f}")
    print("--- %s seconds ---" % (time.time() - start_time))