"""
Reshape redimenciona um array, mas as dimenções DEVEM ser consistentes!
"""

import numpy as np

x = np.array([[1, 3, 7],
              [4, 11, 21],
              [42, 8, 9]])
# x = x.reshape(1, 9)
# print(x)

# x = x.reshape(9, 1)
# print(x)

# transposição, tornar linha coluna e vice-versa
print(x.T)

"""
Metodo .sum(), 
axis=0 ao longo das linhas
axis=1 ao longo das coluna
"""
print(x)

print(f'Soma de todos os elementos do numpy array: \n'
      f'{np.sum(x)}')

print(f'A soma de todas as linhas é: \n'
      f'{np.sum(x, axis=0)} \n'
      f'A soma de todas as colunas é: \n'
      f'{np.sum(x, axis=1)}')

# medias
print(f'Médias: \n'
      f'Matriz inteira: {np.mean(x)} \n'
      f'Ao longo das linhas: {np.mean(x, axis=0)} \n'
      f'Ao longo das colunas: {np.mean(x, axis=1)}')

# np.where()
cond = x % 2 == 0
print(f'Condição: {cond} \n')

i, j = np.where(cond)
print(f'Linhas: {i}\n'
      f'Coluna: {j}')

"""
i_arrow contem uma expressão que retorna linhas onde a cond (par) é satisfeita
x[i_arrow, :] - é um slicing dessa expressão, trazendo não só o número das linhas
mas também os valores contidos nelas.
"""
i_arrow = np.where(np.sum(cond, axis=1))[0]
print(i_arrow)
print(x[i_arrow, :])
