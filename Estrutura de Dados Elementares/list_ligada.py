class Node():
    def __init__(self, v, anterior = None, proximo = None) -> None:
        self.anterior = anterior
        self.proximo = proximo
        self.chave = v
    


class Lista_Duplamente_Ligada():
    def __init__(self) -> None:        
        self.inicio = None
        self.fim = None        
    
    def list_insert(self, v):
        v.proximo = self.inicio                
        v.anterior = None
        if self.inicio:
            self.inicio.anterior = v    
        else:
            self.fim = v            
        self.inicio = v                            

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
