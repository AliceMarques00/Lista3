while True:
    try:
        numero = int(input("Digite um número entre 1 e 10 para ver a tabuada (ou 0 para sair): "))

        if numero == 0:
            print("Encerrando o programa.")
            break
        if 1 <= numero <= 10:
            print(f"\nTabuada do {numero} (usando for):")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")

            print(f"\nTabuada do {numero} (usando while):")
            i = 1
            while i <= 10:
                print(f"{numero} x {i} = {numero * i}")
                i += 1
        else:
            print("ERRO! O número deve estar entre 1 e 10.")

    except ValueError:
        print("ERRO! Entrada inválida. Digite um número inteiro.")
