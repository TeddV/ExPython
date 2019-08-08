casa = float(input('Qual o valor da casa? R$'))
renda = float(input('Qual sua renda mensal? R$'))
anos = int(input('Em quantos anos você pretende pagar?'))
prestaçao = casa / (anos * 12)
prestaçaominima = renda * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos), end='')
print('\nA prestação será de {:.2f}'.format (prestaçao), end='')
if prestaçao <= prestaçaominima:
    print('\nFinanciamento aprovado!')
else:
    print('\nFinanciamento negado!')