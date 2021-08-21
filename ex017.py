temp = float (input('Qual a temperatura na sua região? Cº'))
F = (temp * 9/5) + 32
K = temp + 273.15
print('A temperatura em Cº é {:.1f}, em F {:.1f} e em K {:.1f}'.format(temp, F, K))