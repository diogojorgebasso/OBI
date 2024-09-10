N = str(input())

cartas = {"C": [], "E": [], "U": [], "P": []}

for i in range(0, len(N), 3):
    if N[i:i+2] not in cartas[N[i+2]] and cartas[N[i+2]] != "erro":
        cartas[N[i+2]].append(N[i:i+2])
    else:
        cartas[N[i+2]] = "erro"

for i in cartas.values():
    if i == "erro":
        print("erro")
    else:
        print(13-len(i))
