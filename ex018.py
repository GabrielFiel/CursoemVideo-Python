import math

angulo = float(input('Digite um ângulo: \n'))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O seno de {} é {}.'.format(angulo, seno))
print('O cosseno de {} é {}.'.format(angulo, cosseno))
print('A tangente de {} é {}.'.format(angulo, tangente))

