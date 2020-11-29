import random
al1 = input('Nome dp aluno 1:')
al2 = input('Nome do aluno 2:')
al3 = input('Nome do aluno 3:')
al4 = input('Nome do aluno 4:')
lista = [al1, al2, al3, al4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi: {escolhido}')
