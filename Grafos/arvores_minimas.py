from collections import defaultdict


class Graph:
    def __init__(self) -> None:
        self.V = []
        self.graph = []
    
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
        self.addVertices(u)
        self.addVertices(v)
    

    def addVertices(self, v):
        if v not in self.V:
            self.V.append(v)

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])
    

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        
        else:
            parent[yroot] = xroot
            rank[xroot] += 1
    
    def KruskaMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item:item[2])

        parent = defaultdict()
        rank = defaultdict()

        for node in self.V:            
            parent[node] = node
            rank[node] = 0            
        
        while e < len(self.V) -1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
            
        minimumCost = 0
        print("Edges in the constrcut MST!")
        for u, v, w in result:
            minimumCost += w
            print(f'{u} -- {v}: {w}')
        print(f"Custo total: {minimumCost}")


if __name__ == '__main__':
    g = Graph()
    g.addEdge('a', 'b', 4)
    g.addEdge('a', 'h', 8)
    g.addEdge('b', 'c', 8)
    g.addEdge('b', 'h', 11)
    g.addEdge('c', 'd', 7)
    g.addEdge('c', 'i', 2)
    g.addEdge('c', 'f', 4)
    g.addEdge('d', 'e', 9)
    g.addEdge('d', 'f', 14)
    g.addEdge('e', 'f', 10)
    g.addEdge('f', 'g', 2)
    g.addEdge('g', 'i', 6)
    g.addEdge('g', 'h', 1)
    g.addEdge('h', 'i', 7)
    

    g.KruskaMST()