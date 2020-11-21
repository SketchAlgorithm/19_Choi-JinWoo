import sys
N, Q = map(int, sys.stdin.readline().split(" "))
A = list(map(int, sys.stdin.readline().split(" ")))
Q_list = list(map(int, sys.stdin.readline().split(" ")))

S = []
for i in range(N):
    sub_S = A[i]
    for j in range(1, 4):
        sub_S *= A[(i + j) % N]
    S.append(sub_S)
answer = sum(S)
for Q_idx in Q_list:
    for x in range(0, 4):
        S[(Q_idx - 1 - x) % N] *= -1
        answer += 2*S[(Q_idx-1-x) % N]
    print(answer)

