import pandas as pd  
# lendo a planilha Excel 
df = pd.read_csv('dados_alunos.csv')

# exibindo os dados na tela 
#print(df)  # leitura da planilha inteira 

# 1. visualizar as primeiras linhas 
#print(df.head ()) # exibe os primeiros 5 linhas do dotafrome




# 2. verificar o resumo estatistico (medios, menimos, maximos)
print(df.describe())

# 3. ver os tipos de dados e se ha valores nulos 
print(df.info())







