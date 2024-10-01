import random
lista_original = [random.randint(-100, 100) for n in range(20)]
lista_ordenada = sorted(lista_original)

print("Lista original:", lista_original)
print("Lista ordenada:", lista_ordenada)
print("Índice do maior valor:", max(lista_original))
print("Índice do menor valor:", min(lista_original))