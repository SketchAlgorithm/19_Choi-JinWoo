a = 0
first, second = input().split()
first = int(first)
second = int(second)

k = second/first
if k != int(k):
    print(-1)
else:
    while True:

        if k == 1:
            print(a)
            break
        elif k > 1:
            if k % 2 == 0:
                k = k / 2
                a += 1
            elif k % 3 == 0:
                k = k / 3
                a += 1
            else:
                print(-1)
                break







