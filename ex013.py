dinheiro = float (input('Quanto dinheiro você tem na carteira? R$'))
dolar = dinheiro /5.22
euro = dinheiro / 6.18
print("Com {:.2f} R$ você pode comprar {:.2f} $ dollares e {:.2f}€ euros".format(dinheiro, dolar, euro))