salario = float (input('Qual o salário do funcionário? R$'))
aum = salario + (salario *15/100)
print('O funcionário recebia R${:.2f} e agora, com o aumento de 15%, recebe R${:.2f}'.format(salario, aum))