casa = float(input('Qual é o valor da casa? R$ '))
sal = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você vai pagar? '))
pagar = anos * 12
prestação = casa / pagar
limpres = (sal * 0.30)
print(f'O valor da prestação será de R$ {prestação:.2f} e 30% do seu salário é {limpres}.')
if limpres <= prestação:
    print('Você não tem autorização para comprar a casa. Vai ter que ficar aí mesmo.')
else:
    print('Parabéns! Seu financiamento foi aprovado! Já pode queimar a casa antiga!')

