import random


# Escolhendo uma palavra aleatoria

with open("gabarito_forca.txt","r", encoding="utf-8") as arquivo:
    palavras = arquivo.read().splitlines()

# Tentativas/Letras acertadas

letras_certas = []
tentativas = 6

# Definição do Under Score
 
def exibição_forca(palavras, letras_certas):
    return " ".join([letra if letra in letras_certas else "_" for letra in palavras])

#Definição da palavra aleatoria

palavra_aleatoria = random.choice(palavras)

#Desenho

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as arq:
    desenhos_forca = arq.read().split(",\n")

# Main 

while tentativas > 0:
        print("\npalavras:", exibição_forca(palavra_aleatoria, letras_certas))
        letra_tentativa = input("Digite uma letra: ").lower()


        # Isalpha- verifica se todos os caracteres são de A-Z...    

        if not letra_tentativa.isalpha() or len(letra_tentativa) != 1:
             print("Por favor, digite apenas uma letra")
             continue

        if letra_tentativa in palavra_aleatoria:
            letras_certas.append(letra_tentativa)
            print("Você acertou uma letra.")
        else:
             tentativas -= 1 
             print(f"Letra errada, você tem {tentativas} tentativas.")
             print(desenhos_forca[6 - tentativas])


        if all(letra in letras_certas for letra in palavra_aleatoria):
             print("\n Parabens! Você ganhou!", palavra_aleatoria)
             break     
if tentativas == 0:
     print("\nSuas tentativas acabaram. A palavra era:", palavra_aleatoria)