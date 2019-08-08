import math
angulo = float(input('Informe o ângulo:'))
seno = math.sin(math.radians(angulo))
print('o ângulo {} tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O ângulo {} tem o cosseno de: {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O ângulo {} tem a tangente de {:.2f}'.format(angulo, tangente))