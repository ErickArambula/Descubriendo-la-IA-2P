import networkx as nx

def prim(graph):
    mst = nx.Graph()
    start_node = list(graph.nodes())[0]
    visited_nodes = set([start_node])

    while len(visited_nodes) < len(graph.nodes):
        possible_edges = []
        for node in visited_nodes:
            possible_edges.extend(graph.edges(node, data=True))
        possible_edges = [(u, v, d['weight']) for u, v, d in possible_edges if u in visited_nodes != v in visited_nodes]
        if not possible_edges:
            break
        min_edge = min(possible_edges, key=lambda x: x[2])
        visited_nodes.add(min_edge[1])
        mst.add_edge(*min_edge[:2], weight=min_edge[2])

    return mst

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_edge('A', 'B', weight=4)
G.add_edge('A', 'C', weight=2)
G.add_edge('B', 'C', weight=5)
G.add_edge('B', 'D', weight=10)
G.add_edge('C', 'D', weight=3)

minimum_spanning_tree = prim(G)

# Imprimir el Árbol de Expansión Mínima
for u, v, w in minimum_spanning_tree.edges(data=True):
    print(f'{u} - {v} : {w["weight"]}')
