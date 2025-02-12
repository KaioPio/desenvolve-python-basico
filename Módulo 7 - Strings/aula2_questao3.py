import unidecode


# Looping #
while True: 
    
    frase = input("Digite uma frase! ")

    if frase == "Fim":
        break

# Fazendo ajustes para manter a comparação mais facil # 
    frase = frase.lower() 
    frase_sem_acento = unidecode.unidecode(frase)
    frase_invertida = frase_sem_acento[::-1]

# Comparador #
    print(frase_invertida)
    if frase_sem_acento == frase_invertida:
        print("A Frase é um Palíndromo")
    else:
        print("A Frase não é um Palíndromo")
