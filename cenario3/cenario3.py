import heapq

def ler_grid(arquivo):
    
    with open(arquivo, 'r') as f:
        linhas = f.readlines()
        
    num_linhas, num_colunas = map(int, linhas[0].strip().split())
    
    grid = []
    inicio = None
    objetivo = None
    
    for i, linha in enumerate(linhas[1:]):
        linha = linha.strip()
        grid.append(list(linha)) 
        
        if 'S' in linha:
            inicio = (i, linha.index('S'))
            
        if 'G' in linha:  
            objetivo = (i, linha.index('G'))
            
    return grid, inicio, objetivo, num_linhas, num_colunas

def obter_custo(celula):
    if celula == '.' or celula == 'S' or celula == 'G':
        return 1
    if celula == '~':
        return 3
    if celula == '#':
        return float('inf')
    
    return float('inf')

"""
    O pseudocodigo foi implemnetado aq 
    -> inicializa o dist[V]: infinito para todos, menos para a origem que é 0
    -> inicializa o conjunto S para vertices visitados 
    -> inicializa a fila de prioridade Q com todos os vertices 
    -> e enquanto ainda houver elementos em Q o lgoritmo vai rodar para achar o menor caminho 
    
"""
def dijkstra(grid, inicio, objetivo, num_linhas, num_colunas):
    
    # inicializa os caminhos 
    dist = {}
    predecessor = {}
    for i in range(num_linhas):
        for j in range(num_colunas):
            dist[(i, j)] = float('inf')
            predecessor[(i,j)] = None
            
    dist[inicio] = 0        

    #fila de prioridade com heapq -> distancia, vertice 
    pq = [(0, inicio)]
    
    visitados = set()
    
    direcoes = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while pq: 
        
        #pega o vertice com menor distancia 
        dist_atual, vertice_atual = heapq.heappop(pq)
        
        #pula oq ja foi visitado
        if vertice_atual in visitados:
            continue
        
        #marca como visitado e adc a S
        visitados.add(vertice_atual)
        
        #para se chegar no objetivo
        if vertice_atual == objetivo:
            break
        
        #explorar visinhos 
        i, j = vertice_atual
        
        for di, dj in direcoes:
            ni, nj = i + di, j + dj
            
            # Verifica os limites do grid
            if 0 <= ni < num_linhas and 0 <= nj < num_colunas:
                vizinho = (ni, nj)
                
                #pula oque ja foi visitado
                if vizinho in visitados:
                    continue
                
                #custo da celula vizinha
                custo = obter_custo(grid[ni][nj])
                
                #verifica se é um obstacula para pular 
                if custo == float('inf'):
                    continue
                
                #se encontramos um caminho melhor
                nova_dist = dist[vertice_atual] + custo
                
                if nova_dist < dist[vizinho]:
                    dist[vizinho] = nova_dist
                    predecessor[vizinho] = vertice_atual
                    heapq.heappush(pq, (nova_dist, vizinho))
    
    return dist, predecessor

def reconstruir_caminho(predecessor, inicio, objetivo):
    
    #reconstroi o caminho do inicio ate o objetivo
    if predecessor[objetivo] is None:
        return None
    
    caminho = []
    atual = objetivo
    
    while atual is not None:
        caminho.append(atual)
        atual = predecessor[atual]
        
    caminho.reverse()
    return caminho
        
def main():
    arquivo = 'grid_example.txt'
    
    grid, inicio, objetivo, num_linhas, num_colunas = ler_grid(arquivo)
    
    dist, predecessor = dijkstra(grid, inicio, objetivo, num_linhas, num_colunas)
    
    caminho = reconstruir_caminho(predecessor, inicio, objetivo)
    
    if caminho is None:
        print("Não existe um caminho até o objetivo")
        
    else:
        print("RESULTADO")
        print(f"Caminho mínimo (coordenadas): {caminho}")
        print(f"Número de células no caminho: {len(caminho)}")
        print(f"Custo total do caminho: {dist[objetivo]}")
        print()
        
        # Detalhamento do caminho
        print("Detalhamento do caminho:")
        for idx, pos in enumerate(caminho):
            i, j = pos
            celula = grid[i][j]
            custo = obter_custo(celula)
            print(f"  Passo {idx}: {pos} - célula '{celula}' (custo: {custo})")

    
if __name__ == "__main__":
    main()
