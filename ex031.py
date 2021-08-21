from random import randint
computador = randint(0,5)
n = int (input('Em qual número você pensou?'))
print('Você pensou no número {} e eu no número {}:'.format(n,computador))
if n == computador:
    print('Você ganhou!!')
else:
    print('Você perdeu!!')
