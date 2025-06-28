import os

frase = input("Digite uma frase: ")

nomme_arquivo = "frase.txt"

with open(nomme_arquivo, "w") as arquivo:
    arquivo.write(frase)

caminho_completo = os.path.abspath(nomme_arquivo)

print(f"O arquivo foi salvo em: {caminho_completo}")
