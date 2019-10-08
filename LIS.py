#Longest Increasing Sequence
T = int(input())
answer = []
for case in range(T):
    N = int(input())
    L = [0 for i in range(N)]
    arr =  list(map(int, input().split()))
    for i in range(0, N):
        for j in range(i+1, N):
            if arr[i]<arr[j] and L[i]+1>L[j]:
                L[j]= L[i] + 1
    print(max(L)+1)



