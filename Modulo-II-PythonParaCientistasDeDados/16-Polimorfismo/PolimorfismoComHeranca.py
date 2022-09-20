## Exemplo

class Passaro:
    def voar(self): 
        print("Vuanduhhh")

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

# FIXME Exemplo ruim do uso de herança
class Aviao(Passaro):
    def voar(self):
        print("Decolando")

def plano_de_voo(obj):
    obj.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())
plano_de_voo(Aviao())