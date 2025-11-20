# Pergunta a se fazer: Qual é o padrão de clientes mais predispostos a cancelar o cartão da loja?

# Bibliotecas necessárias
import pandas as pd
import plotly.express as px

df = pd.read_csv("Dados\clientes_ficticios.txt")

#Análise inicial
#print(df.head()) #Essa função demonstra as primeiras linhas da tabela

# Análise de informações de colunas
#print(df.info()) #Essa função demonstra se há alguma linha faltando em alguma das colunas e o tipo de dado por coluna.

dfnovo = df.drop("cliente_id" , axis=1) # Essa função é responsável por excluir uma coluna, para a nossa análise a coluna clients_id não teria nenhuma utilidade.

#print(dfnovo.describe().round(1)) #Essa função é responsável por demonstrar as médias, mínimas e máximas de cada dado em cada coluna, com essa função descobrimos que a idade média dos clientes é de 36 anos e a renda mensal é de aproximadamente R$ 7128,00 

#Verificando quantos clientes cancelaram o cartão:

#qtd_cancelamentos = dfnovo["cancelou_cartao"].value_counts() Este comando nos mostra a quantidade de clientes que cancelaram ou não o cartão de acordo com a coluna "cancelou_cartao"
#print(qtd_cancelamentos)

for coluna in dfnovo:
    grafico = px.histogram(dfnovo, x=coluna, color="cancelou_cartao")
    grafico.show()