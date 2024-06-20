# Inpute de qual as dimensões #

comp = int(input("Qual o comprimento do terreno?"))
larg = int(input("Qual a largura do terreno ?"))
precom2 = float(input("Qual o valor do metro quadrado?"))
# calculo da área #
aream2 = comp * larg


# Calculo do preço total#
preço_total = precom2 * aream2

print (f"O seu terreno possui {aream2}m2 e custa {preço_total:,.2f}")