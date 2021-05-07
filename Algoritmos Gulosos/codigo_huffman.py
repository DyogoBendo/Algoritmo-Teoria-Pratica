class Fila():
    def __init__(self, fila = []) -> None:
        self.fila = fila
        self.inicio = fila[0] if fila else 0
        self.fim = len(fila) if fila else 0
    
    def enqueue(self, x):
        self.fila.append(x)        
        self.fim += 1
    
    def dequeue(self):            
        if self.fim > 0:
            self.fim -= 1
            return self.fila.pop(0)
        else:
            raise Exception("A fila já está vazia")

class Node():    
    def __init__(self, v = None, freq=0) -> None:
        self.left = None
        self.right = None
        self.freq = freq
        self.v = v
    
    def __str__(self) -> str:
        txt = f"Valor: {self.v}, Frequência: {self.freq}"
        return txt

def huffman(C) -> Node:
    n = len(C)
    Q = Fila(C)
    for _ in range(n - 1):      
        z = Node()
        z.left = x = Q.dequeue()
        z.right = y = Q.dequeue()
        z.freq = x.freq + y.freq
        Q.enqueue(z)
    return Q.dequeue()  


if __name__ == "__main__":    
    a = Node("a", 45)
    b = Node("b", 13)
    c = Node("c", 12)
    d = Node("d", 16)
    e = Node("e", 9)
    f = Node("f", 5)    
    alfabeto = [a, b, c, d, e, f]
    raiz = huffman(alfabeto)
    print(raiz, raiz.left, raiz.right)

