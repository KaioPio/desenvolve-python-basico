ano = int(input("Qual o ano deseja saber se é bissexto ?"))
if ((ano % 4) == 0) and ((ano % 100) != 0) or ((ano % 400) == 0):
    print ("Bissexto")
else:
    print ("Não Bissexto")