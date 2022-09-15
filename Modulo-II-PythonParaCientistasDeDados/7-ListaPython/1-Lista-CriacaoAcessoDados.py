frutas = ["laranja", "maca", "uva"]

frutas = []

letras = list("python") # ['p', 'y', 't', 'h', 'o', 'n']
# print(letras)

numeros = list(range(10))

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]


#################################################################

frutas = ["maçã", "laranja", "uva", "pera"]
frutas[0] #maçã
frutas[2] #uva

#################################################################

frutas[-1]#pera
frutas[-3]#laranja

#################################################################

matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] # [1, "a", 2]
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"



# Fatiamento #####################################################
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"] 
lista[::-1] # ["n", "o", "h", "t", "y", "p"]


# Iretando lista com for #########################################

carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

print()
# Função enumerate ###############################################

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Filtro versão 1 ##########################################################
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)



print()
# Filtro versão 2 ##########################################################
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)



print()
# Modificando valores versão 1 ##########################################################
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)



print()
# Modificando valores versão 2 ##########################################################
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]




