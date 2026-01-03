# exercicios/penalti/penaltis.py

import os
import random
import time

def limpar_tela():
    """Limpa o ecrã do terminal, independentemente do SO."""
    os.system('cls' if os.name == 'nt' else 'clear')


def jogar_penaltis():
    """Joga 5 penaltis e calcula a pontuação."""
    limpar_tela()
    print("Começou o jogo! Tens 5 penaltis.")
    print("A cada penalti marcado ganha 10 pontos, a cada penalti falhado perde 5 pontos.\n")
    
    pontos = 0
    total_penaltis = 5

    for i in range(1, total_penaltis + 1):
        input(f"Pressiona Enter para bater o penalti {i}...")
        # Sorteio simples: 0 = falhou, 1 = marcou
        resultado = random.choice([0, 1])
        if resultado == 1:
            print("GOOOOL! Marcaste o penalti!")
            pontos += 10
        else:
            print("Falhaste o penalti...")
            pontos -= 5
        print(f"Pontos atuais: {pontos}\n")
        time.sleep(1)

    print(f"Fim do jogo! Pontuação final: {pontos} pontos.")
    input("Pressiona Enter para voltar ao menu...")


def mostrar_pontuacao(pontos):
    """Mostra a pontuação atual."""
    limpar_tela()
    print(f"A tua pontuação atual é: {pontos} pontos")
    input("\nPressiona Enter para voltar ao menu...")


def main():
    pontos = 0

    while True:
        limpar_tela()
        print("\t*** Jogo de Penaltis ***\n")
        print("1 - Jogar")
        print("2 - Pontuação")
        print("3 - Sair\n")

        try:
            opcao = int(input("Escolhe uma opção: "))
        except ValueError:
            print("Opção inválida!")
            time.sleep(1)
            continue

        if opcao == 1:
            jogar_penaltis()
        elif opcao == 2:
            mostrar_pontuacao(pontos)
        elif opcao == 3:
            limpar_tela()
            print("Jogo encerrado. Até à próxima!")
            break
        else:
            print("Opção inválida!")
            time.sleep(1)


