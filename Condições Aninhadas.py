nome = str(input('Qual o seu nome?'))
if nome == 'Vinicius':
   print('Temos o mesmo nome!')
elif nome in ('Ana, Juliana, Samara'):
    print('Que belo nome feminino!')
elif nome in ('Mateus, Lucas, Elias!'):
    print('Você tem um nome masculino!')
else:
    print('Que belo nome!')
print('Tenha um bom dia {}!'.format(nome))