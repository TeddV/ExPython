salario = float(input('Qual o seu salário?'))
if salario <= 1250:
    novosalario = salario + (salario * 15 / 100)
else:
    novosalario = salario + (salario * 10 / 100)
print('Seu salário que era de {:.2f}R$ passa a ser de {:.2f}R$'.format(salario, novosalario))