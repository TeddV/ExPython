import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('digite o nome do terceiro aluno:')
aluno4 = input('digite o nome do quarto aluno:')
alunos = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi:', random.choice(alunos))