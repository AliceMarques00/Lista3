n = int(input("Digite um número inteiro para verificar se é primo: "))

primo = True

if n <= 1:
    primo = False
else:
  
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            primo = False
            break

if primo:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
