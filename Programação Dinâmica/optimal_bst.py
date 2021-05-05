from pprint import pprint
from math import inf
from utils import bst
from typing import List

def optimal_bst(p, q, n):
    e = [['no' for j in range(n)] for i in range(n + 1)]
    w = [['no' for j in range(n )] for i in range(n + 1)]
    raiz = [['no' for j in range(n)] for i in range(n)]

    for i in range(1, n + 1):        
        e[i][i - 1] = q[i - 1]
        w[i][i - 1] = q[i - 1]
    for l in range(1, n):
        for i in range(1, n - l + 1):
            j = i + l - 1
            e[i][j] = inf
            w[i][j] = w[i][j - 1] + p[j] + q[j]

            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                if t < e[i][j]:
                    e[i][j] = t
                    raiz[i][j] = r    
    raiz.pop(0)
    e.pop(0)
    return e, raiz


def helper_optimal_bst(raiz:List[List[int]], order: list, begin:int, end:int):
    if begin >= end or end == 0:
        return

    print(begin, end)
    s = raiz[begin][end]    
    if s == begin:
        order.append(s)
        helper_optimal_bst(raiz, order, begin + 1, end)
    elif s == end:
        order.append(s)
        helper_optimal_bst(raiz, order, begin, end - 1)
    else:
        order.append(s)        
        helper_optimal_bst(raiz, order, begin, s - 1)
        helper_optimal_bst(raiz, order, s + 1, end)

def contruct_optimal_bst(raiz:List[List[int]]) -> list:    
    order = []
    root = raiz[0][-1]
    order.append(root)

    helper_optimal_bst(raiz, order, 0, root - 1)
    helper_optimal_bst(raiz, order, root, len(raiz[0]) - 1)

    return order
        
        



if __name__ == "__main__":
    p = [0, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    n = 6
    e, raiz = optimal_bst(p, q, n)

    print("-"*60)
    pprint(e)
    print("-"*60)
    pprint(raiz)

    root = raiz[0][-1]
    print(root)

    o = contruct_optimal_bst(raiz)
        
    bst = bst.BST()    
    for r in o:
        bst.insert(r)        
    bst.prettyPrint()    


    


    