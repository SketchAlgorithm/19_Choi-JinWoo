import math

for t in range(int(input())):
    n = int(input())
    cnt = 0
        if n == 2:
    while True:
            break
        # n이 1일때 처리를 안해주면 무한루프를 돈다.
        if n == 1:
            cnt += 1
            break
        # n보다 작거나 같은 최대의 제곱수를 구한다. ex) 8 -> 2
        tmp = int(math.sqrt(n))
        if pow(tmp, 2) == n:  # n이 제곱수
            cnt += 1
            n = int(math.sqrt(n))
        else:
            cnt += (pow(tmp + 1, 2) - n)  # n보다 큰 최소의 제곱수에서 n을 빼서 횟수에 추가
            cnt += 1  # 제곱근 구하는 횟수 추가
            n = int(math.sqrt(n)) + 1
        c