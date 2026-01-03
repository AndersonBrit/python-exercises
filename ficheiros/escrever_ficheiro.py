# exercicios/ficheiro/escrever_ficheiro.py

caminho = r"C:\Users\dedeg\Desktop\PSI _PY\anderson\projetos\ficheiros\ficheiro.txt"

with open(caminho, "a") as ficheiro:
    ficheiro.write("\nola")