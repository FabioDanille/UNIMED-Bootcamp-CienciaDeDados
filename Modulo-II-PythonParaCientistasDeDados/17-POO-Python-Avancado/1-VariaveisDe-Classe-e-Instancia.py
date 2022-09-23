class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome #instância
        self.matricula = matricula # instância
    
    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self. escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" # Variável de Classe
aluno_1.escola = "Apice"# Variável de Instância

aluno_3 = Estudante("Chappie",3) 
mostrar_valores(aluno_1, aluno_2, aluno_3)
