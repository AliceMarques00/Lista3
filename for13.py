n = int(input("Digite o número de notas: "))

soma = 0

for _ in range(n):
    nota = float(input("Digite uma nota: "))
    soma += nota

media = soma / n

print(f"A média das {n} notas é {media:.2f}")
