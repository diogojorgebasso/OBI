n = int(input())
entrada = []

for _ in range(n):
    a = int(input())
    entrada.append(a)

final = []
for a in entrada:
    if a == 0:
        final.pop()
    else:
        final.append(a)
        
print(sum(final))
