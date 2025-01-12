# Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:


frase = input("Digite uma frase, contarei quantas vogais ela possui!")
vogais = 0 
indice_vogal = []

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        vogais += 1
        indice_vogal.append(i)

print(f"Na frase possui {vogais} vogais !")
print(f"E ses indices são: {indice_vogal}")
