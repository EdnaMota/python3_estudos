sal = float(input('Qual é o salário do funcionário? R$ '))
quinze = (sal * 0.15) + sal
dez = (sal * 0.10) + sal
if sal >= 1250:
    print(f'Quem ganhava R$ {sal:.2f} passa a ganhar R$ {dez:.2f} agora.')
else:
    print(f'Quem ganhava R$ {sal:.2f} passa a ganhar R$ {quinze:.2f} agora.')