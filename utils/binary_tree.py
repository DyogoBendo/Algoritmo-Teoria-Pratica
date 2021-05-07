from random import randint

class Node():
    def __init__(self, v) -> None:        
        self.chave = v
        self.left = None
        self.right = None
    
    def __str__(self) -> str:
        esquerda = self.left.chave if self.left else None
        direita = self.right.chave if self.right else None
        return f'Chave: {self.chave}, Esquerda: {esquerda}, Direita: {direita}'   

class ArvoreBinaria():
    def __init__(self, r) -> None:
        self.raiz = r
             
    def visitar_elementos(self, e):
        if e:            
            self.visitar_elementos(e.left)
            self.visitar_elementos(e.right)            
            print(e)
    
    def visitar_nao_recursivo(self):
        s = []
        n = self.raiz        
        while True:                        
            if not n:
                if len(s) > 0:
                    popped = s.pop()
                    print(popped)
                    n = popped.right
                else:
                    break
            else:
                s.append(n)            
                n = n.left

    

if __name__ == "__main__":
    a = Node(randint(0, 50))
    print("A: ", a)
    b = Node(randint(0, 50))
    print("B: ", b)
    c = Node(randint(0, 50))
    print("C: ", c)
    d = Node(randint(0, 50))
    print("D: ", d)
    e = Node(randint(0, 50))
    print("E: ", e)

    a.left = b
    a.right = c
    b.left = d 
    c.right = e

    print("-"*20)
    print("Arvore:")
    arvore = ArvoreBinaria(a)
    arvore.visitar_elementos(a)
    print("-"*20)
    arvore.visitar_nao_recursivo()
    