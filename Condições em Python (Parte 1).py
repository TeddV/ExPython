tempo = int(input('Quantos anos seu carro tem?'))
if tempo<5:
    print('Seu carro está novo')
else:
    print('Seu carro está velho')
print('Fim')

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2
print('Sua media é de {:.2f}'.format(media))
if media >= 6:
    print('Sua nota está acima da média')
else:
    print('Sua nota está abaixo da media')