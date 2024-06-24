ida = int(input("Qual a sua idade?"))
jog = input("Você jogou já pelo menos 3 jogos ? (True/False)")
venc = int(input("Quantos jogos você já venceu?"))

resposta = (ida >= 16) and (ida <= 18) and (jog == 'True') and (venc >= 1)

if resposta:
    print ("Apto para ingressar no clube:True")
else:
    print ("Apto para ingressar no clube:False")


