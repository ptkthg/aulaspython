from datetime import date
anoatual = date.today().year
ano = int(input('Digite o ano do seu nascimento:'))
idade = anoatual - ano
print('De acordo com seu ano de nascimento que é {}, você tem {} anos.'.format(ano,idade))
if idade <= 9:
    print('Você têm {} anos e é um atleta MIRIM'.format(idade))
elif idade <=14:
    print('Você têm {} anos e é um atleta INFANTIL'.format(idade))
elif idade <=19:
    print('Você têm {} anos e é um atleta JUNIOR'.format(idade))
elif idade <=25:
    print('Você têm {} anos e é um atleta SENIOR'.format(idade))
else:
    print('Você têm {} anos e é  um atleta MASTER'.format(idade))