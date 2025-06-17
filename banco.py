menu = """

Selecione uma das opções: 

1. Depostiar
2. Sacar
3. Extrato
4. Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))

        if valor <= 500 and valor > 0:
            saldo += valor
            extrato += f"Depósito: + R$ {valor:.2f}\n"
        else:
            print("Operação falhou. Valor inválido.")

    elif opcao == "2":
        valor = float(input("Digite o valor de saque: "))

        if valor <= saldo and valor <= limite and numero_saques <= LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque: - R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou. Valor inválido")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
