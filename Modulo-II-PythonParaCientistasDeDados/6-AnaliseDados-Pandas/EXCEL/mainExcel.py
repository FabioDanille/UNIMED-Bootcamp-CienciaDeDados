import pandas as pd

df1 = pd.read_excel(r"Vendas/PR/Venda.xlsx")
df2 = pd.read_excel(r"Vendas/RJ/Venda.xlsx")
df3 = pd.read_excel(r"Vendas/RS/Venda.xlsx")
df4 = pd.read_excel(r"Vendas/SC/Venda.xlsx")
df5 = pd.read_excel(r"Vendas/SP/Venda.xlsx")

# print(df1)
# print(df2)
# print(df3)
# print(df4)
# print(df5)

## Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])
# print(df)

## Exibindo as 5 primeiras linhas
# print(df.head())

## Exibindo as 5 últimas linhas
# print(df.tail())

## Verificando o tipo de dado de cada coluna
# print(df.dtypes)

## Alterando o tipo de dado da coluna que quiser
# df["Valor da Venda"] = df["Valor da Venda"].astype("object")
# print(df.dtypes)



""" TRATANDO VALORES FALTANTES """
## Consultando linhas com valores faltantes
print(df.isnull().sum)
print(df.mean())

print()
## Substituindo os valores nulos pela média
# df["Valor da Venda"].fillna(df["Valor da Venda"].mean(), inplace=True) # vai substituir valores nulos pela média
# print(df.isnull().sum)
# print(df.mean())

## Substituindo valores nulos por 0
# df["Valor da Venda"].fillna(0, inplace=True) # vai substituir por 0
# print(df.mean())

## Apagando as linhas com valores nulos
# df.dropna(inplace=True)

## Apagando as linhas com valores nulos com base apenas em 1 coluna
# df.dropna(subset=["Valor da Venda"], inplace=True)

## Removendo linhas que estejam com valores faltantes em todas as colunas
# df.dropna(how="all", inplace=True)



""" CRIANDO COLUNAS - com base no excel da aula """
## Exemplo criado com base na aula
# df["Receita"] = df["Vendas"].mul(df["Qtde"]) 

# df["Qtde"] = df ["Receita"] / df["Vendas"] # caminho inverso pra ver "Qtde"

## Retornando a maior receita
# df["Receita"].max()

## Retornando a menor receita
# df["Receita"].min()

## nlargest
# df.nlargest(3, "Receita") # top3 com base na coluna "Receita"

## nsmallest
# df.nlargest(3, "Receita") # top3 piores com base na coluna "Receita"

## Agrupamento por cidade
# df.groupby("Cidade")["Receita"].sum()

## Ordenando o conjunto de dados
# df.sort_values("Receita", ascending=False).head(10)



""" TRABALHANDO COM DATAS """
## Transformando a coluna de data em tipo inteiro
# df["Data"] = df["Data"].astype("int64")

## Verificando o tipo de dado de cada coluna
# print(df.dtypes)

## Transformando coluna de data em data
# df["Data"] = pd.to_datetime(df["Data"]) # passando para datetime64
# print(df.dtypes)

## Agrupamento por ano
# df.groupby(df["Data"].dt.year)["Receita"].sum() # dt = datetime... vai na data e extrai apenas o ano, passa a receita e a soma

## Criando uma nova coluna com o ano
# df.["Ano_Venda"] = df["Data"].dt.year
# print(df.sample)

## Extraindo o mês e o dia
# df["mes_venda"], df["dia_venda"] = (df["Data"].dtmonth, df["Data"].dt.day)

## Retornando a data mais antiga
# df["Data"].min()

## Calculando a diferença de dias
#df["diferenca_dias"] = df["Data"] - df["Data"].min()
#print(df.sample())

## Criando coluna de trimestr
# df["trimestre_venda"] = df["Data"].dt.quarter
# print(df.sample())

## Filtrando as vendas de 2019 do mês de março
# vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
# print(vendas_marco_19)


""" VISUALIZAÇÃO DE DADOS (GRÁFICOS) """
#df["LojaID"].value_counts(ascending=False) # vai no conjunto de dados e verifica quantas linhas temos com a LojaID

## Gráfico de barras
#df["LojaID"].value_counts(ascending=False).plot.bar(); # Vai gerar o gráfico... faz parte da bibliteca pandas

## Gráfico de barras horizontais
#df["LojaID"].value_counts(ascending=True).plot.barh(); # Vai gerar o gráfico... faz parte da bibliteca pandas
# obs: ascending = true fará que fique em ordem de maior para menor

## Gráfico de pizza
# df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

## Total de vendas por cidade
# df["Cidade"].value_counts()

## Adicionando um título e alterando o nome dos eixos
# import matplotlib.puplot as plt
# df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
# plt.xlabel("Cidade")
# plt.ylabel("Total Vendas")


## Alterando a cor
# import matplotlib.puplot as plt
# df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
# plt.xlabel("Cidade")
# plt.ylabel("Total Vendas")


## Alterando o estilo
# import matplotlib.puplot as plt
# plt.style.use("ggplot")
# df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total produtos vendidos x mês")
# plt.xlabel("Mês")
# plt.ylabel("Total Produtos Vendidos")
# plt.legend()


## Selecionando apenas as vendas de 2019
# df_2019 = df[df["Ano_Venda"] == 2019]

## Total produtos vendidos por mês
# df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
# plt.xlabel("Mês")
# plx.ylabel("Total produtos Vendidos")
# plt.legend()


## Histograma
# plt.hist(df["Qtde"], color="magenta");

## Gráfico dispersão
# plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

## Salvando em png
# df_2019.groupby(df_2019["mes_venda"]).["Qtde"].sum()plot(marker = "v")
# plt.title("Quantidade de produtos vendidos x mês")
# plx.xlabel("Mês")
# plt.ylabel("Total Produtos Vendidos");
# plt.legend()
# plt.savefig("grafico QTDE x MES.png") # salvando arquivo
