"""
Programa que solicita ao usuario a informação quanto ao seu gênero e entrega as informações de
feminino, masculino ou gênero invalido
"""

usuario = input('Informe seu genero com F ou M: ')
feminino = ['f', 'F',]
masculino = ['m', 'M']
if usuario in feminino:
    print('Feminino')
elif usuario in masculino:
    print('Masculino')
else:
    print('Gênero invalido!')
