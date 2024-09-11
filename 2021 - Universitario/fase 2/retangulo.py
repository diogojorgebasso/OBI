from itertools import combinations

def generate_all_combinations(numbers):
    all_combinations = []
    
    # Para cada tamanho de combinação possível de 1 até o tamanho total do conjunto
    for r in range(2, len(numbers)):
        # Gerar todas as combinações de tamanho r
        comb = set()
        comb = combinations(numbers, r)
        # Adicionar cada combinação à lista de todas as combinações
        all_combinations.extend(comb)
    
    return all_combinations

N = int(input())
A = [int(i) for i in input().split()]
combinations_list = generate_all_combinations(A)

for a in combinations_list:
    print(sum(a))