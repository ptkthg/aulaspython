largura = float (input('Qual a largura da parede? '))
altura = float (input('Qual a altura da parede? '))
area = largura* altura
tinta = area /2
print('Sua parede tem dimensão de {}x{} e a sua área é de {}m2'.format(largura, altura, area))
print('Para pintar essa parede você precisara de {}l de tinta'.format(tinta))