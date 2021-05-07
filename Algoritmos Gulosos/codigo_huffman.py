from ..utils.binary_tree import ArvoreBinaria
from ..utils.queue import Fila

class Node():    
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.freq = 0

def huffman(C):
    n = len(C)
    Q = Fila(C)
    for _ in range(n - 1):      
        z = Node()
        z.left = x = Q.dequeue()
        z.right = y = Q.dequeue()
        z.freq = x.freq + y.freq
        Q.enqueue(z)
    return Q.dequeue()  

