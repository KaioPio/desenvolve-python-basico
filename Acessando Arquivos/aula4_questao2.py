import re

with open("frase.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

palavras = re.findall(r'\b[a-zA-ZÀ-ÿ]+\b' , conteudo)


with open("palavras.txt", "w", encoding="utf-8") as novo_arquivo:
    for palavra in palavras:
        novo_arquivo.write(palavra + "\n")

with open("palavras.txt", "r", encoding="utf-8") as resultado:
    print("Conteudo de palavras.txt")
    print(resultado.read())