# Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 

def calcular_digito(cpf, pesos):
    soma = sum(int(cpf[i]) * pesos[i] for i in range(len(pesos)))
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    # Verificar se o CPF tem 11 números e é composto apenas por dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    
    # Primeiros 9 dígitos do CPF
    cpf_base = cpf[:9]
    
    # Pesos para os 9 primeiros dígitos
    pesos_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calcular o primeiro dígito verificador
    digito_1 = calcular_digito(cpf_base, pesos_1)
    
    # Pesos para o cálculo do segundo dígito (usando o primeiro dígito)
    pesos_2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    
    # Calcular o segundo dígito verificador
    digito_2 = calcular_digito(cpf_base + str(digito_1), pesos_2)
    
    # Verificar se os dois dígitos calculados são iguais aos do CPF
    if cpf[-2:] == f"{digito_1}{digito_2}":
        return True
    else:
        return False

# Teste
cpf = input("Digite o CPF (somente números): ")
if validar_cpf(cpf):
    print("CPF Válido!")
else:
    print("CPF Inválido!")
