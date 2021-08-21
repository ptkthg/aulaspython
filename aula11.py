
n1 = float (input('Digite a primeira nota do aluno: '))
n2 = float (input('Digite a segunda nota do aluno:'))
media = (n1+n2)/2
if media < 6.5:
    print('A nota do aluno foi \033[31m{} e ele foi reprovado!!'.format(media))
else:
    print('A nota do aluno foi \033[32m{} e ele foi aprovado!!'.format(media))