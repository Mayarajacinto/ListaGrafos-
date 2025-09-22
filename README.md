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

Passos para Instalação

    Clone o repositório:
    Bash

git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

Crie e ative o ambiente virtual:

    Primeiro, crie o ambiente na pasta do projeto:
    Bash

# Este comando cria uma pasta local chamada "venv"
python -m venv venv

(Observação: Dependendo da sua configuração, talvez seja necessário usar python3).

Em seguida, ative o ambiente de acordo com seu sistema operacional:

    No Windows (PowerShell/CMD):
    Bash

.\venv\Scripts\activate

No macOS ou Linux:
Bash

        source venv/bin/activate


Instale as dependências:

    Com o ambiente já ativado, instale todas as bibliotecas necessárias com um único comando:
    Bash

pip install -r requirements.txt


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
