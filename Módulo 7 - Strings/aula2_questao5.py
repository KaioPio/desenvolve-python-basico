import random

def embaralhar_palavra(palavra):
    if len(palavra) > 2:
        
        meio = palavra[1:-1]
        meio_embaralhado = list(meio)
        random.shuffle(meio_embaralhado)
        meio_embaralhado = ''.join(meio_embaralhado)
        return palavra[0] + meio_embaralhado + palavra[-1]
    else:
       
        return palavra


frase = input("Digite uma frase: ")

palavras = frase.split()

# Embaralhar as palavras
palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]

# Juntar as palavras novamente em uma frase
frase_embaralhada = ' '.join(palavras_embaralhadas)

print(f"Frase embaralhada: {frase_embaralhada}")