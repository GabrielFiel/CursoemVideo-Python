import math

ca = float(input('Digite o cateto adjacente: \n'))
co = float(input('Digite o cateto oposto: \n'))

hipotenusa = math.hypot(ca, co)

print('A hipotenusa é igual a {:.3f}.'.format(hipotenusa))
