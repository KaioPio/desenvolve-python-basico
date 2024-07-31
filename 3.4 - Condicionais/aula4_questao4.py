print ("Vou calcular o valor para a entrega do seu pacote!")
pacotekg, distancia = int(input("Quantos Kg tem o pacote ?")), int(input("Qual a distancia até o local de entrega ? "))
if (distancia < 100) and (pacotekg < 10):
 print (1 * pacotekg)
if (distancia < 300 and distancia > 100) and (pacotekg < 10):
 print (1.50 * pacotekg)
if (distancia > 300) and (pacotekg < 10):
 print (2 * pacotekg)
if (distancia < 100) and (pacotekg > 10):
 print ((1 * pacotekg) + 10)
if (distancia < 300 and distancia > 100) and (pacotekg > 10):
 print ((1.50 * pacotekg) + 10)
if (distancia > 300) and (pacotekg > 10):
 print ((2 * pacotekg) + 10)