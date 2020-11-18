sexo = str(input('Informe seu sexo [ Masculino / Feminino / Outro ]: ' )).strip().upper() # se usar '[0]' no final, só pega a primeira letra do que foi digitado
while sexo not in ['M', 'F', 'O', 'MASCULINO', 'FEMININO', 'OUTRO']:
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
print(f"Sexo '{sexo}' registrado com sucesso!")
