import math
cato = float (input('Digite o cateto oposto: '))
cata = float (input('Digite o cateto adjascente: '))
hipo = math.hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
