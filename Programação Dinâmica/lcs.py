def lcs_length(x:str, y:str):        
    m = len(x)
    n = len(y)    

    b = [['0' for _ in range (n)] for __ in range(m)]
    c = [[0 for _ in range (n + 1)] for __ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "🡤"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "🡡"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "🡠"
    
    return c, b


def print_lcs(b, x, i, j):
    if i == -1 or j == -1:
        return
    if b[i][j]  == "🡤":
        print_lcs(b, x, i - 1, j - 1)
        print(x[i])
    elif b[i][j] == "🡡":
        print_lcs(b, x, i - 1, j)
    else:
        print_lcs(b, x, i, j - 1)


if __name__ == "__main__":
    x = "abcbdab"
    y = "bdcaba"    
    c, b = lcs_length(x, y)                
    print_lcs(b, x, len(x) - 1, len(y) - 1)

    t1 = '10010101'
    t2 = '010110110'
    c, b = lcs_length(t1, t2)                
    print_lcs(b, t1, len(t1) - 1, len(t2) - 1)

