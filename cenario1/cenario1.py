from typing import List, Tuple, Optional

def load_graph(file: str) -> Tuple[Optional[List[List[float]]], int, int]:
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

def floyd_warshall(graph: List[List[float]], num_vertices: int) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
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

def find_central_station(distances: List[List[float]], num_vertices: int) -> Tuple[int, List[float], List, List[List]]:
    """
    Encontrar o nó que representa a estação central escolhida

    Args:
        distances: matriz de distâncias entre os vértices
        num_vertices: número de vértices
    
    Returns:
        tupla: (estacao central,
                vetor de distâncias da estacao central ate os demais vertices,
                vertice mais distante da estacao central e o valor da distancia,
                matriz de candidatos
        )
    """
    INF = float('inf')
    central_station = 1
    distances_to_central = []
    longer_vertex = [1, INF]
    candidates_matrix = []

    for candidate in range(1, num_vertices + 1):
        max_distance = 0
        distances_candidate = []

        for destiny in range(1, num_vertices + 1):
            if candidate != destiny:
                if distances[candidate][destiny] != INF:
                    distances_candidate.append(distances[candidate][destiny])
                    max_distance = max(max_distance, distances[candidate][destiny])
                else:
                    max_distance = INF
                    break
        
        candidates_matrix.append([candidate, max_distance] + distances_candidate)
        
        # Verifica se este candidato é melhor que o atual central_station
        if max_distance < longer_vertex[1]:
            central_station = candidate
            distances_to_central = distances_candidate[:]
            longer_vertex = [candidate, max_distance]
    
    # Encontra o vértice mais distante da estação central escolhida
    if distances_to_central:
        max_dist_from_central = max(distances_to_central)
        # Encontra qual vértice tem essa distância máxima
        vertex_index = 0
        for destiny in range(1, num_vertices + 1):
            if destiny != central_station:
                if distances[central_station][destiny] == max_dist_from_central:
                    longer_vertex = [destiny, max_dist_from_central]
                    break
                vertex_index += 1
    
    return (central_station, 
            distances_to_central, 
            longer_vertex, 
            candidates_matrix)

def main() -> None:
    file = "cenario1/graph1.txt"
    
    print("=" * 60)
    print("CENÁRIO 1: DETERMINANDO A ESTAÇÃO CENTRAL")
    print("=" * 60)
    print("Algoritmo utilizado: Floyd-Warshall")
    print("Motivo: Calcula todas as distâncias mínimas entre todos os pares de vértices")
    print()
    
    graph, num_vertices, num_edges = load_graph(file)
    
    if graph is None:
        return
    
    print(f"Grafo carregado com sucesso: {num_vertices} vértices, {num_edges} arestas")
    print("Executando algoritmo de Floyd-Warshall...")
    distances, routing = floyd_warshall(graph, num_vertices)
    
    # Encontra a estação central
    central_station, distances_to_central, longer_vertex, candidates_matrix = find_central_station(distances, num_vertices)
    
    print("\n" + "=" * 60)
    print("ANÁLISE DOS CANDIDATOS:")
    print("=" * 60)
    
    # Mostra análise de cada candidato
    for line in candidates_matrix:
        candidate = line[0]
        dist_max = line[1]
        distances = line[2:]
        print(f"Vértice {candidate}: distância máxima = {dist_max}")
        print(f"  Distâncias para outros vértices: {distances}")
    
    print("\n" + "=" * 60)
    print("RESULTADOS FINAIS:")
    print("=" * 60)
    print(f"• Estação central escolhida: Vértice {central_station}")
    print(f"• Vetor de distâncias da estação central: {distances_to_central}")
    print(f"• Vértice mais distante: Vértice {longer_vertex[0]} com distância {longer_vertex[1]}")
    
    print(f"\nMatriz de candidatos:")
    print("Candidato | Dist.Max | Distâncias para outros vértices")
    print("-" * 60)
    for line in candidates_matrix:
        candidate = line[0]
        dist_max = line[1]
        distancias = line[2:]
        print(f"    {candidate:2}    |   {dist_max:2}     | {distancias}")
    
    print(f"\nConclusão:")
    print(f"O vértice {central_station} é a estação central ótima porque:")
    print(f"- Tem a menor distância máxima ({longer_vertex[1]}) para qualquer outro vértice")
    print(f"- Minimiza o tempo máximo de deslocamento na rede de metrô")

if __name__ == "__main__":
    main()
