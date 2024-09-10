N= int(input())

if N>5:
    print("IIIII")
    for _ in range(N-5):
        print("I", end="")
elif N == 0:
    print("*")
    print("*")
else:
    for _ in range(N):
        print("I", end="")
    print("\n*")
