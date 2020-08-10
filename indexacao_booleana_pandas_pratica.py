"""
Setando o label de uma coluna como índice faz com que todos os
valores sejam indexados a partir deste.

dataframe.set_index('nome da coluna')

.head() tem por padrão mostrar os 5 primeiros valores
"""

import pandas as pd

excel_file = pd.ExcelFile('temperature.xlsx')
dataFrame = pd.read_excel(excel_file, sheet_name='Sheet1')
# print(dataFrame.dtypes)

dataFrame = dataFrame.set_index('date')
# print(dataFrame.head())

# a condição pode ser passado diretamente ou através de variável

print(dataFrame[dataFrame['temperatura'] >= 25], '\n')

cond = dataFrame['temperatura'] < 25
print(cond)
print(dataFrame[cond], '\n')

cond_data = dataFrame.index <= '2020-03-01'
print(dataFrame[cond_data])

"""
Implicando uma condição que traz resultados antecessores a março e
realiza slice da coluna classification.

Lembrando que no caso de loc precisamos passar o nome da coluna/label
que está sendo filtrado(a) e iloc, o índice numérico.
"""
cond_class = dataFrame.loc[dataFrame.index < '2020-03-01', ['classification']]
print(cond_class)

cond_ = dataFrame.iloc[dataFrame.index < '2020-03-01', [-1]]
print(cond_)

