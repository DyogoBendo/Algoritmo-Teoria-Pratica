from collections import defaultdict
from math import inf


class Heap():
    def __init__(self) -> None:
        self.array = []
        self.size = 0
        self.pos = []
    

    def newMinHeapNode(self, v, dist):
        minHeapNode = [v, dist]
        return minHeapNode
    

    def swapMinHeapNode(self, a, b):        
        self.array[a], self.array[b] = self.array[b], self.array[a]


    def minHeapfy(self, idx):
        smallest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < self.size and self.array[left][1] < self.array[smallest][1]:
            smallest = left
        if right < self.size and self.array[right][1] < self.array[smallest][1]:
            smallest = right
        
        if smallest != idx:
            self.pos[self.array[smallest][0]] = idx            
            self.pos[self.array[idx][0]] = smallest

            self.swapMinHeapNode(smallest, idx)
            self.minHeapfy(smallest)


    def extractMin(self):
        if self.isEmpty():
            return
        
        root = self.array[0]
        lastNode = self.array[self.size - 1]
        self.array[0] = lastNode

        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size -1

        self.size -= 1
        self.minHeapfy(0)

        return root
    

    def isEmpty(self):
        return True if self.size == 0 else False
    

    def decreaseKey(self, v, dist):
        i = self.pos[v]
        self.array[i][1] = dist

        while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]:
            self.pos[self.array[i][0]] = (i - 1)/2
            self.pos[self.array[(i - 1) / 2][0]] = i
            self.swapMinHeapNode(i, (i -1)/2)
            i = (i - 1)/2
    
    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


class PrimGraph():
    def __init__(self, V) -> None:
        self.V = V
        self.graph = defaultdict(list)
    

    def addEdge(self, src, dest, weight):
        newNode = [dest, weight]
        self.graph[src].insert(0, newNode)

        newNode = [src, weight]
        self.graph[dest].insert(0, newNode)


    def primMST(self):
        V = self.V
        key = []
        parent = []
        minHeap = Heap()
        for v in range(V):
            parent.append(-1)
            key.append(inf)
            minHeap.array.append(minHeap.newMinHeapNode(v, key[v]))
            minHeap.pos.append(v)
        

        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0])
  
        # Initially size of min heap is equal to V
        minHeap.size = V;
  
        # In the following loop, min heap contains all nodes
        # not yet added in the MST.
        while minHeap.isEmpty() == False:
  
            # Extract the vertex with minimum distance value
            newHeapNode = minHeap.extractMin()
            u = newHeapNode[0]
  
            # Traverse through all adjacent vertices of u 
            # (the extracted vertex) and update their 
            # distance values
            for pCrawl in self.graph[u]:
  
                v = pCrawl[0]
  
                # If shortest distance to v is not finalized 
                # yet, and distance to v through u is less than
                # its previously calculated distance
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]:
                    key[v] = pCrawl[1]
                    parent[v] = u
  
                    # update distance value in min heap also
                    minHeap.decreaseKey(v, key[v])


class KruskalGraph:
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
    g = KruskalGraph()
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