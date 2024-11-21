lista = (input("Digite uma frase para mostrar as vogais e consoantes!"))
vogais = "AEIOUaeiou"
listav = sorted([ i for i  in lista if i in vogais])
print(listav)
listac = [ i for i in lista if i not in vogais]
print(listac)