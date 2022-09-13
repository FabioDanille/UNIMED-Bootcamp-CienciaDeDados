"""For"""
# texto = input("Informe um texto: ")
texto = "batata"
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print("Executa no final do laço")



"""Função range"""
# range(stop) -> range object
# range(start, stop[, step]) ->
list(range(0, 4)) #[0,1,2,3]
print()

# Utilizando range com for
for numero in range(0, 11):
    print(numero, end=" ")

print()

# exibindo a tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

print()



"""While"""
opcao = -1

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")

print()

while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema")


print()



""" Break """
while True:
    numero10 = int(input("Informe o número 10 ou fique aqui para sempre!"))

    if numero10 == 10:
        break
    
    print(opcao)

print()

for numero in range(100):
    if numero == 10:
        break
    
    print(numero, end=" ")

print()

for numero in range(100):
    if numero % 2 == 0:
        continue # usa-se continue quando quer pular execução
    
    print(numero, end=" ")