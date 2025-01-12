# Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

# Chave de criptografia: gere um valor n aleatório entre 1 e 10

# Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)

import random


nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]

def criptografia(strings):
    n = random.randint(1, 10)
    
    def criptografando(s):
        criptofrado = []
        for char in s:
            unicode_val = ord(char)  
            new_unicode_val = unicode_val + n 
            
            if new_unicode_val > 126:
                new_unicode_val = 33 + (new_unicode_val - 127)  
            
            criptofrado_char = chr(new_unicode_val)  
            criptofrado.append(criptofrado_char)  #

        return ''.join(criptofrado) 
    
    
    strings_criptografadas = [criptografando(nome) for nome in strings]

    return strings_criptografadas, n  


strings_criptografadas, chave = criptografia(nomes)

print("Strings criptografadas:", strings_criptografadas)
print("Chave utilizada:", chave)