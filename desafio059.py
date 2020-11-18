from time import sleep
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    sleep(1)
    opção = int(input('>>>>>> Qual é a sua opção? '))
    sleep(1)
    if opção == 1:
        r1 = v1 + v2
        print(f'O resultado de {v1} + {v2} é {r1}.')
    elif opção == 2:
        r2 = v1 * v2
        print(f'O resultado de {v1} x {v2} é {r2}.')
    elif opção == 3:
        if v1 == v2:
            print('Os números são iguais.')
        elif v1 > v2:
            print(f'O número {v1} é maior.')
        else:
            print(f'O número {v2} é maior.')
    elif opção == 4:
        print('Informe os números novamente: ')
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opção Inválida. Tente novamente.')
print('Fim do Programa. Volte Sempre!')