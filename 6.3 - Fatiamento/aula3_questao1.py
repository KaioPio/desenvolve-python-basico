x = int(input("Quantos numeros você deseja em sua lista? "))
#lista1
lista1 = []
#Adicionar numeros a lista 
for i in range(x):
    y = int(input(f"Me fala o numero {i + 1}: "))
    lista1.append(y)      


print(f"Lista original", lista1)
print(f"Primeiros 3 numeros da lista {lista1[0:3]}")
print(f"Ultimos dois numeros da lista: {lista1[-2:]}")
print(f"Lista invertida: {lista1[::-1]}")
print(f"Elementos de índice par: {lista1[::2]}")
print(f"Elementos de índice ímpar: {lista1[1::2]}")
85