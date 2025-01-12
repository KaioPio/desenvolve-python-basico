# Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
import itertools
from nltk.corpus import words
import nltk
nltk.download('words')
dicionario = set(words.words())

palavra = input("Me diga uma palavra e mostrarei os anagramas possíveis!")
palavra = palavra.replace(" ", "").lower()
permutacoes = itertools.permutations(palavra)
anagramas = itertools.permutations(palavra)
anagramas_unicos = set([''.join(p) for p in permutacoes if ''.join(p) in dicionario])

print("Anagramas gerados:")
for anagrama in anagramas_unicos:
    print(anagrama)