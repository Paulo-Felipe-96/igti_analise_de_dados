import numpy as np

x = np.array([[1, -5], [10, 2]])
y = np.array([1.75, -1.99])

print(f'x maior que y: \n'
      f'{x > y}')

print(f'x maior que 2: \n'
      f'{x > 2}')

print(f'y menor que 1: \n'
      f'{y < 1}')

# atividade: retorne numeros maiores que k
k = 1
x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])

cond = x > k
retorno = x[cond]
print(retorno)
print(f'Quantos números são maiores que {k}: {len(retorno)} \n'
      f'Estes números são {retorno}')

numeros_pares = x % 2 == 0
numeros_impares = x % 2 != 0
print(f'Resposta booleana: \n'
      f'{numeros_pares} \n'
      f'Os números pares são: {x[numeros_pares]} \n'
      f'Os números impares são: {x[numeros_impares]}')

x = np.array([5, 20, 6])
y = np.array([25, 15, 16])

# y é divisível por x ?
res = y % x == 0
print(f'{y[res]} divisível por {x[res]}? \n'
      f'{res}')
