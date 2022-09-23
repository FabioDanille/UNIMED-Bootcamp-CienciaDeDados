class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade
    
    @classmethod #criando método de classe... precisando acesso ao contexto da classe usa-se method class
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod #criando método estático... usa-se quando não precisa de contexto, classe nem instância do objeto
    def e_maior_idade(idade):
        return idade >= 18

# p = Pessoa("Guilherme", 28)
# print(p.nome, p.idade)

p = Pessoa.criar_de_data_nascimento(1994,3,21,"Guilherme")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))

