velocidade = float(input('Qual a sua vlocidade atual?'))
if velocidade<80:
    print('Você está dentro do limite aceitavel')
else:
    multa = (velocidade - 80) * 7
    print('Você excedeu o limite e foi multado em {:.2f}!'.format(multa))
