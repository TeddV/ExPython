a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Segundo valor:'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and c > b:
    maior = b
if c > a and c > b:
    maior = b
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
