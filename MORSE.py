C = int(input())

### n is '-' and m is 'o'

for i in range(0, C):
    n, m, k = input().split()
    n = int(n)
    m = int(m)
    k = int(k)
    list = [1]
    for i in range(1, m+n):
        list.append(list[i-1]*i)

    str = ""
    while True:
        if n is 0 and m is 0:
            print(str)
            break
        temp = list[m+n-1]/(list[n-1]*list[m])
        if k <= temp:
            str = str + "-"
            n -= 1
        else:
            str = str + "o"
            m -= 1
            k -= temp
















