import numpy as np

x = np.linspace(start=10, stop=100, num=10)
print('x:', x)
print(x.shape)
print(x[-3])

# omitindo o início se ele for 0
print(x[:2])

# indo de 60 até o final pelo indice negativo ou positivo
print(x[-5:])
print(x[5:])

# matriz 2D

x = x.reshape(2, 5)
print('x: \n', x)

""""
Acessando pelos índices.
Lembrando: axis 0 é a linha e axis 1 é a coluna
x[linha, coluna]
"""
print(x[1, -2])
print(x[1, 3])
print(x[0, -2])

# pegando toda linha ou coluna
print(f'Primeira linha inteira: {x[0, :]}')
print(f'Segunda linha inteira: {x[1, :]}')
print(f'Selecionando uma coluna inteira:\n'
      f'{x[:, [-4]]}')

"""
Slicing é o compartilhamento de memória do array original.
Para lidar com este detalhe, utilize a função .copy()
"""

c = [1, 2, 3]
print('Antes: ', c)
y = c.copy()  # y = c
y[0] = -100
print('Depois', c)
print(y)
