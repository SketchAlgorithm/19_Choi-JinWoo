import sys

def DFS(W, H, N):
    global answer, dp
    if W==N and H==N:
       answer+=1
    if W>N or H>N:
        return
    DFS(W+1, H, N)
    if W>H:
        DFS(W, H+1, N)

while True:

    answer = 0
    N = int(sys.stdin.readline())
    if N == 0:
        break;
    # dp = [[0]*N for _ in range(N)]
    # print(dp)
    DFS(0, 0, N)
    print(answer)

