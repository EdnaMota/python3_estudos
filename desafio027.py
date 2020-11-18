from time import sleep
n = str(input('Digite seu nome completo: ')).strip() ##fatia o nome inteiro divide os espaços
nome = n.split()
sleep (2)
print(f'Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu último nome é {nome[-1]}') ## -1, é o último objeto da lista
