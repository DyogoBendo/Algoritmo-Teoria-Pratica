class Node():
    def __init__(self, v, anterior = None, proximo = None) -> None:
        self.anterior = anterior
        self.proximo = proximo
        self.chave = v
    
    def __str__(self) -> str:
        return f'Chave: {self.chave}, Anterior: {self.anterior}, Próximo: {self.proximo}'


class Lista_Duplamente_Ligada():
    def __init__(self) -> None:        
        self.inicio = None
        self.size = 0
    
    def list_insert(self, v):
        if self.inicio:
            pointer = self.inicio
            while pointer.proximo:
                pointer = pointer.proximo
            pointer.proximo = Node(v, pointer)
        else:
            self.inicio = Node(v)
        
        self.size += 1

    def list_search(self, v):
        x = self.inicio
        while x and x.chave != v:
            x = x.proximo
        
        return x

    def list_delete(self, v):
        if v.anterior:
            v.anterior.proximo = v.proximo
        else:
            self.inicio = v.proximo

        if v.proximo:
            v.proximo.anterior = v.anterior
        else:
            self.fim = v.anterior

        v = None


    def __len__(self):
        return self.size
    

    def __getitem__(self, index):
        pointer = self.inicio
        for _ in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("O index está fora de alcance")
        if pointer:
            return pointer
        raise IndexError("O index está fora de alcance")



