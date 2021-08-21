d = float(input('Digite a distância que será percorrida na viagem: '))
preço = d*0.50
preçod = d* 0.45
if d < 200:
       print('Sua viagem foi de {:.1f}Km, você pagou R${:.2f} nela'.format(d, preçod))
else:
    print('Sua viagem foi de {:.1f}Km, você pagou R${:.2f} nela'.format(d, preço))