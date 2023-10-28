class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

def kruskal(graph, maximum=False):
    edges = []
    for u in range(len(graph)):
        for v in range(u + 1, len(graph)):
            if graph[u][v] is not None:
                edges.append((u, v, graph[u][v]))

    edges.sort(key=lambda x: x[2], reverse=maximum)
    mst = []
    uf = UnionFind(len(graph))

    for u, v, w in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, w))
            uf.union(u, v)

    return mst

# Ejemplo de uso
graph = [
    [None, 2, 4, None, None],
    [2, None, 3, 10, None],
    [4, 3, None, 7, 5],
    [None, 10, 7, None, 1],
    [None, None, 5, 1, None]
]

# Árbol de Expansión Mínima
minimum_spanning_tree = kruskal(graph)
print("Árbol de Expansión Mínima (Kruskal):", minimum_spanning_tree)

# Árbol de Expansión Máxima (simplemente invertimos los pesos)
maximum_spanning_tree = kruskal(graph, maximum=True)
print("Árbol de Expansión Máxima (Kruskal):", maximum_spanning_tree)
