lista = [num for num in range (20, 51) if num % 2 == 0 ]
print(lista)

lista2 = [1,2,3,4,5,6,7,8,9]
quadrado = [ i**2 for i in lista2]
print(quadrado)

lista3 = [num for num in range (1, 100) if num % 7 == 0 ]
print(lista3)

lista4 = [0,30,3]
listapar = [ "Par" if i % 2 == 0 else "Impar" for i in lista4 ]
print(listapar)