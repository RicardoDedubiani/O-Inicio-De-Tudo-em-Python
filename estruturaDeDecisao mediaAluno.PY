"""
Programa que solicita ao usuario as notas dos 4 bimestres, mostra a média e diz se o aluno foi aprovado, reprovado ou
aprovado com mérito.
"""

nota1 = int(input("Nota primeiro bimestre: "))
nota2 = int(input("Nota segundo bimestre: "))
nota3 = int(input("Nota terceiro bimestre: "))
nota4 = int(input("Nota quarto bimestre "))
media = (nota1+nota2+nota3+nota4)/4
if media >= 7:
    print("Aluno aprovado! A sua media foi {}! ".format (media))
if media == 10:
    print("Parabéns, aprovado com distinção!")
elif media < 7:
    print("Reprovado! A sua média foi {}! ".format(media))
