nome = str(input('Qual é seu nome?'))
if nome == 'Patrick':
    print('Que nome bonito!')
elif nome == 'Lucas':
    print('Que nome feio!!')
elif nome in 'Ana, Luis, Felipe, Rose, Paulo, Jessica':
    print('Que nome popular!')
else:
    print('Que nome normal!')
print('Tenha um bom dia {}'.format(nome))