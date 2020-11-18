from random import randint
from time import sleep
from termcolor import colored
pc = randint(0, 5)
print(colored('-=-', 'yellow') * 20)
print(colored('Vou pensar em um número entre 0 e 5. Tente adivinhar...', 'blue'))
print(colored('-=-', 'yellow') * 20)
resp = int(input('Em que número eu pensei? '))
print(colored('PROCESSANDO...', 'magenta'))
sleep(2)
if resp == pc:
    print(colored('YES! PARABÉNS! Você conseguiu me vencer!', 'green'))
elif pc != resp >= 5:
    print(colored('\nVocê escolheu um número acima de 5, imbecil.', 'cyan'))
else:
    print(colored(f'GANHEI! Eu pensei no {pc} e não no {resp}.', 'red'))


    ##print('\nDeixa eu pensar...')
    ##time.sleep(1)
    ##print('\no PC escolheu o nº {0} e o seu palpite foi {1}. Logo, vc perdeu!!'.format(a, b))
##else:
    ##print('\nvc escolheu um número acima de 5')