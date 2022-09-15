frutas = ("laranja", "pera", "uva",) # para evitar erros, coloca-se ',' no final

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)



### Acessando valores da tupla
frutas = ("maçã", "laranja", "uva", "pera",)
frutas[0] # maçã
frutas[2] # uva

frutas[-1] # pera
frutas[-3] # laranja


# Tuplas aninhadas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz[0][-1] # 2
matriz[-1][-1] # "c"


# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n")

tupla[2:] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")
tupla[1:3] # ("y", "t")
tupla[0:3:2] # ("p", "t")
tupla[::] # ("p", "y", "t", "h", "o", "n")
tupla[::-1] # ("n", "o", "h", "t", "y", "p")




# Iretando tupla com for #########################################

carros = ("gol", "celta", "palio")
for carro in carros:
    print(carro)

print()




# Função enumerate ###############################################

carros = ("gol", "celta", "palio")

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


""" MÉTODOS COM TUPLAS """

# ().count #############################
cores = ("vermelho", "azul", "verde", "azul")

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1
print()



# ().index #############################
linguagens = ("python", "js", "c", "java", "csharp")

linguagens.index("java") # 3 (mostra onde há o índice pela primera vez)
linguagens.index("python") # 0
print()




# len #############################
linguagens = ("python", "js", "c", "java", "csharp")

print(len(linguagens)) # 5
