from time import sleep
from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('Suas opções: ')
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' * 15)
print(f'O computador jogou {itens[computador]}.')
print(f'O jogador jogou {itens[jogador]}.')
print('-=' * 15)
if computador == 0: # Pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print(f'O JOGADOR VENCEU!')
    elif jogador == 2:
        print(f'O COMPUTADOR VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA.')
elif computador == 1: # Papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE.')
    elif jogador == 2:
        print('O JOGADOR VENCEU!')
    else:
        print('OPÇÃO INVÁLIDA.')
elif computador == 2: # Tesoura
    if jogador == 0:
        print('O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE.')
    else:
        print('OPÇÃO INVÁLIDA.')
else:
    print('Opção inválida. Tente novamente.')