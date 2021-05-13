class Node():
    def __init__(self, k) -> None:
        self.chave = k
        self.grau = 0
        self.p = None
        self.filho = None
        self.marca = False
        self.anterior = None
        self.proximo = None

    
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


class Fib_Heap():
    def __init__(self) -> None:
        self.n = 0
        self.min = None
        self.raizes = Lista_Duplamente_Ligada()
    
    def insert(self, x):
        self.raizes.list_insert(x)
        if self.min is None:
            self.min = x 
        elif x < self.min:
            self.min = x
        self.n += 1
    
    @staticmethod
    def union(h1, h2):
        h = Fib_Heap()
        h.min = h1.min    

        h1.raizes.list_insert(h2.raizes.inicio)
        h.raizes = h1.raizes

        if h2.min is not None:
            if h1.min is None:
                h.min =  h2.min
            elif h2.min < h1.min:
                h.min = h2.min
        h.n = h1.n + h2.n
        return h
    def extract_min(self):
        z = self.min
        if z is not None:
            for x in z.filho:
                self.raizes.list_insert(x)
                x.p = None
            self.raizes.list_delete(z)

            if z.proximo is None:
                self.min = None
            else:
                self.min = z.proximo            
                self.__consolidate()
            self.n -= 1
        return z
    
    def __consolidate(self):
        a = [None for _ in range(self.n)]
        for w in self.raizes:
            x = w
            d = x.grau
            while a[d] != None:
                y = a[d]
                if x.chave > y.chave:
                    x, y = y, x
                    self.__fib_heap_link(y, x)
                    a[d] = None
                    d += 1
            a[d] = x 
        self.min = None
        for i in range(self.n):
            if a[i] != None:
                if self.min == None:
                    self.raizes = Lista_Duplamente_Ligada()
                    self.raizes.list_insert(a[i])
                else:
                    self.raizes.list_insert(a[i])
                    if a[i].chave < self.min.chave:
                        self.min = a[i]
    
    def __fib_heap_link(self, y:Node, x:Node):
        self.raizes.list_delete(y)
        x.grau += 1
        x.filho.append(y)
        y.marca = False
                