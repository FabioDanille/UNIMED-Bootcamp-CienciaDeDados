class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("FOOOOOOOOOOON!")

    def parar(self):
        print("Parando bike")
        print("Parei!")


    def correr(self):
        print("Vruuuuuum")

    # def __str__(self):
    #     return f"{self.__class__.__name__}: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    

b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
b2.buzinar()
# Bicicleta.buzinar(b2)
print(b2) # Bicicleta: verde, monark, 2000, 189