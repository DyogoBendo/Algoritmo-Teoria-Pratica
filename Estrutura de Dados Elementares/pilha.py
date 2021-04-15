# Em Python, as listas funcionam como uma pilha já

class Pilha():
    def __init__(self, valores = []) -> None:
        self.valores = valores
        self.topo = len(valores) if valores else 0
    
    def is_empty(self):
        if not self.topo:
            return True
        else:
            return False
    
    def push(self, v):
        self.valores.append(v)
        self.topo += 1

    def pop(self):
        if self.is_empty():
            raise Exception("A pilha está vazia")
        else:
            self.topo -= 1
            self.valores.pop()
            

if __name__ == "__main__":
    pilha = [1, 2, 0, 7, 4]  # criamos uma pilha
    print("Nossa pilha: ", pilha)
    pilha.append(9)  # 9 é adicionado ao final
    print("Adicionamos 9 ao final da pilha: ", pilha)

    pilha.pop()  # removemos o último elemento (9)
    print("Removemos o 9 da pilha: ", pilha)
    pilha.pop()  # removemos o último elemento (4)
    print("Removemos o 4 da pilha: ", pilha)

    pilha_propria = Pilha(pilha)
    print("Criando nossa própria pilha: ", pilha_propria.valores)

    print("A pilha está vazia? ", pilha_propria.is_empty())

    pilha_propria.push(10)
    print("Adicionamos 10: ", pilha_propria.valores)

    pilha_propria.pop()
    print("Removemos o último elemento: ", pilha_propria.valores)
    pilha_propria.pop()
    print("Removemos o último elemento: ", pilha_propria.valores)
    pilha_propria.pop()
    print("Removemos o último elemento: ", pilha_propria.valores)
    pilha_propria.pop()
    print("Removemos o último elemento: ", pilha_propria.valores)
    pilha_propria.pop()
    print("Removemos o último elemento: ", pilha_propria.valores)

    print("Tentamos remover um elemento com a pilha vazia:")
    pilha_propria.pop()
    
