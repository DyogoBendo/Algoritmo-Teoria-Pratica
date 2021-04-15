class Deque():
    def __init__(self, values = []) -> None:
        self.values = values
        self.inicio = 0
        self.fim = len(values) if values else 0
    
    def adiciona_fim(self, v):
        self.values.append(v)
    
    def adiciona_inicio(self, v):
        self.values.insert(0, v)

    def remove_inicio(self):
        self.values.pop(0)
    
    def remove_fim(self):
        self.values.pop()
    
