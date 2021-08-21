from datetime import date
ano = int(input('Que ano você que analisar? Coloque 0 para analisar o ano atual:'))
if ano % 4 and ano % 100 !=0 or ano% 400 == 0:
    ano = date.today().year
    print('O ano de {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
