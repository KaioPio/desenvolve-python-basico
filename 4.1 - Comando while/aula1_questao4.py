n = int(input("Digite o valor de n: "))
maior = 0  # Inicializa a variável 'maior' como 0

if n > 0:
    while n > 0:
        x = int(input("Digite o valor de x: "))
        if x > maior:
            maior = x  # Atualiza 'maior' se 'x' for maior
        n -= 1  # Decrementa o valor de 'n'
else:
    print("Menor")