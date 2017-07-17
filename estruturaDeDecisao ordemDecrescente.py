"""
Programa que solicita ao usuário 3 numeros e os apresenta em ordem decrescente.
"""

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

if num1 > num2 > num3:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num1, num2, num3))
elif num1 > num3 > num2:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num1, num2, num3))
elif num2 > num1 > num3:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num2, num1, num3))
elif num2 > num3 > num1:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num2, num3, num1))
elif num3 > num2 > num1:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num3, num2, num1))
elif num3 > num1 > num2:
    print('O maior é o {}, o do meio é o {} e o menor é o {}'.format(num3, num1, num2))
