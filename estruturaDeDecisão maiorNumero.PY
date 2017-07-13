"""
Estrutura de decisão.
    Programa que pede dois números inteiros ao usuario e entrega o maior entre eles.
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 > num2:
    print('O maior número inserido foi: {}'.format (num1))
else:
    print('O maior número inserido foi: {}'.format (num2))
