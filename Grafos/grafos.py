from collections import defaultdict
from math import inf


class Node:
    def __init__(self, k) -> None:
        self.cor = 'branco'
        self.d = inf
        self.p = None
        self.k = k
        self.f = 0
    
    def __str__(self) -> str:
        p = ' Sem pai' if self.p is None else self.p.k
        txt = f'Valor: {self.k}, Cor: {self.cor}, Encontrado: {self.d}, Finalizado: {self.f}, Pai: {p}'
        return txt

class Graph:

    def __init__(self) -> None:        
        self.graph = defaultdict(list)
        self.vertices = []


    def addEdge(self, u:Node, v:Node):
        self.graph[u.k].append(v)
        self.addVertice(u)
        self.addVertice(v)
    
    def addVertice(self, v:Node):
        if v not in self.vertices:
            self.vertices.append(v)


    def bfs(self, s:Node): # breadth first search 
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
    

    def dfs(self): # depth first search
        global tempo
        tempo = 0
        for u in self.vertices:
            if u.cor == 'branco':
                self.__dfs_visit(u)
    

    def __dfs_visit(self, u:Node):
        global tempo
        tempo += 1
        u.d = tempo
        u.cor = 'cinzento'
        for v in self.graph[u.k]:
            if v.cor == 'branco':
                v.p = u
                self.__dfs_visit(v)
        u.cor = 'preto'
        tempo += 1
        u.f = tempo

    def dfs_topological(self):
        global tempo, lista_ligada
        tempo = 0
        lista_ligada = []        
        for u in self.vertices:
            if u.cor == 'branco':
                self.__dfs_topological_visit(u)
        return lista_ligada

    def __dfs_topological_visit(self, u:Node):
        global tempo, lista_ligada
        tempo += 1
        u.d = tempo
        u.cor = 'cinzento'
        for v in self.graph[u.k]:
            if v.cor == 'branco':
                v.p = u
                self.__dfs_topological_visit(v)
        u.cor = 'preto'
        lista_ligada.insert(0, u)        
        tempo += 1
        u.f = tempo

    def topological_sort(self):
        return self.dfs_topological()



if __name__ == '__main__':
    g = Graph()
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    g.addEdge(n0, n1)
    g.addEdge(n0, n2)
    g.addEdge(n1, n2)
    g.addEdge(n2, n0)
    g.addEdge(n2, n3)
    g.addEdge(n3, n3)
    g.addEdge(n0, n4)
    g.addEdge(n5, n6)
    
    # g.bfs(n2)
    # g.print_path(n2, n4)

    # g.dfs()
    l = g.topological_sort()
    for v in l:
        print(v)
        
        