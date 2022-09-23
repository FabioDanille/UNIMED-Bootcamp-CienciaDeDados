# Criando Classes Abstratas com o modo ABC
from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligado!")


    def desligar(self):
        print("Desligando a TV...")
        print("Desligado!")

    @property
    def marca(self):
        return "Philco"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando O Ar Condicionado...")
        print("Desligado!")
    
    @property
    def marca(self):
        return "LG"

controle = ControleTV()
controle.ligar()
print(controle.marca)
controle.desligar()

print()

controle = ControleArCondicionado()
controle.ligar()
print(controle.marca)
controle.desligar()