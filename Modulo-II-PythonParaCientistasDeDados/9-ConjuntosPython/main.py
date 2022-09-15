# Removendo itens iguais
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio","gol","celta","palio")) # {"gol","celta","palio"}



### Acessando dados
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(f"{carro}")
    

print()
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")



""" MÉTODOS DA CLASSE SET """

# ().union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
print()



# ().intersection
conjunto_a = {1, 2, 3}
conjunto_a = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b)) # {3, 4}
print()



# ().difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}
print()



# ().symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}
print()



# ().issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False
print()



# ().issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True
print()



# ().isdisjoint
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False
print()



# ().add
sorteio = {1, 23}

sorteio.add(25) # {1, 23, 25}
sorteio.add(42) # {1, 23, 25, 42}
sorteio.add(25) # {1, 23, 25, 42}



# ().clear
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.clear()
sorteio # {}



# ().copy
sorteio = {1, 23}

sorteio # {1, 23}
sorteio.copy()
sorteio # {}



# ().discard
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45)
numeros # {2, 3, 4, 5, 6, 7, 8, 9, 0}



# ().pop
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.pop() # 0
numeros.pop() # 1
numeros # {2, 3, 4, 5, 6, 7, 8, 9} ENGRAÇADO QUE FOI PELA ORDEM NÚMERICA E NÃO DO CONJUNTO



# ().remove
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(0) # 0
numeros # {1, 2, 3, 4, 5, 6, 7, 8, 9}
numeros.discard(45) # a diferença é que aqui vai dar erro, diferente do ().discard



# len
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

len(numeros) # 10



# in
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

1 in numeros # True
10 in numeros # False