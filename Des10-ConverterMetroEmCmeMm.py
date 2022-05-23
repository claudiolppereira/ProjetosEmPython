valor = float(input('Digite o valor em metro: '))
centimetro = valor * 100
milimetro = valor * 1000
print('{:.2f}m equivale a: {:.2f}cm'.format(valor, centimetro))
print('{:.2f}m equivale a: {:.2f}mm'.format(valor, milimetro))
