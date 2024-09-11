N = int(input())
lista = [int(i) for i in input(0).split()]
operacoes=0

for _ in range(int(N/2)):
  if (lista[0] != lista[-1]):
    lista[0] = lista[0] + lista[1]
    operacoes+=1
    if(lista[0] != lista[-1]):
      lista[0] = lista[0] - lista[1]
      lista[-1] = lista[-1] + lista[-2]
    else:
      lista.pop()
      lista.pop(0)
  else:
    lista.pop()
    lista.pop(0)

print(operacoes)