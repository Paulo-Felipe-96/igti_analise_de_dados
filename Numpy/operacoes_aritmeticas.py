"""
Numpy permite realizar operações aritmeticas de maneira performatica e intuitiva.
As operações podem ser feitas "element by element" ou por matrizes.

Broadcasting ou propagação:
É um recurso que permite realizar operações aritmeticas entre arrays de diferentes
dimensões.
Em casos onde um array é maior que outro, virtualmente o python completa os valores
do menor array para que a operação seja concluída com sucesso.

Soma:
    +
    np.add
Subtração:
    -
    np.subtract
Divisão:
    /
    np.divide
Multiplicação:
    *
    np.multiply

Operações matriciais, multiplicação de matrizes:

Python puro A @ B
Numpy
    np.dot(A,B) ou
    A.dot(B)
"""
import numpy as np

v = [2, 2]
u = [2, 2]
soma = np.add(v, u)
print(soma)
