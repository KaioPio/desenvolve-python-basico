with open(r'C:\Users\USER\Documents\Python\Acessando Arquivos\Atividade6\spotify-2023.csv', 'r', encoding='latin-1') as arquivo:
    # Lendo as cinco primeiras linhas
    for i in range(5):
        linha = arquivo.readline()
        print(linha.strip())

import csv
from tabulate import tabulate


def processar_csv(caminho_arquivo):
    mais_tocadas_por_ano = {}

    with open(caminho_arquivo, encoding='latin-1') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            # Ignora linhas com campos entre aspas (indicadores de problemas com vírgulas internas)
            if any(campo.startswith('"') and campo.endswith('"') for campo in linha):
                continue

            try:
                track_name = linha[0].strip()
                artist_name = linha[1].strip()
                artist_count = int(linha[2])
                released_year = int(linha[3])
                streams = int(linha[8])

                if 2012 <= released_year <= 2022:
                    atual = mais_tocadas_por_ano.get(released_year)
                    if not atual or streams > atual[3]:
                        mais_tocadas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

            except (IndexError, ValueError):
                # Pula linhas mal formatadas
                continue

    # Gera lista ordenada por ano
    resultado = [mais_tocadas_por_ano[ano] for ano in sorted(mais_tocadas_por_ano)]
    return resultado

# Exemplo de uso:
caminho = r"C:\Users\USER\Documents\Python\Acessando Arquivos\Atividade6\spotify-2023.csv"
top_musicas = processar_csv(caminho)

#Print das musicas em tabela.

cabecalho = ['Ano', 'Música', 'Artista(s)', 'Streams']
tabela = [[m[2], m[0], m[1], f'{m[3]:,}'] for m in top_musicas]

print(tabulate(tabela, headers=cabecalho, tablefmt='fancy_grid', stralign='center', numalign='right'))
