import pandas as pd
import sqlite3
import io

#1. Carregar e Preparar os Dados ---
#Conteúdo do arquivo CSV lido como uma string para simulação
dados_csv = """
id,cliente,produto,quantidade,valor
1,Ana,Notebook,1,3500
2,João,Mouse,2,80
3,Maria,Teclado,1,120
4,Ana,Monitor,2,900
5,Pedro,Notebook,1,3500
6,Maria,Mouse,1,40
"""
df = pd.read_csv(io.StringIO(dados_csv))

#Cálculo essencial para análise: TotalVenda = quantidade * valor
df['TotalVenda'] = df['quantidade'] * df['valor']

#2. Configurar o SQLite Temporário ---
#Cria um banco de dados temporário na memória RAM
conn = sqlite3.connect(':memory:')

#Envia o DataFrame do Pandas para o SQLite como uma tabela chamada 'vendas'
df.to_sql('vendas', conn, index=False, if_exists='replace')

print('Análise de Vendas SQL (via Python/Pandas)')
print('=' * 50)

#3. Executar Consultas SQL 

#Consulta 1: Total Faturado por Cliente
print('1. Total Faturado por Cliente:')
sql_query_cliente = """
SELECT 
    cliente, 
    SUM(TotalVenda) AS total_gasto 
FROM 
    vendas
GROUP BY 
    cliente
ORDER BY 
    total_gasto DESC;
"""
resultado_clientes = pd.read_sql_query(sql_query_cliente, conn)
print(resultado_clientes.to_string(index=False))
print('\n' + ('-' * 50) + '\n')


#Consulta 2: Produto mais vendido (por número de ITENS vendidos)
print('2. Produto mais vendido (por ITENS):')
sql_query_produto = """
SELECT 
    produto, 
    SUM(quantidade) AS total_itens_vendidos
FROM 
    vendas
GROUP BY 
    produto
ORDER BY 
    total_itens_vendidos DESC;
"""
resultado_produtos = pd.read_sql_query(sql_query_produto, conn)
print(resultado_produtos.to_string(index=False))

#3: Finalizar 
conn.close()
print('\n' + ('=' * 50))
print('Análise concluída e conexão fechada.')

