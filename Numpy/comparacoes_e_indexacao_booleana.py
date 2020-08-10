import numpy as np

# é possível salvar em uma variável, o retorno de uma expressão lógica
A = np.array([1, -10, 100]) > np.array([100, 0, 0])
B = np.array([1, -10, 100]) < np.array([100, 0, 0])
C = len(np.array([1, -10, 100])) == len(np.array([100, 0, 0]))
print(A)
print(B)
print(C)

# broadcasting de comparações
D = np.array([10, 20, -1])
E = np.array([100, 43, -100])

print(D[-1] < E[-2])
num = 3
print(f'Comparação: \n'
      f'é {num} maior que: {num > D} \n'
      f'é {num} menor que: {num < D} \n'
      f'é {num} diferente de: {num != D} \n'
      f'é {num} igual a: {num == D} \n'
      f'é {num} maior/igual a: {num >= D}')

# operacao de filtro
cond = D < 1
F = D[cond]
print(D)
print(F)
print(cond)
