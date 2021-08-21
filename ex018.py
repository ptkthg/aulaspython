km = float (input('Quantos km foram percorridos?'))
dia = int (input('Quantos dias ele percorreu?'))
preco = (60* dia) + (km * 0.15)
print('Foram percorridos {}km e, o preço a pagar é de R${:.2f}'.format(km,preco))
