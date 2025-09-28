*Mini-projeto: Análise Simples de Vendas com Pandas e SQL - Semana 2*

Olá! Bem-vindo(a) ao meu mini-projeto de Análise de Dados.

O objetivo deste projeto é simular uma pequena base de vendas e extrair *insights* básicos, praticando o fluxo fundamental da análise de dados: **carregar, calcular e consultar**.

________________________________________

## 🛠️ Tecnologias Utilizadas

Este projeto usa a stack básica de análise de dados em Python:

* **Python:** Linguagem de programação principal.
* **Pandas:** Usado para ler o arquivo CSV, criar colunas de cálculo (`TotalVenda`) e exibir os resultados das consultas.
* **SQLite3:** Usado internamente pelo script Python para tratar o DataFrame como um banco de dados e executar consultas **SQL**.

________________________________________

## 📁 O que você vai encontrar

Este repositório contém os seguintes arquivos principais:

* **`vendas.csv`**: O arquivo de dados brutos que simula as transações de vendas.
* **`analise_sql.py`**: O script principal em Python que realiza todo o processo:
    1.  Lê o `vendas.csv`.
    2.  Calcula o faturamento real (`quantidade * valor`).
    3.  Cria um banco de dados SQLite temporário na memória.
    4.  Roda consultas SQL complexas.
    5.  Exibe os resultados.

________________________________________

## 🚀 Como rodar o projeto

Quer ver as análises e consultas funcionando na sua máquina? É fácil!

### Pré-requisitos

Certifique-se de que você tem o Python instalado e a biblioteca Pandas (o `sqlite3` já vem com o Python padrão).


