from math import inf


def matrix_chain_order(p):
    # p -> lista das dimensões das matrizes em ordem sem repetição
    n = len(p) - 1
    m = [[0 for _ in range(n)] for _ in range(n)]
    s = [[0 for _ in range(n)] for _ in range(n)]
    for l in range(2, n + 1):  # tamanho de cada encadeamento
        for i in range(1, n - l + 2):  # início
            j = i + l - 1  # fim
            m[i - 1][j - 1] = inf
            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + (p[i - 1] * p[k] * p[j])
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 1] = k

    return m, s


def print_optimal_parens(s, i, j):            
    if i == j:
        print (f"A{i + 1}", end="")
    else:        
        
        print("( ", end="")
        print_optimal_parens(s, i, s[i][j] - 1)
        print_optimal_parens(s, s[i][j], j)
        print(" )", end="") 


if __name__ == "__main__":
    p = (30, 35, 15, 5, 10, 20, 25)

    a, b = matrix_chain_order(p)

    t = len(a[0])
    for i in range(t - 1):
        for j in range(i + 1,t):
            print(f"Se multiplicarmos as matrizes de {i + 1} até a matriz {j + 1} realizaremos {a[i][j]} operações")
            print(f"A ordem das multiplicações deve ser: (matriz {i + 1} até a matriz {b[i][j]}) X (matriz {b[i][j] + 1} até a matriz {j + 1}) \n")            

        if i < t - 2:
            print("\n")
    
    print_optimal_parens(b, 1, 4)
    print( "\n" + "*" * 50)

    p = (5, 10, 3, 12, 5, 50, 6)    
    a, s = matrix_chain_order(p)    
    print_optimal_parens(s, 0, 5)
    print()