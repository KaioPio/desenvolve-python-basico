
meses = [
    "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
]


data = input("Me diga sua data de aníversário?")

dia, mes, ano = data.split("/")
dia = int(dia)
mes = int(mes)
ano = int(ano)
mes_extenso = meses[mes - 1 ]

print(f"Você nasceu em {dia} de {mes_extenso} de {ano}")