"""Parâmetros especiais"""
### Positional only
def criar_carro (modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # INVÁLIDO


### Keyword only
def criar_carro (*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Válido

# criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # INVÁLIDO



### Keyword and Positional only
def criar_carro (modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # Válido

# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # INVÁLIDO



### Objetos de primeria classe
def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar) # O resultado da operação 10 + 10 = 20



### Escopo local e Escopo global
salario = 2000
lista = [1]

def salario_bonus(bonus):
    global salario # no python é preciso avisar que está buscando a variável do escopo global
    
    # lista.append(2) # assim NÃO PODE, pq vai interferir na lista do escopo global, pois sendo objeto imutável, tudo que há de mudança no objeto, há mudança por referência... seria uma exceção
    lista_aux = lista.copy() # por isso usa-se o .copy()
    lista_aux.append(2)
    print(f"Essa é a auxiliar: {lista_aux}")
    salario += bonus
    return salario

salario_bonus(500) #2500
print(f"Essa é a lista normal: {lista}")
