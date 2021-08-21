import math
ang = float (input('Qual o angulo que você deseja?'))
sen = math.sin(math.radians(ang))
cos = math.cos (math.radians(ang))
tan = math.tan (math.radians (ang))
print('O seno é {:.2f}\no cosseno {:.2f}\ne a tangente {:.2f}'.format(sen, cos, tan))