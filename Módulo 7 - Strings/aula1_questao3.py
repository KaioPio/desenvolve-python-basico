frase = str(input("Escreva uma frase para eu contabilizar quantos espaços em branco ela possui"))
espaços = 0
for i in range(len(frase)):
    if frase[i] == " ":
        espaços += 1


print(f"Esta frase tem {espaços} espaços contabilizados!")