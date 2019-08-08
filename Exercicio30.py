numero = int(input('Digite um número:'))
resultado = numero % 2
if resultado == 0:
    print('{} é par!'.format(numero))
else:
    print('{} é impar!'.format(numero))