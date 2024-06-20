nota = int(input("Qual o valor que você deseja receber em troco ?"))
nota_100 = nota // 100
nota = nota % 100
nota_50 = nota // 50
nota = nota % 50
nota_20 = nota // 20
nota = nota % 20
nota_10 = nota // 10
nota = nota % 10
nota_5 = nota // 5
nota = nota % 5
nota_2 = nota // 2
nota = nota % 2
nota_1 = nota // 1

print (f"{nota_100} nota(s) de RS:100,00")
print (f"{nota_50} nota(s) de RS:50,00")
print (f"{nota_20} nota(s) de RS:20,00")
print (f"{nota_10} nota(s) de RS:10,00")
print (f"{nota_5} nota(s) de RS:05,00")
print (f"{nota_2} nota(s) de RS:02,00")
print (f"{nota_1} nota(s) de RS:01,00")