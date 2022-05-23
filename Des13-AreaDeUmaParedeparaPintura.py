largura = float(input('Digite a largura da parede em m: '))
altura = float(input('Digite a altura da parede em m: '))
area = largura * altura
total_tinta = (0.5 * area)
print('A área da parede é equivalente a: {}m²'.format(area))
print('O total de tinta a ser utilizado para pintar toda a parede equivale a: {} litro(s)'.format(total_tinta))
