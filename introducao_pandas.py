import pandas as pd

# leitura dos dados csv
csv_file = 'temperature.csv'

df = pd.read_csv(csv_file)
print(df)

# leitura de arquivos excel
excel_file = pd.ExcelFile('temperature.xlsx')
print(type(excel_file), '\n')

df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

# df3 = pd.read_excel(excel_file, sheet_name='Sheet2')
# print(df3)

head = 2  # definindo a quantidade incial de linhas a serem lidas
print(df.head(head))

tail = 2  # exibindo as n ultimas linhas
print(df.tail(tail))

print(df.dtypes)
print(df.describe())  # estatísticas básicas de colunas numéricas
print(df.info())  # dataframe info
print(df.columns)  # colunas
