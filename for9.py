cont_pares = 0
cont_impares = 0

print("Usando for")
for _ in range(10):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1

print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números ímpares: {cont_impares}")

cont_pares = 0
cont_impares = 0
contador = 0

print("\nUsando while")
while contador < 10:
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        cont_pares += 1
    else:
        cont_impares += 1
    contador += 1

print(f"Quantidade de números pares: {cont_pares}")
print(f"Quantidade de números ímpares: {cont_impares}")
