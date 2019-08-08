from random import randint
computador = randint (0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5 tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero pensei?'))
if jogador == computador:
    print('Você acertou, parabens')
else:
    print('Que pena você errou, eu pensei em {} e não em {}'.format(computador, jogador))