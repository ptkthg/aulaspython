import random
aluno1 = input('Digite o nome do primeiro aluno:')
aluno2 = input('Digite o nome do segundo aluno:')
aluno3 = input('Digite o nome do terceiro aluno:')
aluno4 = input('Digite o nome do terceiro aluno:')
lista = [aluno4,aluno3,aluno2,aluno1]
venc = random.choice(lista)
print('O aluno escolhido foi {}'.format(venc))
