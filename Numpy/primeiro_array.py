# importando a biblioteca
import numpy as np

# criação de um array 1D
l = [1, 2, 3]
x = np.array(l)
print('x:', x)
print('shape:', x.shape)

# criação de um array 2D
l = [[1, 2], [3, 4]]
x = np.array(l)
print('x:', x)
print('shape:', x.shape)

# zeros
x = np.zeros((5))
print(x)

# array contendo apenas 0's
dim = (2, 2)
x = np.zeros(dim)
print('x:\n', x)
print('shape:', x.shape)

# array contendo apenas 1's
size = (2, 2)
x = np.ones(size)
print('x:\n', x)
print('shape:', x.shape)

"""
crião de valores dentro de um intervalo
valores uniformes entre 5 e 15

o intervalo de 5 a 15 é 2
"""
x_min, x_max = 5, 15
x = np.linspace(start=x_min, stop=x_max, num=6)
print('x:', x)
print('shape:', x.shape)

"""
matriz identidade, onde sua diagonal principal é
composta por 1's e todos os números fora da diagonal
são 0's
"""
n = 10
x = np.eye(n)
print('x:\n', x)
print('shape:', x.shape)

"""
criação de valores aleatórios
valores gerados uniformemente entre 0.0 e 1.0
"""
x = np.random.random(size=(2, 3))
print("x:\n", x)
print("shape:", x.shape)