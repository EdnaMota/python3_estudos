print('-=' * 16)
print(f'***** ATACADÃO MOTOLIVEIRA *****')
print('-=' * 16)
preço = float(input('Qual o preço das compras? R$ '))
print('[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais')
avd = preço - (preço * 0.10)
avc = preço - (preço * 0.05)
parc = preço + (preço * 0.20)
cond = str(input('Qual a condição de pagamento? '))
if cond == '1':
    print(f'O pagamento ficará no valor de R$ {avd:.2f}.')
elif cond == '2':
    print(f'O pagamento ficará no valor de R$ {avc:.2f}.')
elif cond == '3':
    print(f'O pagamento sem juros é de R$ {preço:.2f}.')
elif cond == '4':
    vez = int(input('Em quantas vezes você quer pagar? '))
    if vez < 3:
        print(f'Opção inválida. Digite um  número de parcelas igual ou maior que 3.')
    else:
        print(f'Sua compra de R$ {preço:.2f} dividida em {vez} parcelas de R$ {parc / vez:.2f} terá o total de R$ {parc:.2f}.')
else:
    print(f'Opção inválida, tente novamente.')