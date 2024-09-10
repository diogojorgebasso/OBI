jogadores = []

for _ in range(4):
  jogadores.append(int(input()))

jogadores = sorted(jogadores)
diff1 = jogadores[1] - jogadores[0]
diff2 = jogadores[3] - jogadores[2]
print(diff2-diff1)