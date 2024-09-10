s = int(input())
a = int(input())
b = int(input())


# menor
maior = 0
menor = 0
for i in range(a,b+1):
    soma = 0
    for digit in str(i):
        soma += int(digit)
    if soma == s:
        maior = i
    if soma == s and menor ==0:
        menor = i
print(menor)
print(maior)
