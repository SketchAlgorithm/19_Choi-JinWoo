import sys

def DFS(W, H):
    global answer, dp

    if W<0 or H<0:
        return 0
    elif W==0 and H==0:
        return 1
    elif dp[W][H]!=0:
        return dp[W][H]

    dp[W][H] = (DFS(W - 1, H + 1) + DFS(W, H - 1))
    return dp[W][H]

while True:

    answer = 0
    N = int(sys.stdin.readline())
    if N == 0:
        break;
    dp = [[0]*(N+1) for _ in range(N+1)]
    # print(dp)
    DFS(0, 0)
    print(DFS(N, 0))

