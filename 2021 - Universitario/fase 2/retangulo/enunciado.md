
# Retângulo

Vô Pedro é um fazendeiro meticuloso. Em sua fazenda ele tem uma plantação no formato circular, com algumas árvores plantadas exatamente na circunferência da plantação. A figura (a) abaixo mostra a plantação com as árvores.

Agora vô Pedro quer usar uma longa corda e quatro das árvores para demarcar um retângulo na plantação, usando as árvores como vértices, com a corda marcando os lados. A figura (b) abaixo mostra dois retângulos que podem ser demarcados usando as árvores na plantação da figura (a).

![Retângulo](2021f2p1_retangulo.png)

Dada a descrição das posições das árvores na plantação circular de vô Pedro, sua tarefa é determinar se é possível demarcar um retângulo conforme descrito acima.

## Entrada

A primeira linha da entrada contém um inteiro `N` indicando o número de árvores na circunferência da plantação. As árvores são representadas como pontos na circunferência. A segunda linha contém `N` inteiros `L1, L2, …, LN`, indicando o comprimento do arco entre cada par de árvores consecutivas. Os arcos são dados no sentido anti-horário.

## Saída

Seu programa deve produzir uma única linha, contendo um único caractere, que deve ser `S` se é possível demarcar um retângulo usando as árvores como vértices, ou `N` caso contrário.

## Restrições

- `4 ≤ N ≤ 10^5`
- `1 ≤ L_i ≤ 10^6` para `i = 1,2,…,N`

### Informações sobre a pontuação

- Para um conjunto de casos de testes valendo 20 pontos, `N ≤ 100`.
- Para um conjunto de casos de testes valendo outros 20 pontos, `N ≤ 300`.
- Para um conjunto de casos de testes valendo outros 20 pontos, `N ≤ 1000`.
- Para um conjunto de casos de testes valendo outros 40 pontos, nenhuma restrição adicional.

## Exemplos

### Entrada

```
8
3 3 4 2 6 2 2 2
```

### Saída

```
S
```

### Entrada

```
4
14 16 15 15
```

### Saída

```
N
```

### Entrada

```
6
3 7 7 3 10 10
```

### Saída

```
S
```
