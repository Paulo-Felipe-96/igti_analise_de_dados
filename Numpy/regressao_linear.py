"""
Regressão linear

O objetivo da aula é introduzir matplotlib e resolver o problema de regressão linear
e o problema quadrática.

.reshape(-1, 1), a presença do -1 indica que estamos forçando o numpy a ignorar o
numero de colunas e transformar a quantidade de elementos em linhas

matplotlib é uma biblioteca para visualização de dados

A função que melhor explica o comportamento dos dados é:
y = a*x + b
"""
import numpy as np
import matplotlib.pyplot as plt

# dados
x = [-1., -0.77777778, -0.55555556, -0.33333333, -0.11111111,
     0.11111111, 0.33333333, 0.55555556, 0.77777778, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657,
     1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais') # 'o' indica utilização de Scatter plot
plt.legend()  # para expor a label
plt.xlabel('x')  # eixo x
plt.ylabel('y')  # eixo y
plt.grid()  # define a grid da imagem, sem ela seria uma linha
plt.savefig('demo.png', bbox_inches='tight')  # no lugar de .show(), pois no console não funcionaria

x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# gerando a quantidade de linhas que x tem
X = np.hstack((x, np.ones(x.shape)))

beta = np.linalg.pinv(X).dot(y)
print(f'a estimado: {beta[0][0]} \n'
      f'b estimado: {beta[1][0]}')

# plot dos dados com o problema resolvido

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'o', label='dados originais')
plt.plot(x, X.dot(beta), label='regressão linear')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('solved.png', bbox_inches='tight')