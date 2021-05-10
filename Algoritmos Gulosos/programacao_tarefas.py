class Node():    
    def __init__(self, d, w) -> None:        
        self.d = d
        self.w = w                
    
    def __eq__(self, other):
        return self.d == other.d
    def __lt__(self, other):
        return self.d < other.d
    def __gt__(self, other):
        return self.d > other.d

def greedy(M: list):
    A = []  
    cost = 0  
    t = 0  
    i = 0
    for x in M:
        i += 1
        size = len(A)
        t = x.d if x.d > t else t
        if t >= size + 1:
            a = f"a{i}"
            A.append(a)
        else:
            cost += x.w
    A.sort()
    return A, cost



if __name__ == "__main__":
    a1 = Node(4, 70)
    a2 = Node(2, 60)
    a3 = Node(4, 50)
    a4 = Node(3, 40)
    a5 = Node(1, 30)
    a6 = Node(4, 20)
    a7 = Node(6, 10)

    tarefas = [a1, a2, a3, a4, a5, a6, a7]

    to_do, cost = greedy(tarefas)
    print("Tarefas que precisam ser feitas:",to_do)
    print("Custo em detrimento das tarefas não feitas:",cost)
