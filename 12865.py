N, K = map(int, input().split(" "))

w = [0]
v = [0]

for _ in range(N):
    x, y = map(int, input().split(" "))
    w.append(x)
    v.append(y)

# N+1 * N+1 리스트 생성
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        if j >= w[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][K])