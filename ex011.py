alt = float(input('Digite a altura da parede: \n'))
lar = float(input('Digite a largura da parede: \n'))

area = alt * lar
qtdTinta = area / 2

print('Será necessário {:.2f} litros de tinta para pintar {:.2f}m²'.format(qtdTinta, area))
