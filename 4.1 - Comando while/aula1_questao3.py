
cont = 0
while cont < 3:
    n1 = int(input("Qual o valor de N1? "))
    n2 = int(input("Qual o valor de N2? "))
    n3 = int(input("Qual o valor de N3? "))

    m = (n1 + n2 + n3) / 3

    if m >= 60:
        print("Aprovado")
    elif 40 <= m < 60:
        print("Recuperação")
    else:
        print("Reprovado")
    print("Fim")        

       