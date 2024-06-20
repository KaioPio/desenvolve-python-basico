
nomep1 = str(input("Qual o produto comprado ?"))
qntp1 = int(input (f"Quantas {nomep1} foram compradas?"))
valor1 = float(input("Qual o valor do produto?"))

nomep2 = str(input("Qual o produto comprado ?"))
qntp2= int(input (f"Quantas {nomep2} foram compradas?"))
valor2 = float(input("Qual o valor do produto?"))

nomep3 = str(input("Qual o produto comprado ?"))
qntp3= int(input (f"Quantas {nomep3} foram compradas?"))
valor3 = float(input("Qual o valor do produto?"))

calctotal = (qntp1 * valor1) + (qntp2 * valor2) + (qntp3 * valor3)

print (f"A compra deu um valor de RS:{calctotal:,.2f}")
