A = int(input())
answer = 0
senhas= []

for _ in range(A):
    senhas.append(input().strip())
    
answer = 0

for i in range(A):
    for j in range(A):
        if i != j and senhas[i] in senhas[j]:
            answer += 1
        
print(answer)
