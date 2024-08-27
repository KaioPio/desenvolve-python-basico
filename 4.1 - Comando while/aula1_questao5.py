p = int(input("Quantas pessoas estão participando da entrevista?"))
cont = 0 
soma = 0

while cont < p:
    idade = int(input("Qual a idade?"))
    soma += idade
    cont += 1
print(soma/p)    
