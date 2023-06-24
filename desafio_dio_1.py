import os
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
data_atual = datetime.now()

menu = """
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def limpar_console():
    """
    Método para limpar o console/terminal para realizar as devidas operações sem muita poluição  visual.\n
    O metodo funciona no Windows e no Linux
    """
    if os.name == "nt":
        # Limpa o console no Windows
        os.system("cls")
    else:
        # Limpa o console no Linux
        os.system("clear")

while True:
    opcao = input(menu)
    limpar_console()
    
    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))
        
        if valor > 0:
            saldo += valor
            print(f"Foi adicionado R${locale.currency(valor, grouping=True, symbol='')} ao saldo!")
            extrato.append({"descricao": "Depósito", "data": data_atual, "valor": valor})
        else:
            print("O valor informado é inválido!\nFavor, digite o valor a ser depositado novamente!")
            
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))
        
        if valor > saldo:
            print("Operação falhou!\nO valor informado é maior que o saldo atual!")
            
        elif valor > limite:
            print(f"Operação falhou!\nO valor informado é maior que o limite de saque que é no  valor de R${limite}!")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou!\nNúmero máximo de saques foi excedido!")
            
        elif saldo >= valor:
            saldo -= valor
            extrato.append({"descricao": "Saque", "data": data_atual, "valor": -valor})
            print(f"Foi retirado R${locale.currency(valor, grouping=True, symbol='')} do saldo!")
            numero_saques += 1
    
        elif saldo == 0:
            print("Saldo insuficiente!")
        
        else:
            pass
            
    elif opcao == "3":
        print("========== Extrato Bancário ==========")
        print(f"Saldo atual: {locale.currency(saldo, grouping=True, symbol='')}")

        if extrato:
            saldo_atual = 0
            print("Histórico de Movimento:")
            for transacao in extrato:
                descricao = transacao["descricao"]
                data = transacao["data"].strftime("%d/%m/%Y")
                valor = transacao["valor"]
                hora = transacao["data"].strftime("%H:%M")
                saldo_atual += valor
                saldo_formatado = locale.currency(saldo_atual, grouping=True, symbol='')
                valor_formatado = locale.format_string("%.2f", abs(valor), grouping=True)

                print(f"{data}-{hora} - {descricao}: R${valor_formatado}.")
        else:
            print("Não foram realizadas movimentações.")

        print("======================================")
    
    elif opcao == "0":
        print("Obrigado por utilizar o nosso sistema!\nVolte sempre!")
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada!")