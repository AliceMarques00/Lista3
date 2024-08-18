n = int(input("Digite o número de termos para gerar a série de Fibonacci: "))

a, b = 1, 1

print("Série de Fibonacci:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
