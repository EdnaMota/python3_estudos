from termcolor import colored
vel = float(input('Qual é a velocidade atual do carro? '))
mul = (vel-80) * 7
if vel > 80:
    print(colored(
        f'MULTADO! Você excedeu o limite permitido que é de 80Km/h.\nVocê deve pagar uma multa de R$ {mul:.2f}!',
        'red'))
print(colored('Tenha um bom dia! Dirija com segurança!', 'yellow'))