numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro número '))
if numero1 < numero2:
    print('O número {} é menor que {}!'.format(numero1, numero2))
elif numero1 == numero2:
    print('Os números são iguais')
else:
    print('O número {} é menor que {}!'.format(numero2, numero1))