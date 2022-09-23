import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

## importando dados para o projeto
url = 'https://github.com/neylsoncrepalde/projeto_eda_covid/blob/master/covid_19_data.csv?raw=true'
# url = '22set2022.csv'

df = pd.read_csv(url, parse_dates=['ObservationDate', 'Last Update'])
# print(df)
# print(df.dtypes)


## Nomes de colunas não devem ter letras maiúsculas e nem caracteres especiais. Portanto deve fazer a limpeza
import re

def corrige_colunas(col_name):
    return re.sub(r"[/| ]", "", col_name).lower()


## Corrigir todas colunas do df
df.columns = [corrige_colunas(col) for col in df.columns]
# print(df)


## Brasil... Selecionando apenas dados do Brasil para estudo
df.loc[df.countryregion == 'Brazil']

brasil = df.loc[
    (df.countryregion == 'Brazil') &
    (df.confirmed > 0)
]

# print(brasil)

## Casos confirmados
## Gráfico de evolução de casos confirmados

# px.line(brasil, 'observationdate', 'confirmed', title='Casos confirmados no Brasil') # ... n funciona no vscode



## Casos novos por dia
## Técnica de programação funcional
brasil['novoscasos'] = list(map(
    lambda x: 0 if (x==0) else brasil['confirmed'].iloc[x] - brasil['confirmed'].iloc[x-1],
    np.arange(brasil.shape[0])
))

# print(brasil)




## Mortes
fig = go.Figure()
fig.add_trace(
    go.Scatter(x=brasil.observationdate, y=brasil.deaths, 
    name='Mortes', mode='lines+markers', line={'color':'red'})
)

## Layout
fig.update_layout(title='Mortes por COVID-19 no Brasil')
# fig.show()


## Taxa de crescimento
def taxa_crescimento(data, variable, data_inicio=None, data_fim=None):
    # Se data inicio for None, define como a primeira data disponível
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)

    if data_fim == None:
        data_fim = data.observationdate.iloc[-1]
    else:
        data_fim = pd.to_datetime(data_fim)

    # Define os valores do presente e passado
    passado = data.loc[data.observationdate == data_inicio, variable].values[0]
    presente = data.loc[data.observationdate == data_fim, variable].values[0]

    # Define o número de pontos no tempo que vamos avaliar
    n = (data_fim - data_inicio).days

    # Calcular a taxa
    taxa = (presente/passado)**(1/n) - 1

    return taxa*100

## Taxa de crescimento médio do COVID no Brasil em todo o período
print(taxa_crescimento(brasil, 'confirmed'))


## Taxa de crescimento diário
def taxa_crescimento_diaria(data, variable, data_inicio=None):
    # Se data inicio for None, define como a primeira data disponível
    if data_inicio == None:
        data_inicio = data.observationdate.loc[data[variable] > 0].min()
    else:
        data_inicio = pd.to_datetime(data_inicio)
    
    data_fim = data.observationdate.max()

    # Define o número de pontos no tempo que vamos avaliar
    n = (data_fim - data_inicio).days

    # Taxa calculada de um dia para o outro
    taxas = list(map(
        lambda x: (data[variable].iloc[x] - data[variable].iloc[x-1]) / data[variable].iloc[x-1], 
        range(1, n+1)
    ))
    return np.array(taxas) * 100

tx_dia = taxa_crescimento_diaria(brasil, 'confirmed')
# print(tx_dia)

primeiro_dia = brasil.observationdate.loc[brasil.confirmed > 0].min()

# print(px.line(x=pd.date_range(primeiro_dia, brasil.observationdate.max())[1:],
# y=tx_dia, title='Taxa de crescimento de casos confirmados no Brasil'))




