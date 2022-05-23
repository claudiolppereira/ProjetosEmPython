nome = input('Digite o Nome do Aluno: ')
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media_nota = (nota1 + nota2)/2
print('\n {} \n nota 1: {:.2f} \n nota 2 {:.2f}'.format(nome, nota1, nota2))
print('Sua média é: {:.2f}'.format(media_nota))
