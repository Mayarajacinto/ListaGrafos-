# Prática 1 - Algoritmos de Caminho Mínimo
# Autores: Abraão Melo, Mayara Jacinto e Paulo Veras

## Resumo

Nesta atividade, vamos explorar o conceito de caminho mínimo utilizando algoritmos como Djkistra, Bellman-Ford, Floyd. A atividade foi realizada em trio, pelos discentes Abraão Melo, Mayara Jacinto e Paulo Veras. Exploramos três cenários de aplicação:
* **Cenário 1 - Determinando a estação central**
* **Cenário 2 - Otimizando caminho com regeneração**
* **Cenário 3 - Robô de armazém com obstáculos**

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

### Pré-requisitos

* Python 3.13
* Git

## Passos para Instalação

Clone o repositório:
```bash
git clone https://github.com/Mayarajacinto/PraticaGrafos.git
cd PraticaGrafos
```
    
## Como Compilar

Para testar o cenário 1:
```bash
cd .\cenario1 # ir ao diretório do cenário 1
python cenario1.py
cd .. # volta para o diretório principal após o teste
```

Para testar o cenário 2:
```bash
cd .\cenario2 # ir ao diretório do cenário 2
python cenario2.py
cd .. # volta para o diretório principal após o teste
```

Para testar o cenário 3:
```bash
cd .\cenario3 # ir ao diretório do cenário 3
python cenario3.py
cd .. # volta para o diretório principal após o teste
```
## Escolha dos algoritmos
### Cenário 1 - Determinando a estação central
O algoritmo escolhido para esse cenário foi o Floyd-Warshall. O motivo dessa escolha é porque esse algoritmo calcula todas as distâncias mínimas entre todos os pares de vértices de uma só vez e permite fácil comparação de qual vértice tem a menor distância máxima para todos os outros vértices. Apesar de ter complexidade O(V³), ainda é aceitável para grafos de tamanho razoável. Outro motivo para a escolha foi a forma da saída desse algoritmo, que se dá em forma de matriz, o que facilita a vizualição.

#### [Comparação com pseudocódigo - Floyd Warshall](docs/comparacao1.pdf)

##

### Cenário 2 - Otimizando caminho com regeneração
O algoritmo escolhido para esse cenário foi o Bellman-Ford. O principal motivo dessa escolha foi que o algorítmo foi feito para lidar com pesos negativos. O algorítimo Floyd-Warshall também lida com pesos negativos, mas ele calcula todos os caminhos mínimos entre os pares de vértices, retornando uma matriz V×V com todas as distâncias. Isso implica em sua complexidade, que se dá por O(V³), enquanto o Bellman-Ford se dá por O(V·E). Em grafos esparsos (onde E ≈ V), o Bellman-Ford se torna O(V²), sendo significativamente mais eficiente que o Floyd-Warshall.

#### [Comparação com pseudocódigo - Bellman-Ford](docs/comparacao2.pdf)

##

### Cenário 3 - Robô de armazém com obstáculos
O algoritmo escolhido para esse cenário foi o Dijkstra. O motivo principal é que esse algoritmo é ideal para encontrar o caminho mínimo em grafos com pesos não-negativos, que é o caso desse cenário, onde todos os custos são positivos (custo 1 para corredores livres e custo 3 para piso difícil). O Dijkstra garante encontrar o caminho ótimo do inicio (S) até o objetivo (G). Na implementação com fila de prioridade a complexidade é de O(V²), mas usando fila de prioridade (heap) a complexidade se reduz para O((V + E) log V), tornando-o eficiente para grids de tamanho razoável. Outro motivo para a escolha foi a facilidade de adaptação do algoritmo para trabalhar com estruturas de grid, onde cada célula representa um vértice e as conexões entre células adjacentes (4 direções) representam as arestas.

#### [Comparação com pseudocódigo - Dijkstra](docs/comparacao3.pdf)
