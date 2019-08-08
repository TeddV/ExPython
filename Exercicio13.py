salario = float(input('Insira seu salario:'))
novo = salario+(salario*15/100)
print('Seu salario era de: R${:.2f} e agora com o aumento de 15% passa a ser de R${:.2f}'.format(salario, novo))