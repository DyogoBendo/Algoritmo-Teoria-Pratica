from collections import defaultdict
from math import inf


class Node:
    def __init__(self, k) -> None:
        self.cor = 'branco'
        self.d = inf
        self.p = None
        self.k = k

class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)


    def addEdge(self, u:Node, v:Node):
        self.graph[u.k].append(v)


    def bfs(self, s:Node):
        s.cor = 'cinza'        
        s.d = 0        
        queue = []
        queue.append(s)        
        while queue:
            u = queue.pop(0)            
            for i in self.graph[u.k]:
                if i.cor == 'branco':
                    i.cor = 'cinzento'
                    i.d = u.d + 1
                    i.p = u
                    queue.append(i) 
            u.cor = 'preto'                    
    
    def print_path(self, s:Node, v:Node):  # imprime um caminho de s até v, sendo s a raiz da arvore de busca em largura
        if v == s:
            print(s.k)
        elif v.p == None:
            print("Não existe nenhum caminho entre esses dois vértices")
        else:
            self.print_path(s, v.p)
            print("↓")
            print(v.k)
    
if __name__ == '__main__':
    g = Graph()
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    g.addEdge(n0, n1)
    g.addEdge(n0, n2)
    g.addEdge(n1, n2)
    g.addEdge(n2, n0)
    g.addEdge(n2, n3)
    g.addEdge(n3, n3)
    g.addEdge(n0, n4)

    print ("Following is Breadth First Traversal"
                    " (starting from vertex 2)")
    g.bfs(n2)
    g.print_path(n2, n4)
        