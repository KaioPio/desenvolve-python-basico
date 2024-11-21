import random

lista = [random.randint(-10, 10) for n in range(20)]
print(lista)

tam_lista_maior, inicio_lista_maior = 0, 0
tam_lista_atual, inicio_lista_atual = 0, 0

for i in range (len(lista)):
    if lista[i] < 0:
        tam_lista_atual += 1 
        if tam_lista_atual == 1:
            inicio_lista_atual = i
    else:
        if tam_lista_atual > tam_lista_maior:
            tam_lista_maior = tam_lista_atual
            inicio_lista_maior = inicio_lista_atual
        tam_lista_atual = 0    

print(f"A fatia que será deletada será: {inicio_lista_maior, tam_lista_maior}")
del lista[inicio_lista_maior: inicio_lista_maior + tam_lista_maior]
print(lista)