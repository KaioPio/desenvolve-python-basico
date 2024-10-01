import random

lista1 = [random.randint(0, 50) for n in range(20)]
lista2 = [random.randint(0, 50) for n in range(20)]
#Operação para fazer a interccção das duas listas e separar os valores que se repentem.     
interseccao = list(set(lista1) & set(lista2))
interseccao.sort()

contagem_interseccao = {item: (lista1.count(item), lista2.count(item)) for item in interseccao}

print(lista1)
print(lista2)
print(interseccao)
print("Contagem:")
for item, counts in contagem_interseccao.items():
    print(f"{item}: (lista1={counts[0]}, lista2={counts[1]})")