"""
Pandas possui 2 métodos de indexação muito comuns:

iloc, que busca por índice Inteiro linhas e colunas, também aceitando slicing [:, :]
loc, que busca os índices das linhas e colunas por nome

Indexação booleana:

df[df['classification']=='quente'], que retorna uma nova lista, trazendo somente
resultados que são verdadeiros.

df.loc[df['classification']=='quente', 'temperatura'], selecionando a coluna onde a condição
é verdadeira e trazendo qual o valor associado.
"""

import pandas as pd

excel_file = pd.ExcelFile('temperature.xlsx')

df = pd.read_excel(excel_file, sheet_name='Sheet1')

quente = df.loc[df['classification'] == 'quente', 'temperatura']
print(quente)
