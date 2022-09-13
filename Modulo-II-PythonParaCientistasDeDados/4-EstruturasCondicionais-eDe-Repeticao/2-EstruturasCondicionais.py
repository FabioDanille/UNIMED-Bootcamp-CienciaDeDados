saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque")
else:
    print("Saldo insuficiente!")



opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrado: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque"))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")

"""""""""If aninhado"""""""""
conta_normal = False
conta_universitaria = False
conta_especial = True

saldo = 2000
saque = 1500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")


"""""""""If ternário"""""""""
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque")