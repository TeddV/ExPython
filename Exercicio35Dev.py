print('-='*20)
print('Analisador mde Triângulo')
print('-=*'*-20)
r1 = float(input('Primeiro segundo segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float('Terceiro segmento: ')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r1:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima não formam um triangulo! ')
