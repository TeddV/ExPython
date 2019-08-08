numero = int(input('Insira um número inteiro: '))
print('Escola uma das opço~es abaixo: ')
print('\n [1] Binario: \n [2] Octal: \n [3] Hexadecimal: ')
opçao = int(input('Sua opção: '))
if opçao == 1:
    print('{} convertido para binario é igual a {}'.format(numero, bin(numero)))
elif opçao == 2 :
    print('{} convertido em octal é igual a {}'.format(numero, oct(numero)))
elif opçao ==3:
    print('{} convertido em hexadecimal é igual a {}'.format(numero, hex(numero)))
else:
   print('Opção invalida digite novamente')