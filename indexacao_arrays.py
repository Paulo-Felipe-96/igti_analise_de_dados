"""
Arrays são acessados pelo seu índice que vai de 0 até n-1

Índices positivos começam de 0 até n-1
Índices negativos começam de trás para frente sendo o último elemento -1
"""

import numpy as np

a = np.array([10.2, 4.2, 1, 15])
print(a[0])
print(a[-2])
print(a[-1])

# percorrendo o vetor A
i = 0
while i < len(a):
    for x in a:
        print(f'A:{x} | {i}')
        i += 1

"""
Podemos ler a notação : como até, por exemplo:
a[0:2] 0 até 2 (-1)
"""
print(a[0:2])  # o número da direita é ele -1
