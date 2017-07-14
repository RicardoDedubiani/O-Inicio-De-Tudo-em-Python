"""
Programa que solicita ao usuário uma letra e informa se é uma vogal ou uma consoante.
"""

letra = input('Digite uma letra: ')
vogais = ['a', 'e', 'i', 'o', 'u']
if letra in vogais:
    print('A letra inserida é uma vogal! ')
else:
    print("A letra inserida é uma consoante!")
