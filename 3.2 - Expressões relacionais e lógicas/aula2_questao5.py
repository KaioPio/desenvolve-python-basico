Genr = input("Qual o seu genero? (M/F)")
ida = int(input("Qual a sua idade ?"))
tano = int(input("Quanto tempo de trabalho?"))

if Genr == 'M':
    valido = (ida > 65) or (tano > 30) or ((ida >60) and (tano >= 25)) 
elif Genr == 'F':
    valido = (ida > 60) or (tano > 30) or ((ida >60) and (tano >= 25)) 

print(valido)
