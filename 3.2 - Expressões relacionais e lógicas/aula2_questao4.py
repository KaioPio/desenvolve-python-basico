classe = input("Qual a sua classe? (Guerreiro/Mago/Arqueiro)")
pm = int(input("Digite os pontos de Magia de (de 1 a 20)"))
pf = int(input("Digite os pontos de Força de (de 1 a 20)"))
    
if classe == 'guerreiro':
    consistentes = (pf >= 15) and (pm <= 10)
elif classe == 'mago':
    consistentes = (pf <= 10) and (pm >= 15)
elif classe == 'arqueiro':
    consistentes = (pf > 5 and pf <= 15) and (pm > 5 and pm <= 15)
else:

 print("Classe Invalida")

print(f"Pontos de atributo consistentes com a classe escolhida: {consistentes}")

