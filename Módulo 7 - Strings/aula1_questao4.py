#Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos,
#acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9.
#Adicione o separador "-" na sua impressão.

tel = input("Digite o seu número de telefone para correção: ")

if len(tel) == 8:
    tel = '9' + tel  

elif len(tel) == 9:
    if tel[0] != '9': 
        tel = '9' + tel[1:]
        
tel_formatado = tel[:5] + '-' + tel[5:]

print(tel_formatado)