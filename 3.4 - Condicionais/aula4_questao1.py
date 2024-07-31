x = int(input("Qual o primeiro numero ? "))
y = int(input("Qual o segundo numero ?"))

r = x + y % 2 

if ((r % 2) == 0):
    print ("Este numero é par")
else:
    print ("Este numero é impar")