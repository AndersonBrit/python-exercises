# exercicios/classes/pessoa.py

import os

def limpar_tela():
    """Limpa o ecrã do terminal, independentemente do SO."""
    os.system('cls' if os.name == 'nt' else 'clear')

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"Bem-vindo {self.nome}, tens {self.idade} anos"

def main():
    pessoas = []

    while True:
        limpar_tela()
        print("1 - Inserir dados")
        print("2 - Ver lista")
        print("3 - Sair")
        print("")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            input("Valor inválido. Enter para continuar...")
            continue

        if opcao == 1:
            try:
                total = int(input("Quantas pessoas quer adicionar? "))
            except ValueError:
                input("Número inválido. Enter...")
                continue

            for i in range(total):
                limpar_tela()
                print(f"[{i+1}/{total}]")

                nome = input("Nome: ")

                try:
                    idade = int(input("Idade: "))
                except ValueError:
                    input("Idade inválida. Enter...")
                    continue

                pessoas.append(Pessoa(nome, idade))
                input("Pessoa adicionada! Enter...")

        elif opcao == 2:
            limpar_tela()
            if not pessoas:
                print("Lista vazia.")
            else:
                for i, p in enumerate(pessoas, start=1):
                    print(f"{i}. {p.nome} - {p.idade} anos")
            input("\nEnter para continuar...")

        elif opcao == 3:
            print("Programa encerrado.")
            break

        else:
            input("Opção inválida. Enter...")


if __name__ == "__main__":
    main()
