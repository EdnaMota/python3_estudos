from time import sleep
from random import randint
print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?')
pc = randint(0, 10)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente outra vez: ')
        else:
            print('Menos... Tente outra vez: ')
print(f'Isso! O número era {pc}.\nAcertou com {palpites} tentativa(s).')
