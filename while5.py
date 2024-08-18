populacaoA=int(input('Digite quantas pessoas tem na população A: '))
populacaoB = int(input('Digite quantas pessoas tem na população B: '))
taxa_crescimentoA = float(input('Informe a taxa de crescimento da população A: '))
taxa_crescimentoB = float(input('Informe a taxa de crescimento da população B: '))
anos=0

while populacaoA < populacaoB:
    populacaoA += populacaoA * taxa_crescimentoA
    populacaoB += populacaoB * taxa_crescimentoB
    anos += 1

print(f'Número de anos necessários para a população de A ultrapassar ou igualar a de B: {anos}')
