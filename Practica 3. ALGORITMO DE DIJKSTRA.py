import sys

class Grafo:
    def __init__(self):
        self.nodos = set()
        self.aristas = {}
    
    def agregar_nodo(self, valor):
        self.nodos.add(valor)
        self.aristas[valor] = []
    
    def agregar_arista(self, desde, hacia, peso):
        self.aristas[desde].append((hacia, peso))
    
def dijkstra(grafo, inicio):
    distancia = {nodo: float('infinity') for nodo in grafo.nodos}
    distancia[inicio] = 0
    nodos_no_visitados = set(grafo.nodos)

    while nodos_no_visitados:
        nodo_actual = min(nodos_no_visitados, key=lambda nodo: distancia[nodo])

        for vecino, peso in grafo.aristas[nodo_actual]:
            ruta_alternativa = distancia[nodo_actual] + peso
            if ruta_alternativa < distancia[vecino]:
                distancia[vecino] = ruta_alternativa

        nodos_no_visitados.remove(nodo_actual)

    return distancia

# Crear un grafo de ejemplo
grafo = Grafo()
grafo.agregar_nodo('A')
grafo.agregar_nodo('B')
grafo.agregar_nodo('C')
grafo.agregar_nodo('D')
grafo.agregar_arista('A', 'B', 1)
grafo.agregar_arista('A', 'C', 4)
grafo.agregar_arista('B', 'C', 2)
grafo.agregar_arista('B', 'D', 5)
grafo.agregar_arista('C', 'D', 1)

inicio = 'A'
distancias = dijkstra(grafo, inicio)

for nodo, distancia in distancias.items():
    print(f'Distancia desde {inicio} a {nodo}: {distancia}')
