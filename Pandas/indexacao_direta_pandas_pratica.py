import pandas as pd

excel_file = pd.ExcelFile('temperature.xlsx')
dataFrame = pd.read_excel(excel_file, sheet_name='Sheet1')
print(dataFrame.head(), '\n')

# print(dataFrame['temperatura'], '\n')
# data_temperatura = dataFrame[['date', 'classification', 'temperatura']]

# print(data_temperatura.head())

# frio = dataFrame.loc[dataFrame['classification'] == 'frio', 'date']
# print(f'Dia frio: {frio}')

# acessando através dos índices
# iloc acessa como no numpy, por índice, por números inteiros
# print(help(dataFrame.iloc))

print(dataFrame.iloc[:, 1], '\n')
print(dataFrame.iloc[:, 1:3], '\n')

# loc acessa com o label/nome da coluna

print(dataFrame.loc[:, ['temperatura', 'classification']])

# do label temperatura até o final com a notação loc e :
print(dataFrame.loc[:, 'temperatura':])

# de temperatura para trás
print(dataFrame.loc[:, :'temperatura'])
