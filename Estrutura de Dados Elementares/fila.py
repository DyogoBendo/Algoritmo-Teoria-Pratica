class Fila():
    def __init__(self, fila = []) -> None:
        self.fila = fila
        self.inicio = fila[0] if fila else 0
        self.fim = fila[-1] if fila else 0
    
    def enqueue(self, x):
        self.fila.append(x)        
        self.fim += 1
    
    def dequeue(self):            
        if self.fim > 0:
            self.fim -= 1
            return self.fila.pop(0)
        else:
            raise Exception("A fila já está vazia")


if __name__ == "__main__":
    fila = Fila([1, 4, 5, 2, 7])

    print("Fila inicialmente: ", fila.fila)
    
    for i in range(3):        
        print("Removemos elemento inicial: ", fila.dequeue())
        print(fila.fila)

    print("-"*15)
    fila.enqueue(10)
    fila.enqueue(19)

    print("Adicionamos dois elementos no final: ", fila.fila)

    print("Removemos o elemento inicial: ", fila.dequeue())

    print("Fila ao final: ", fila.fila)

    
    

