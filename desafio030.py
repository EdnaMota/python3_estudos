from termcolor import colored
num = int(input(colored(f'Me diga um número qualquer: ', 'cyan')))
resultado = num % 2
if resultado == 0:
    print(f'O número {num} é PAR.')
else:
    print(f'O número {num} é ÍMPAR.')
