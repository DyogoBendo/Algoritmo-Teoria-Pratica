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

def youngfy(matriz, i, j):
    direita = [i, j + 1]
    baixo = [i + 1, j]
    
    linha = len(matriz) - 1
    coluna = len(matriz[0]) - 1                
    
    if baixo[0] > linha or matriz[baixo[0]][baixo[1]] == None:
        menor = [i, j]
    else:
        if matriz[baixo[0]][baixo[1]] < matriz[i][j]:
            menor = [baixo[0], baixo[1]]
        else:
            menor = [i, j]

    if direita[1] <= coluna and matriz[direita[0]][direita[1]] != None:
        if matriz[direita[0]][direita[1]] < matriz[menor[0]][menor[1]]:
            menor = [direita[0], direita[1]]        
    
    if menor[0] != i or menor[1] != j:
        matriz[menor[0]][menor[1]], matriz[i] [j] = matriz[i][j], matriz[menor[0]] [menor[1]]
        youngfy(matriz, menor[0], menor[1])        
        


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
        