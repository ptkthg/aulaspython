
print('=='*20)
nome = str (input('Qual o seu nome?'))
print('Seja bem vindo a Vila Militar, {}'.format(nome))
idade = int (input('Qual a sua idade?'))
print('=='*20)
if idade < 18:
    print('{}, ainda não está na hora você de se alistar'.format(nome))
elif idade == 18:
    print('{}, está na hora de se alistar'.format(nome))
else:
    idade > 18
    print('{},já passou da hora de se alistar'.format(nome))