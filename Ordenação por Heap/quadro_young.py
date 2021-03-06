from pprint import pprint

def extract_min(quadro):
    if quadro[0][0] == None:
        pass
    else:
        linha_original = len(quadro) - 1
        linha = linha_original
        coluna_original = len(quadro[0]) - 1
        coluna = coluna_original
        while quadro[linha][coluna] == None:                       
            if linha == 0:
                linha = linha_original
                coluna -= 1
            elif coluna == 0:
                coluna = coluna_original
                linha -= 1
            elif coluna != 0 and linha != 0:
                coluna -= 1         
        quadro[0][0], quadro[linha][coluna] = quadro[linha][coluna], None

        youngfy(quadro, 0, 0)

def youngfy(matriz, i, j, breakpoint = None):
    direita = [i, j + 1]
    baixo = [i + 1, j]
    
    linha = len(matriz) - 1
    coluna = len(matriz[0]) - 1                
    
    possible = True
    if breakpoint:
        if breakpoint[0] < baixo[0]:
            possible = False
        elif breakpoint[0] == baixo[0]:
            if breakpoint[1] <= baixo[1]:
                possible = False        
    
    if baixo[0] > linha or matriz[baixo[0]][baixo[1]] == None or not possible:
        menor = [i, j]            
    else:
        if matriz[baixo[0]][baixo[1]] < matriz[i][j]:
            menor = [baixo[0], baixo[1]]
        else:
            menor = [i, j]

    possible = True
    if breakpoint:
        if breakpoint[0] < direita[0]:
            possible = False
        elif breakpoint[0] == direita[0]:
            if breakpoint[1] <= direita[1]:
                possible = False        

    if direita[1] <= coluna and matriz[direita[0]][direita[1]] != None and possible:
        if matriz[direita[0]][direita[1]] < matriz[menor[0]][menor[1]]:
            menor = [direita[0], direita[1]]        
        
    if menor[0] != i or menor[1] != j:
        matriz[menor[0]][menor[1]], matriz[i] [j] = matriz[i][j], matriz[menor[0]] [menor[1]]
        youngfy(matriz, menor[0], menor[1], breakpoint)        
        

def young_insert(board, value):
    linha = len(board) - 1
    coluna = len(board[0]) - 1
    
    young_insert_order(board, value, linha, coluna)


def young_insert_order(board, value, linha, coluna):    
    while True:
        if linha - 1 < 0:
            break
        if board[linha - 1][coluna] == None:
            linha -= 1
        else:
            break
    
    while True:
        if coluna - 1 < 0:
            break
        if board[linha][coluna - 1] == None:
            coluna -= 1
        else:
            break
    
    while True:  
        maior = value
        pos_maior = [linha, coluna]       
        if linha - 1 >= 0:      
            if board[linha - 1][coluna] > maior:
                pos_maior = [linha - 1, coluna]
                maior = board[linha - 1][coluna]
        
        if coluna - 1>= 0:                        
            if board[linha][coluna - 1] > maior:
                pos_maior = [linha, coluna - 1]
                maior = board[linha][coluna - 1]            
                 
                
        if maior != value:
            board[linha][coluna], board[pos_maior[0]][pos_maior[1]] = board[pos_maior[0]][pos_maior[1]], board[linha][coluna]
            linha, coluna = pos_maior
        else: 
            board[linha][coluna] = value
            break                        


def young_sort(board):        
    for i in range(len(board) - 1, -1, -1):        
        for j in range(len(board[0]) - 1, -1, -1):              
            board[i][j], board[0][0] = board[0][0], board[i][j]                        
            youngfy(board, 0, 0, [i, j])        

# problema de como encontrar um número de O(m + n) não resolvido
    
if __name__ == "__main__":
    quadro_young = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ]
    
    extract_min(quadro_young)
    pprint(quadro_young)
    
    extract_min(quadro_young)
    pprint(quadro_young)
    
    extract_min(quadro_young)
    pprint(quadro_young)
    
    extract_min(quadro_young)
    pprint(quadro_young)
    
    young_insert(quadro_young, 1)
    pprint(quadro_young)
    
    young_insert(quadro_young, 3)
    pprint(quadro_young)
    
    young_insert(quadro_young, 10)
    pprint(quadro_young)
    
    young_insert(quadro_young, 11)
    pprint(quadro_young)
    
    print()
    young_sort(quadro_young)
    pprint(quadro_young)
    