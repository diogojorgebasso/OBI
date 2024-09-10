vitorias = 0

for _ in range(6):
    a = str(input())
    if a == 'V':
        vitorias=vitorias+1

if vitorias == 0:
    print("-1")
elif vitorias <= 2:
    print("3")
elif vitorias <= 4:
    print("2")
else:
    print("1")
