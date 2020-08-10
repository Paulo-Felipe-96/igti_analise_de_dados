"""
Multiplicação matricial:

x @ y
np.dot(x, y)
x.dot(y)
"""

import numpy as np

# personalizando os valores de cada posição com a multiplicação
x = 10 * np.ones([2, 4])
print(f'Primeiro: \n {x}')

x = 5 * np.ones([2, 4])
print(f'Segundo: \n {x}')

x = np.ones([10, 10])
print(f'Terceiro: \n {x}')

x = np.array([10, 50])
y = np.array([20, 60])
print(f'Notação nativa x @ y: \n'
      f'{x @ y}')

print(f'Notação np.dot(x, y): \n'
      f'{np.dot(x, y)}')

print(f'Notação x.dot(y): \n'
      f'{x.dot(y)}')
