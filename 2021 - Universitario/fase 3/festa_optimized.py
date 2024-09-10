N = int(input())
M = int(input())
entrada = [int(i) for i in range(1,N+1)]
remover = [False]*N

for _ in range(M): #quantos loops
    a = int(input())
    for i in range(a-1, N, a): #posicao
        remover[i] = True
        
for i in range(N):
    if not remover[i]:
        print(entrada[i])

