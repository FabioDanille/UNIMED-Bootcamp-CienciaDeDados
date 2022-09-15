# [].append #############################
lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista) # [1, "Python", [40,30,20]]
print()



# [].clear #############################
lista = [1, "Python", [40,30,20]]
print(lista) # [1, "Python", [40,30,20]]
lista.clear()
print(lista) # []
print()



# [].copy #############################
lista = [1, "Python", [40,30,20]]
lista.copy()  # retorna a lista em outra instância, não sendo afetado por functions
print(lista)
print()



# [].count #############################
cores = ["vermelho", "azul", "verde", "azul"]

cores.count("vermelho") # 1
cores.count("azul") # 2
cores.count("verde") # 1
print()



# [].extend #############################
linguagens = ["python", "js", "c"]

print(linguagens) # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens) # ["python", "js", "c", "java", "csharp"]
print()



# [].index #############################
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.index("java") # 3 (mostra onde há o índice pela primera vez)
linguagens.index("python") # 0
print()


# [].pop #############################
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.pop() # csharp
linguagens.pop() # java
linguagens.pop() # c
linguagens.pop(0) # python


# [].remove #############################
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c") # assim não manda o índice, e sim o objeto em si
print()



# [].reverse #############################
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens) # ["csharp, "java", "c", "js", "python"]
print()



# [].sort #############################

# ordenando alfabeticamente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort() # ["c", "csharp", "java", "js", "python"] 

# ordenando alfabeticamente de trás para frente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True) # ["python", "js", "java", "csharp", "c"]

# ordenando por tamanho da palavra
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]

# ordenando por tamanho da palavra de trás para frente
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True) # ["python, "csharp", "java", "js", "c"])

### OBS: lambda é uma função, onde vai atuar em cada objeto da lista

# len #############################
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens)) # 5



# sorted (caso prefira usar função assim tbm...) #############################
linguagens = ["python", "js", "c", "java", "csharp"]

sorted(linguagens, key=lambda x: len(x)) # ["c", "js", "java", "python", "csharp"]
sorted(linguagens, key=lambda x: len(x), reverse=True) # ["python", "js", "java", "csharp", "c"]
