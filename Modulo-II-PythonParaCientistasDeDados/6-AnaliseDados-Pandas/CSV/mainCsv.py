import pandas as pd

df = pd.read_csv("advertising.csv")

# print(df.head()) # Mostra as 5 primeiras linhas
# print(df.tail()) # Mostra as 5 últimas linhas
# print(df.shape) # retorna (linha, coluna)
# print(df.columns) # Index(['TV', 'Radio', 'Jornal', 'Vendas'], dtype='object')
# print(df.dtypes)#TV        float64
                  #Radio     float64
                  #Jornal    float64
                  #Vendas    float64
                  #dtype: object
# print(df.describe()) # informações estatísticas do conjunto de dados

# print(df['Radio'].unique())

# print(df)


# Oceania = df.loc[df["continente"] == "Oceania"] # exemplo da aula, modo de utilizar filtros na base de dados
# df.groupby("continente")["País"].nunique() # exemplo da aula, muito utilizado para sqn
# df.groupby("Ano")["Expectativa de vida"].mean() # exemplo da aula, retornando para cada ano qual era a expectativa de vida media
# df["PIB"].mean() # exemplo da aula, retornando a média do PIB
# df["PIB"].sum() # exemplo da aula, somando PIB
