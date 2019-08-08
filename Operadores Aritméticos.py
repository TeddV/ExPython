# + = Soma
# - = Subtração
# * = Multiplicação
# / = Divisão
# ** = Potencia
# // = Divisão inteira
# % = Resto da divisão
n1 = int (input('Um valor:'))
n2 = int(input('Outro valor:'))
soma = n1+n2
subtracao = n1-n2
multipicacao = n1*n2
divisao = n1/n2
potencia = n1**n2
divisaointeira = n1//n2
print('A soma vale: {},\n O produto é: {},\n A divisao é: {:.2f} \n  A diferença é igual a {}' .format(soma, multipicacao, divisao, subtracao))
print('Divisão inteira: {}\n A potencia é igual a: {}' .format(divisaointeira, potencia ))