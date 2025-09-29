import sys

def bellman_ford(vertices, edges, origem, destino):
    """
    Implementa o algoritmo de Bellman-Ford para encontrar o caminho mínimo
    em grafos com pesos negativos (regeneração de bateria).
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

# Leitura do grafo
def ler_grafo(arquivo):
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
    print("=== RESULTADO - CAMINHO MÍNIMO ===")
    print(f"Caminho: {' -> '.join(map(str, caminho))}")
    print(f"Custo total (energia líquida): {custo_total} Wh")
    print()