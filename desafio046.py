from time import sleep
from termcolor import colored
print('*-' * 10)
print('CONTAGEM REGRESSIVA:')
print('*-' * 10)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(colored('HAPPY NEW YEAR!','yellow'))
