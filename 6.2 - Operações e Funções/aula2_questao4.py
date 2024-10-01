import random
def intercalar_listas(lista1, lista2):
    lista_intercalada = []
    
    # Obtem o tamanho máximo entre as duas listas
    tamanho_maximo = max(len(lista1), len(lista2))
    
    # Intercala os elementos das duas listas
    for i in range(tamanho_maximo):
        if i < len(lista1):
            lista_intercalada.append(lista1[i])
        if i < len(lista2):
            lista_intercalada.append(lista2[i])
    
    return lista_intercalada


# Lista 1 
vezes = int(input("Quantos numeros quer adicionar na lista 1 ?"))
lista1= []
for n in range(vezes):
    x = int(input(f"Digite o numero {n+1}: "))
    lista1.append(x)
# Lista 2 
vezes = int(input("Quantos numeros quer adicionar na lista 2 ?"))
lista2= []
for n in range(vezes):
    x = int(input(f"Digite o numero {n+1}: "))
    lista1.append(x)
# Soma das listas
lista_intercalada = intercalar_listas(lista1, lista2)

print(lista_intercalada)