## Método Construtor (__init__)
class Cachorro
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome # atributo
        self.cor = cor   # atributo
        self.acordado = acordado  # atributo

## Método Destrutor (__del__)
class Cachorro:
    def __del__(self):
        print("Destruindo a instância")

c = Cachorro()
del c
