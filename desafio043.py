peso = float(input('Qual o seu peso? '))
alt = float(input('Qual a sua altura? '))
imc = peso / (alt ** 2)
print(f'Seu IMC é {imc:.1f}.')
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc == 18.5 or imc <= 25:
    print('Você está com o peso ideal.')
elif imc > 25 or imc < 30:
    print('Você está com sobrepeso.')
else:
    print('Você está com obesidade mórbida.')
