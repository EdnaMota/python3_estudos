print('-=' * 13)
print('Analisador de Triângulos: ')
print('-=' * 13)
l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print(f'Os segmentos acima PODEM formar um triângulo', end=" ")
    if l1 != l2 != l3 != l1:
        print('escaleno.') #tds os lados diferentes
    elif l1 == l2 == l3:
        print('equilátero.') #tds os lados iguais
    elif l1 == l2 or l1 == l3 or l2 == l3 or l3 == l2: #else: (só ISSO!)
        print('isósceles.')# dois lados iguais
else:
    print(f'Os segmentos acima NÃO PODEM formar triângulo!')
