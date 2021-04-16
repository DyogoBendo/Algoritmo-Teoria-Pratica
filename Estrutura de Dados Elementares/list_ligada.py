class Node():
    def __init__(self, v, anterior = None, proximo = None) -> None:
        self.anterior = anterior
        self.proximo = proximo
        self.chave = v
    
    def __str__(self) -> str:
        return f'Chave: {self.chave}, anterior: {self.anterior}, proximo: {self.proximo}'


class Lista_Duplamente_Ligada():
    def __init__(self) -> None:        
        self.nulo = Node(None) 
        self.nulo = Node(None, self.nulo, self.nulo)
    
    def list_insert(self, v):
        v.proximo = self.nulo.proximo                  
        self.nulo.proximo.anterior = v    # anterior do primeiro elemento        
        self.nulo.proximo = v  # novo primeiro elemento 
        v.anterior = self.nulo        
                     

    def list_search(self, v):
        x = self.nulo.proximo
        while x != self.nulo and x.chave != v:
            x = x.proximo
        
        return x

    def list_delete(self, v):
        v.anterior.proximo = v.proximo
        v.proximo.anterior = v.anterior
        v = None
    
    def __str__(self) -> str:
        txt = ''
        x = self.nulo.proximo        
        while x != self.nulo:
            txt += str(x) + '\n'
            x = x.proximo
            print(x.proximo)
        
        return txt


if __name__ == "__main__":
    node1 = Node(6)
    node2 = Node(7)
    node3 = Node(1)
    node4 = Node(9)
    print(node3)

    lista = Lista_Duplamente_Ligada()

    lista.list_insert(node1)
    lista.list_insert(node2)
    lista.list_insert(node3)
    lista.list_insert(node4)
    # print(lista)

    # print(lista.list_search(1))