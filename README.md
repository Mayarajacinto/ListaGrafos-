# Prática 1 - Algoritmos de Caminho Mínimo
# Autores: Abraão Melo Santana Duarte, Mayara Jacinto e Paulo Veras

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Resumo

Breve descrição do projeto (1-3 parágrafos). Qual é a pergunta de pesquisa, a metodologia principal e a contribuição deste trabalho? Pense nisso como o abstract do seu artigo.

**Artigo Associado:** [Título do Artigo](https://link-para-o-artigo-se-existir.com)

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
