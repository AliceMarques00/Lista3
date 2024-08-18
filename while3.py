while True:

    nome = input('Digite o seu nome (maior que 3 caracteres): ')
    if len(nome) <= 3:
        print('ERRO! O nome precisa ter mais de 3 caracteres.')
        continue

    idade = int(input('Digite a sua idade: '))
    if idade < 0 or idade > 150:
        print('ERRO! A idade precisa ser entre 0 e 150.')
        continue

    salario = float(input('Digite o seu salário: '))
    if salario <= 0:
        print('ERRO! O salário precisa ser maior que 0!')
        continue

    sexo = input('Digite o seu sexo (f/m): ').strip().lower()
    if sexo not in ['f', 'm']:
        print('ERRO! Precisa responder com f ou m.')
        continue

    estado_civil = input('Digite o seu estado civil (s/c/v/d): ').strip().lower()
    if estado_civil not in ['s', 'c', 'v', 'd']:
        print('ERRO! A resposta precisa ser (s/c/v/d).')
        continue

    print(f'Seu nome foi validado: {nome}')
    print('Idade validada!')
    print('Salário validado!')
    print('Sexo validado!')
    print('Estado Civil validado!')
    break
