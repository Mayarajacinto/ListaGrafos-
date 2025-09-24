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
