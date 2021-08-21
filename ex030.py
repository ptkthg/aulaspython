v = float(input('Qual a velocidade em Km/h? '))
multa = (v - 80) * 7
if v > 80:
    print('Você pagara {} de multa'.format(multa))
else:
    print('Você não pagara multa.')
