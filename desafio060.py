'''from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')'''
from time import sleep
n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1 #fator nulo de multiplicação é 1, de soma e subtração é 0 (se eu somo 0 ao número, ele resulta nele mesmo)
print(f'Calculando {n}! = ', end='')
sleep (1)
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 #c = c - 1 (tirar 1 do c)
print(f'{f}.')