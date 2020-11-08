# def answer(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 2
#
#     if n%2==0:
#         return answer(n/2) + 2
#     else:
#         return answer(n+1) + 1

from _collections import deque

#가능한 연산 : 전체 복사, 붙여넣기, 1개 삭제

s = int(input())
dp = [[-1]*1001 for _ in range(1001)]
dp[1][0] = 0  # 화면 1개, 클립보드 0개

q = deque()
q.append((1,0))

while q:    #q가 empty일 때까지
    S, C = q.popleft()
    #복사
    if dp[S][S] == -1:
        dp[S][S] = dp[S][C]+1
        q.append((S, S))

    #붙여넣기
    if S+C<=1000 and dp[S+C][C] == -1:
        dp[S+C][C] = dp[S][C] + 1
        q.append((S+C, C))

    if S>=1 and dp[S-1][C] == -1:
        dp[S - 1][C] = dp[S][C] + 1
        q.append((S - 1, C))

ans = 1000
for i in range(s):
    if dp[s][i] != -1 and dp[s][i]<ans:
        ans = dp[s][i]
# print(dp)
print(ans)