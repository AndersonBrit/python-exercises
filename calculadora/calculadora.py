# exercicios/calculadora/calculadora.py

import time
import os

def limpar_tela():
    """Limpa o ecrã do terminal, independentemente do SO."""
    os.system('cls' if os.name == 'nt' else 'clear')


def Soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A soma é: {num1 + num2}")
    time.sleep(3)

def Subtração():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A subtração é: {num1 - num2}")
    time.sleep(3)

def Multiplicação():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print(f"A multiplicação é: {num1 * num2}")
    time.sleep(3)

def Divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if num2 != 0:
        print(f"A divisão é: {num1 / num2}")
    else:
        print("Erro: Divisão impossivel")
    time.sleep(3)


def Calculadora():

    while True:

        limpar_tela()
        print("\t*** Calculadora Python ***\n")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Sair\n")


        try:
            opcao = int(input("Escolha a opção desejada\n"))

        except ValueError:
            limpar_tela()
            print("Insira um valor valido")
            input("\nPressione Enter para continuar...")
            continue

        if opcao == 1:
            limpar_tela()
            Soma()

        elif opcao == 2:
            limpar_tela()
            Subtração()

        elif opcao == 3:
            limpar_tela()
            Multiplicação()

        elif opcao == 4:
            limpar_tela()
            Divisao()

        elif opcao == 5:
            limpar_tela()
            print("O programa foi encerrado")
            break

        else:
            limpar_tela()
            print("Opção errada")


Calculadora()
