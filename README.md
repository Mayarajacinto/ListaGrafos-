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
git clone https://github.com/Mayarajacinto/ListaGrafos-.git
cd ListaGrafos-
```
    
## Como Compilar

Para testar o cenário 1:
```bash
cd .\cenario1 # ir ao diretório do cenário 1
python cenario1.py
```

Para testar o cenário 2:
```bash
cd .\cenario2 # ir ao diretório do cenário 2
python cenario2.py
```

Para testar o cenário 3:
```bash
cd .\cenario3 # ir ao diretório do cenário 3
python cenario3.py
```
## Escolha dos algoritmos
### Cenário 1 - Determinando a estação central
O algoritmo escolhido para esse cenário foi o Floyd-Warshall. O motivo dessa escolha é porque esse algoritmo calcula todas as distâncias mínimas entre todos os pares de vértices de uma só vez e permite fácil comparação de qual vértice tem a menor distância máxima para todos os outros vértices. Apesar de ter complexidade O(n³), ainda é aceitável para grafos de tamanho razoável. Outro motivo para a escolha foi a forma da saída desse algoritmo, que se dá em forma de matriz, o que facilita a vizualição.

#### Comparação do código com pseudocódigo (Floyd-Warshall)
A comparação com o pseudocódigo do cenário 1 está no PDF com nome "Comparação pseudocódigo - Cenário 1"

