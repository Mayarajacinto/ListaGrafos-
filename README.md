# Prática 1 - Algoritmos de Caminho Mínimo
# Autores: Abraão Melo, Mayara Jacinto e Paulo Veras

## Resumo

Nesta atividade, vamos explorar o conceito de caminho mínimo utilizando algoritmos como
Djkistra, Bellman-Ford, Floyd. A atividade foi realizada em trio, pelos discentes Abraão Melo, Mayara Jacinto e Paulo Veras.
Exploramos três cenários de aplicação:
Cenário 1 - Determinando a estação central.
Cenário 2 - Otimizando caminho com regeneração
Cenário 3: Robô de armazém com obstáculos.

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento local.

### Pré-requisitos

Liste as principais dependências de software que precisam ser instaladas manualmente.
* Python 3.9+
* Conda

### Passos para Instalação

1.  Clone o repositório:
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  Crie e ative o ambiente Conda:
    ```bash
    conda env create -f environment.yml
    conda activate nome-do-ambiente
    ```
    *Como alternativa, se estiver usando `pip`*:
    ```bash
    pip install -r requirements.txt
    ```

## Como Usar

Para reproduzir os resultados principais do artigo, execute os scripts na seguinte ordem:

1.  **Pré-processamento dos dados:**
    ```bash
    python src/01_preprocess_data.py
    ```

2.  **Execução da análise principal:**
    ```bash
    Rscript src/02_run_analysis.R
    ```

3.  **Geração das figuras e tabelas:**
    ```bash
    python src/03_generate_figures.py
    ```
    As figuras serão salvas no diretório `/results/figures`.

## Estrutura do Repositório
