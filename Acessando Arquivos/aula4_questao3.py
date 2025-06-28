import re


with open ("estomago.txt", "r", encoding="latin-1") as f:
    linhas = f.readlines()

print("Primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

num_linhas = len(linhas)
print(f"Numero total de linhas: {num_linhas}")

#Variavel comparativa de maior linha em extensão 

linha_maior = max(linhas, key=len)
print("Linha com maior numero de caracteres:")
print(linha_maior.strip())

# V necessário para realizar uma melhor procura das menções dos nomes
texto_completo = texto_completo = "".join(linhas)

# Procura dos termos no texto 

nonato_contar  = len(re.findall(r'\bnonato\b'
                                , texto_completo, flags=re.IGNORECASE))
iria_contar  = len(re.findall(r'\bíria\b', texto_completo, flags=re.IGNORECASE))

print(f"Número de menções a 'Nonato': {nonato_contar}")
print(f"Número de menções a 'Íria': {iria_contar}")