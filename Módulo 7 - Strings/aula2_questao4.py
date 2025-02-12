import re

# Validador de senha conforme os requisitos #
def validador_senha(x):
    if len(x)<8:
        return "A senha deve ter pelo menos 8 caracteres."
    if not re.search(r'[A-Z]', senha):
        return "A senha deve conter pelo menos uma letra maiúscula."
    if not re.search(r'[a-z]', senha):
        return "A senha deve conter pelo menos uma letra minuscula."
    if not re.search(r'[0-9]', senha):
        return "A senha deve conter pelo menos um número."
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', senha):
        return "A senha deve conter pelo menos um caractere especial."
    return "A senha está válida!"

senha = input("Vamos criar uma nova senha? Digite uma senha e te ajudarei.")
resultado = validador_senha(senha)
print(resultado)