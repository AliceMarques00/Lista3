populacaoA = 80000
populacaoB = 200000
taxa_crescimentoA = 0.03  # 3%
taxa_crescimentoB = 0.015  # 1.5%
anos = 0

while populacaoA < populacaoB:
    populacaoA += populacaoA * taxa_crescimentoA
    populacaoB += populacaoB * taxa_crescimentoB
    anos += 1

print(f'Número de anos necessários para a população de A ultrapassar ou igualar a de B: {anos}')
