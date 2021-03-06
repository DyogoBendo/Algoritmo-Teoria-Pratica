class Node():    
    def __init__(self, d, w, i) -> None:        
        self.d = d
        self.w = w                
        self.i = i

    def __str__(self) -> str:        
        return str(self.i)

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
    for x in M:        
        size = len(A)
        t = x.d if x.d > t else t
        if t >= size + 1:            
            A.append(x)
        else:
            cost += x.w
    A.sort()
    return A, cost



if __name__ == "__main__":
    a1 = Node(4, 70, 1)
    a2 = Node(2, 60, 2)
    a3 = Node(4, 50, 3)
    a4 = Node(3, 40, 4)
    a5 = Node(1, 30, 5)
    a6 = Node(4, 20, 6)
    a7 = Node(6, 10, 7)

    tarefas = [a1, a2, a3, a4, a5, a6, a7]

    to_do, cost = greedy(tarefas)
    txt = ""
    for x in to_do:
        txt += str(x.i) + " "
    print("Tarefas que precisam ser feitas:", txt)
    print("Custo em detrimento das tarefas não feitas:",cost)
