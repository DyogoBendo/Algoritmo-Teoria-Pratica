
class Node():
    def __init__(self, folha=False) -> None:
        self.chave = []
        self.folha = False
        self.n = 0
        self.c = []


class BTree():
    def __init__(self, t) -> None:
        self.raiz = None
        self.t = t

    def b_tree_search(self, x, k):
        i = 0
        while i < x.n and k > x.chave[i]:
            i += 1
        if i <= x.n and k == x.chave[i]:
            return (x, i)
        elif x.folha:
            return None
        else:
            return self.b_tree_search(x.c[i], k)


    def b_tree_create(self):
        x = Node()
        x.folha = True
        x.n = 0        
        self.raiz = x

    

    def b_tree_split_child(self, x:Node, i):
        z = Node()
        y = x.c[i]
        z.folha = y.folha
        z.n = self.t - 1
        cz = [0 for _ in range(z.n)]
        fz = [0 for _ in range(z.n)]
        z.chave = cz
        z.c = fz
        for j in range(self.t - 1):
            z.chave[j] = y.chave[j + self.t]
        
        if not y.folha:
            for j in range(self.t):
                z.c[j] = y.c[j + self.t]
        
        y.n = self.t - 1
        for j in range(x.n - 1, i, -1):
            x.c[j + 1] = x.c[j]
        
        x.c.append(None)
        x.c[i + 1] = z
        try:
            x.c.remove(None)
        except:
            pass
        for j in range(x.n - 2, i - 1, -1):
            x.chave[j + 1] = x.chave[j]
        
        x.chave.append(None)
        x.chave[i] = y.chave[self.t]
        try:
            x.chave.remove(None)
        except:
            pass
        x.n += 1

    def b_tree_insert(self, k):
        r = self.raiz
        if r.n == (2 *self.t) - 1:
            s = Node()
            self.raiz = s
            s.folha = False
            s.n = 0
            s.c.append(None)
            s.c[0] = r
            self.b_tree_split_child(s, 0)
            self.b_tree_insert_nonfull(s, k)
        else:
            self.b_tree_insert_nonfull(r, k)

    def b_tree_insert_nonfull(self, x:Node, k):
        i = x.n - 1
        if x.folha:
            x.chave.append(None)
            while i >= 0 and k < x.chave[i]:
                x.chave[i + 1] = x.chave[i]
                i -= 1
            x.chave[i + 1] = k
            x.n += 1
        else:                        
            print(i)
            while i >= 0 and k < x.chave[i]:
                i -= 1
            i += 1
            if x.c[i].n == 2 * (self.t) - 1:
                self.b_tree_split_child(x, i)
                if k > x.chave[i]:
                    i += 1                
            self.b_tree_insert_nonfull(x.c[i], k)

    def print_tree(self, x:Node, i=0):
        print(f"Nível {i}", end=':')
        for k in x.chave:
            print(str(k), end=' ')
        print()
        i += 1
        for c in x.c:
            self.print_tree(c, i)    

if __name__ == "__main__":
    btree = BTree(3)
    btree.b_tree_create()
    btree.b_tree_insert('F')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('S')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('Q')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('K')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('C')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('L')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('H')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('T')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('V')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('W')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('M')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('R')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('N')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('P')
    btree.print_tree(btree.raiz)
    btree.b_tree_insert('A')
    btree.b_tree_insert('B')
    btree.b_tree_insert('X')
    btree.b_tree_insert('Y')
    btree.b_tree_insert('D')
    btree.b_tree_insert('Z')
    btree.b_tree_insert('E')

    btree.print_tree(btree.raiz)
