import numpy as np

x = np.ones((2, 2))
y = np.eye(2)
print(x)
print(y)
print(f'Soma elemento a elemento: \n{x + y}')
print(f'Soma broadcast: \n{x + 2.}')  # broadcast

print(f'Subtração elemento a elemento: \n{x - y}')
print(f'Subtração broadcast: \n{x - 1.}')  # broadcast

try:
    print(f'Divisão elemento a elemento: \n{x / y}')
except BaseException:
    print('Divisão por zero detectada.')

print(f'Divisão broadcast: \n{x / 2}')  # broadcast

# quando o broadcast não dá certo
try:
    print(f'{np.array([1, 2, 3]) + np.array([1, 2])}')
except ValueError:
    print('Arrays com dimensões inconsistentes não podem ser somados')

# arrays com consistência para funcionamento de broadcast
print(f'{np.array([1, 2, 3]) + np.array([2])}')
