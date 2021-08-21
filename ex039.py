vcasa = float (input('Qual o valor da casa? R$'))
sal = float (input('Qual o salário do comprador? R$'))
anos = int (input('Em quantos anos ele vai pagar? '))
prestação = vcasa/(anos*12)
minimo = sal * 30/100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(vcasa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo concedido!')
else:
    print('Emprestimo NEGADO!!')