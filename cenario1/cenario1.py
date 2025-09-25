def main():
    file = "cenario1/graph1.txt"

def load_graph(file):
    try:
        """
        lê o arquivo;
        cria as variáveis para armazenar o número de vertices e arestas;
        e cria a matriz de adjacência com infinitos.
        """

        with open(file, 'r') as f:
            lines = f.readlines()
 
        num_vertices, num_edges = map(int, lines[0].strip().split())
        INF = float('inf')
        graph = [[INF for _ in range(num_vertices + 1)] for _ in range(num_edges + 1)]

        # custo de um vértice para ele mesmo é zero
        for i in range(1, num_vertices + 1):
            graph[i][i] = 0
        
        # lendo as arestas
        for i in range(1, len(lines)):
            initial_vertex, final_vertex, cost = map(int, lines[i].strip().split())
            graph[initial_vertex][final_vertex] = cost
            graph[final_vertex][initial_vertex] = cost
        
        return graph, num_vertices, num_edges
    
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return None, 0
    except Exception as e:
        print(f"Error loading graph: {e}")
        return None, 0

def floyd_warshall(graph, num_vertices):
    """
    Implementação do algoritmo de Floyd Warshall

    Args:
        graph: matriz de adjacência
        num_vertices: número de vértices do grafo

    Returns:
        tupla = (matriz de distâncias, matriz de roteamento)
    """
    INF = float('inf')
    # cria uma cópia do grafo (da matriz)
    distances = [line[:] for line in graph]
    # cria uma matriz de roteamento de tamanho num_vertices x num_vertices e inicializa como None
    routing = [[None for _ in range(num_vertices + 1)] for _ in range(num_vertices + 1)]

    for i in range(1, num_vertices + 1):
        for j in range(1, num_vertices + 1):
            if i != j and distances[i][j] != INF:
                routing[i][j] = i

    for k in range(1, num_vertices + 1):
        for i in range(1, num_vertices + 1):
            for j in range(1, num_vertices + 1):
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][k]
                    routing[i][j] = routing[i][k]
     
    return distances, routing


