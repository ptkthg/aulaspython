sal = float (input('Qual o salário do funcionário?'))
if sal <=1250:
    novo = sal + (sal*15/100)
else:
    novo = sal + (sal*10/100)
print('O novo salário é R${}'.format(novo))