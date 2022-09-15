### Etapa 1

from sklearn.datasets import make_regression
# gerando uma massa de dados:
x, y = make_regression(n_samples=200, n_features=1, noise=30)



import matplotlib.pyplot as plt
#mostrando no gráfico:
plt.scatter(x,y)
plt.show()



from sklearn.linear_model import LinearRegression
# Criação do modelo
modelo = LinearRegression()



### Etapa 2

modelo.predict(x)

array = [] ## where, huh

plt.scatter(x, y)
plt.plot(x, modelo.predict(x), color='red', linewidth=3)
plt.show()

