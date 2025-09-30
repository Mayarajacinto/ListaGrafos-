import sys

def bellman_ford(vertices, edges, origem, destino):
    """
    Implementa o algoritmo de Bellman-Ford para encontrar o caminho mínimo.
    
    Este algoritmo é adequado para grafos com pesos negativos, como no caso
    de carros elétricos com regeneração de bateria, onde trechos de descida
    devolvem energia (pesos negativos) e trechos de subida consomem energia
    (pesos positivos).
    
    Args:
        vertices (int): Número total de vértices no grafo
        edges (list[tuple]): Lista de arestas no formato (u, v, peso), onde:
            - u (int): vértice de origem da aresta
            - v (int): vértice de destino da aresta
            - peso (int): custo da aresta (positivo=consumo, negativo=regeneração)
        origem (int): Vértice de origem do caminho
        destino (int): Vértice de destino do caminho
    
    Returns:
        tuple: Uma tupla contendo:
            - list[int] or None: Lista ordenada de vértices que formam o caminho,
              ou None se não houver caminho válido
            - int or None: Custo total do caminho (energia líquida em Wh),
              ou None se não houver caminho válido
            - str or None: Mensagem de erro se houver ciclo negativo ou caminho
              inexistente, ou None se o caminho foi encontrado com sucesso
    
    Note:
        - Complexidade de tempo: O(V·E)
        - Complexidade de espaço: O(V)
        - O algoritmo detecta ciclos negativos automaticamente
    """
    # Inicializa distâncias e predecessores
    dist = [float('inf')] * vertices
    pred = [-1] * vertices
    dist[origem] = 0
    
    # Relaxa todas as arestas V-1 vezes
    for _ in range(vertices - 1):
        for u, v, peso in edges:
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                pred[v] = u
    
    # Verifica ciclos negativos
    for u, v, peso in edges:
        if dist[u] != float('inf') and dist[u] + peso < dist[v]:
            return None, None, "Ciclo negativo detectado!"
    
    # Reconstrói o caminho
    if dist[destino] == float('inf'):
        return None, None, "Não há caminho para o destino!"
    
    caminho = []
    atual = destino
    while atual != -1:
        caminho.append(atual)
        atual = pred[atual]
    caminho.reverse()
    
    return caminho, dist[destino], None


def ler_grafo(arquivo):
    """
    Lê um grafo direcionado de um arquivo de texto.
    
    O arquivo deve estar no formato:
    - Primeira linha: número de vértices e número de arestas (separados por espaço)
    - Linhas seguintes: uma aresta por linha no formato "u v peso"
    
    Args:
        arquivo (str): Caminho do arquivo contendo a representação do grafo
    
    Returns:
        tuple: Uma tupla contendo:
            - int: Número de vértices no grafo
            - list[tuple]: Lista de arestas, onde cada aresta é uma tupla (u, v, peso):
                - u (int): vértice de origem
                - v (int): vértice de destino
                - peso (int): peso da aresta (pode ser negativo)
    """
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
    
    primeira_linha = linhas[0].strip().split()
    vertices = int(primeira_linha[0])
    num_arestas = int(primeira_linha[1])
    
    edges = []
    for i in range(1, num_arestas + 1):
        u, v, peso = map(int, linhas[i].strip().split())
        edges.append((u, v, peso))
    
    return vertices, edges

# Execução principal
vertices, edges = ler_grafo('graph2.txt')
origem = 0
destino = 6

caminho, custo_total, erro = bellman_ford(vertices, edges, origem, destino)

if erro:
    print(erro)
else:
    print(f"Caminho: {' -> '.join(map(str, caminho))}")
    print(f"Custo total (energia líquida): {custo_total} Wh")