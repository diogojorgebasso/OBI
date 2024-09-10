N = int(input())

amigos = {}

acoes = []

for _ in range(N):
    acao, numero = [str(x) for x in input().split()]
    acoes.append([acao, int(numero)])

#criar amigos - O(n)
for [estado, amigo] in acoes:
  if estado != "T":
    amigos[amigo] = 0

# O(n²)
for i in amigos:
    total = 0
    passed = False
    print(f"printing friend {i}")
    for index, [estado, amigo] in enumerate(acoes):
        if i==amigo:
            if estado == "R":
                total = total - index
                passed = True
            else:
                total = total + index
                passed = False
        if estado == "T" and passed:
           total = total + amigo - 2
    amigos[i] = total

#O(n)
for amigo, valor in sorted(amigos.items()):
   if valor < 0:
      valor = -1
   print(amigo, valor)

# O(n) + O(n²) + O(n) = O(n² + 2n) = O(n²)