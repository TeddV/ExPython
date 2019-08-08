distancia = float(input('Digite a distancia da viagem:'))
print('Voce esta prestes a iniciar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da passagem sera de {}R$!'.format(preco))